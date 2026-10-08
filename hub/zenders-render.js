// Gedeelde render-functies voor de zenderpagina's (/zenders/<slug>). Wordt gebruikt door de Cloudflare-worker
// (server-side, zichtbaar voor Google) én als fallback in de embed (bv. op de webflow.io-staging).
// Invoer: de ruwe CMS-velden met één regel per item, velden gescheiden door " | ".
var ZP = (function () {
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function unesc(s) { return String(s || "").replace(/&amp;/g, "&").replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&#x27;/g, "'"); }
  function regels(raw) {
    return unesc(raw).split(/\r?\n|<br\s*\/?>/i).map(function (r) { return r.trim(); }).filter(Boolean)
      .map(function (r) { return r.split(/\s+\|\s+/).map(function (x) { return x.trim(); }); });
  }
  var DAG = ["zo", "ma", "di", "wo", "do", "vr", "za"], MND = ["jan", "feb", "mrt", "apr", "mei", "jun", "jul", "aug", "sep", "okt", "nov", "dec"];
  function ams(iso) {
    var d = new Date(iso);
    var p = new Intl.DateTimeFormat("nl-NL", { timeZone: "Europe/Amsterdam", hour: "2-digit", minute: "2-digit", weekday: "short", day: "numeric", month: "numeric", hour12: false }).formatToParts(d);
    var g = {}; p.forEach(function (x) { g[x.type] = x.value; });
    var wd = new Intl.DateTimeFormat("en-US", { timeZone: "Europe/Amsterdam", weekday: "short" }).format(d);
    var dag = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 }[wd];
    return { tijd: g.hour + ":" + g.minute, dag: DAG[dag] + " " + g.day + " " + MND[+g.month - 1] };
  }

  function competities(raw) {
    var r = regels(raw); if (!r.length) return "";
    return '<div class="zp-comp-grid">' + r.map(function (x) {
      var badge = x[2] ? '<span class="zp-badge ' + (/exclusief/i.test(x[2]) ? "zp-badge--excl" : "") + '">' + esc(x[2]) + "</span>" : "";
      return '<div class="zp-comp"><div><div class="zp-comp-naam">' + esc(x[0]) + '</div><div class="zp-comp-sub">' + esc(x[1] || "") + "</div></div>" + badge + "</div>";
    }).join("") + "</div>";
  }
  function providers(raw) {
    var r = regels(raw); if (!r.length) return "";
    return '<table class="zp-tabel"><thead><tr><th>Provider</th><th>Pakket</th><th class="zp-r">Prijs p/m</th></tr></thead><tbody>' +
      r.map(function (x) { return "<tr><td><strong>" + esc(x[0]) + "</strong></td><td>" + esc(x[1] || "") + '</td><td class="zp-r">' + esc(x[2] || "") + "</td></tr>"; }).join("") +
      '</tbody></table><p class="zp-noot">Indicatieve prijzen. Actuele prijs en voorwaarden staan bij de aanbieder.</p>';
  }
  function kanaalnummers(raw) {
    var r = regels(raw); if (!r.length) return "";
    var per = {}, volg = [];
    r.forEach(function (x) { if (!per[x[0]]) { per[x[0]] = []; volg.push(x[0]); } per[x[0]].push(x); });
    return volg.map(function (z) {
      return '<table class="zp-tabel zp-kanaal"><thead><tr><th>Provider</th><th class="zp-r">Kanaalnummer ' + esc(z) + "</th></tr></thead><tbody>" +
        per[z].map(function (x) { return "<tr><td>" + esc(x[1]) + '</td><td class="zp-r"><strong>' + esc(x[2]) + "</strong></td></tr>"; }).join("") + "</tbody></table>";
    }).join("");
  }
  function alternatieven(raw) {
    var r = regels(raw); if (!r.length) return "";
    return '<div class="zp-alt">' + r.map(function (x) {
      var ini = esc((x[0] || "").replace(/[^A-Za-z0-9]/g, "").slice(0, 3).toUpperCase());
      var inner = '<span class="zp-alt-logo">' + ini + '</span><span class="zp-alt-main"><strong>' + esc(x[0]) + "</strong><small>" + esc(x[1] || "") +
        '</small></span><span class="zp-alt-label">' + esc(x[2] || "") + " →</span>";
      return x[3] ? '<a class="zp-alt-item" href="' + esc(x[3]) + '">' + inner + "</a>" : '<div class="zp-alt-item">' + inner + "</div>";
    }).join("") + "</div>";
  }
  function faq(raw) {
    var r = regels(raw).filter(function (x) { return x[0] && x[1]; }); if (!r.length) return "";
    var ld = { "@context": "https://schema.org", "@type": "FAQPage", mainEntity: r.map(function (x) {
      return { "@type": "Question", name: x[0], acceptedAnswer: { "@type": "Answer", text: x.slice(1).join(" | ") } }; }) };
    return '<div class="zp-faq">' + r.map(function (x, i) {
      return "<details" + (i === 0 ? " open" : "") + '><summary>' + esc(x[0]) + '<span class="zp-faq-ico">›</span></summary><p>' + esc(x.slice(1).join(" | ")) + "</p></details>";
    }).join("") + '</div><script type="application/ld+json">' + JSON.stringify(ld).replace(/</g, "\\u003c") + "</script>";
  }

  // 'Deze week op <naam>': uitzendingen waarvan een zender of stream in de lijst van deze dienst staat
  function matcht(lijst, naam) {
    for (var i = 0; i < lijst.length; i++) { var t = lijst[i]; if (naam === t || naam.indexOf(t + " ") === 0) return t; }
    return null;
  }
  function week(schema, zendersAttr, naam, max) {
    var lijst = String(zendersAttr || "").split(",").map(function (s) { return s.trim(); }).filter(Boolean);
    var nu = Date.now(), eind = nu + 7 * 864e5, rows = [];
    ((schema && schema.uitzendingen) || []).forEach(function (u) {
      var t = new Date(u.ko).getTime(); if (t < nu - 2 * 3600e3 || t > eind) return;
      var badge = null;
      (u.zenders || []).some(function (z) { if (matcht(lijst, z)) { badge = z; return true; } });
      if (!badge) (u.streams || []).some(function (s) { if (matcht(lijst, s)) { badge = "Livestream " + s; return true; } });
      if (badge) rows.push({ u: u, badge: badge });
    });
    var head = '<div class="zp-week-head"><span class="zp-eyebrow">Deze week op ' + esc(naam) + '</span><span class="zp-week-count">' +
      rows.length + (rows.length === 1 ? " uitzending" : " uitzendingen") + "</span></div>";
    if (!rows.length) return head + '<p class="zp-leeg">Deze week staan er geen live uitzendingen gepland die wij volgen.</p>';
    return head + rows.slice(0, max || 5).map(function (r) {
      var a = ams(r.u.ko), t = esc(r.u.titel);
      var titel = r.u.url ? '<a href="' + esc(r.u.url) + '">' + t + "</a>" : t;
      return '<div class="zp-week-row"><span class="zp-week-when"><strong>' + a.tijd + "</strong><small>" + a.dag + '</small></span>' +
        '<span class="zp-week-main"><span class="zp-week-titel">' + titel + '</span><small>' +
        esc(r.u.comp && r.u.comp !== r.u.titel ? r.u.comp : (r.u.sport || "").replace(/^./, function (c) { return c.toUpperCase(); })) + '</small></span>' +
        '<span class="zp-pill">' + esc(r.badge) + "</span></div>";
    }).join("") + '<a class="zp-week-more" href="/live-kijken">Volledig uitzendschema →</a>';
  }
  return { competities: competities, providers: providers, kanaalnummers: kanaalnummers, alternatieven: alternatieven, faq: faq, week: week };
})();
if (typeof module !== "undefined") module.exports = ZP;
