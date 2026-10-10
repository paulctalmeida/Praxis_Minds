/* Praxis Minds website: header and menu, scroll reveals, service tabs, the example week,
   the task calculator, and the contact form. No dependencies.
   One script for every language: page text lives in the HTML, and the few strings the
   script writes itself are in STRINGS below. The language comes from data-locale on <main>. */
(function () {
  "use strict";

  var STRINGS = {
    en: {
      numberLocale: "en-GB",
      otherTask: "A task",
      prefill: function (label, count, minutes, hours) {
        return label + ": about " + count + " a week, " + minutes + " minutes each (roughly " + hours + " hours a year).";
      },
      copied: "Copied",
      selectAndCopy: "Select and copy",
      composeLabels: { name: "Name", company: "Company", email: "Email", task: "The task" },
      missing: { name: "your name", email: "a valid email address", task: "the task" },
      and: " and ",
      pleaseAdd: function (list) { return "Please add " + list + "."; },
      sending: "Sending…",
      send: "Send",
      taken: "Taken",
      placesOpen: function (open, total) { return open + " of " + total + " places open"; },
      allTaken: "All founding places are taken"
    },
    pt: {
      numberLocale: "pt-PT",
      otherTask: "Uma tarefa",
      prefill: function (label, count, minutes, hours) {
        return label + ": cerca de " + count + " por semana, " + minutes + " minutos de cada vez (aproximadamente " + hours + " horas por ano).";
      },
      copied: "Copiado",
      selectAndCopy: "Selecione e copie",
      composeLabels: { name: "Nome", company: "Empresa", email: "Email", task: "A tarefa" },
      missing: { name: "o seu nome", email: "um email válido", task: "a tarefa" },
      and: " e ",
      pleaseAdd: function (list) { return "Por favor, indique " + list + "."; },
      sending: "A enviar…",
      send: "Enviar",
      taken: "Ocupado",
      placesOpen: function (open, total) { return open + " de " + total + " lugares livres"; },
      allTaken: "Todos os lugares de fundador estão ocupados"
    }
  };

  var localeEl = document.querySelector("[data-locale]");
  var locale = (localeEl && localeEl.getAttribute("data-locale")) || document.documentElement.lang || "en";
  var T = STRINGS[locale.slice(0, 2).toLowerCase()] || STRINGS.en;

  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var hasIO = "IntersectionObserver" in window;

  function fmtDuration(hours) {
    var total = Math.round(hours * 60);
    var h = Math.floor(total / 60);
    var m = total % 60;
    if (h && m) return h + " h " + m + " min";
    if (h) return h + " h";
    if (m) return m + " min";
    return "0 h";
  }

  function fmtNumber(n) {
    return Math.round(n).toLocaleString(T.numberLocale);
  }

  function fmtDecimal(n, digits) {
    return n.toLocaleString(T.numberLocale, { minimumFractionDigits: digits, maximumFractionDigits: digits });
  }

  function fmtEuro(n) {
    return n.toLocaleString(T.numberLocale, { style: "currency", currency: "EUR", minimumFractionDigits: 0, maximumFractionDigits: 0 });
  }

  /* Counts a number up or down to its new value. el._v remembers the last value shown. */
  function tween(el, to, format, done) {
    var from = typeof el._v === "number" ? el._v : to;
    el._v = to;
    if (el._raf) cancelAnimationFrame(el._raf);
    if (reduceMotion || from === to) {
      el.textContent = format(to);
      if (done) done();
      return;
    }
    var start = null;
    var duration = 650;
    function step(now) {
      if (start === null) start = now;
      var p = Math.min(1, (now - start) / duration);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = format(p < 1 ? from + (to - from) * eased : to); // end on the exact value
      if (p < 1) el._raf = requestAnimationFrame(step);
      else { el._raf = null; if (done) done(); }
    }
    el._raf = requestAnimationFrame(step);
  }

  /* ---------- Scroll reveals ----------
     Elements with .reveal, and the children of [data-stagger], fade up as they come on screen.
     The hiding CSS only applies once this runs, so nothing stays hidden if the script fails. */
  (function () {
    var targets = [];
    document.querySelectorAll("[data-stagger]").forEach(function (parent) {
      Array.prototype.forEach.call(parent.children, function (child, i) {
        child.style.setProperty("--rd", i);
        targets.push(child);
      });
    });
    document.querySelectorAll(".reveal").forEach(function (el) { targets.push(el); });
    if (reduceMotion || !hasIO || !targets.length) return;

    document.documentElement.classList.add("reveal-on");

    function finish(el) {
      el.classList.remove("is-visible");
      el.classList.add("is-done");
    }

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        io.unobserve(el);
        el.classList.add("is-visible");
        var delay = (parseFloat(el.style.getPropertyValue("--rd")) || 0) * 90;
        // Hand the element back to its own hover transitions once it has arrived.
        setTimeout(function () { finish(el); }, 1000 + delay);
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.12 });
    targets.forEach(function (el) { io.observe(el); });
  })();

  /* ---------- Header: background on scroll, mobile menu, current section ---------- */
  var head = document.getElementById("site-head");
  if (head) {
    var ticking = false;
    function onScroll() {
      head.classList.toggle("is-scrolled", window.scrollY > 8);
      ticking = false;
    }
    window.addEventListener("scroll", function () {
      if (!ticking) { ticking = true; requestAnimationFrame(onScroll); }
    }, { passive: true });
    onScroll();

    var menuBtn = head.querySelector(".menu-btn");
    var nav = document.getElementById("site-nav");
    if (menuBtn && nav) {
      function setMenu(open) {
        head.classList.toggle("nav-open", open);
        menuBtn.setAttribute("aria-expanded", String(open));
      }
      menuBtn.addEventListener("click", function () { setMenu(!head.classList.contains("nav-open")); });
      nav.addEventListener("click", function (e) { if (e.target.closest("a")) setMenu(false); });
      document.addEventListener("keydown", function (e) {
        if (e.key === "Escape" && head.classList.contains("nav-open")) { setMenu(false); menuBtn.focus(); }
      });
      document.addEventListener("click", function (e) {
        if (head.classList.contains("nav-open") && !head.contains(e.target)) setMenu(false);
      });
      window.addEventListener("resize", function () { if (window.innerWidth > 900) setMenu(false); });
    }

    if (nav && hasIO) {
      var links = {};
      nav.querySelectorAll('a[href^="#"]:not(.btn)').forEach(function (a) { links[a.getAttribute("href").slice(1)] = a; });
      var spy = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          var link = links[entry.target.id];
          if (!link) return;
          if (entry.isIntersecting) {
            Object.keys(links).forEach(function (k) { links[k].classList.toggle("is-active", links[k] === link); });
          } else if (link.classList.contains("is-active")) {
            link.classList.remove("is-active");
          }
        });
      }, { rootMargin: "-40% 0px -55% 0px" });
      Object.keys(links).forEach(function (id) {
        var section = document.getElementById(id);
        if (section) spy.observe(section);
      });
    }
  }

  /* ---------- Example week ----------
     Each .wk-row carries --now (hours today) and --after (hours a person still spends checking).
     The totals are added up here, so the rows in the HTML are the only thing to edit. */
  var week = document.getElementById("week");
  if (week) {
    var btnNow = document.getElementById("week-now");
    var btnAfter = document.getElementById("week-after");
    var statBusy = document.getElementById("stat-busy");
    var statBack = document.getElementById("stat-back");
    var rows = [];
    var busyNow = 0;
    var busyAfter = 0;

    week.querySelectorAll(".wk-row").forEach(function (row) {
      var now = parseFloat(row.style.getPropertyValue("--now")) || 0;
      var after = parseFloat(row.style.getPropertyValue("--after")) || 0;
      busyNow += now;
      busyAfter += after;
      rows.push({ time: row.querySelector(".wk-time"), now: now, after: after });
    });

    function fmtSteps(h) { return fmtDuration(Math.round(h * 12) / 12); } // 5-minute steps while counting
    var userTouched = false;

    function setWeek(after) {
      week.classList.toggle("is-after", after);
      btnNow.setAttribute("aria-pressed", String(!after));
      btnAfter.setAttribute("aria-pressed", String(after));
      rows.forEach(function (r) {
        if (!r.time) return;
        r.time.textContent = "";
        if (after) {
          var was = document.createElement("s");
          was.textContent = fmtDuration(r.now);
          r.time.appendChild(was);
          r.time.appendChild(document.createTextNode(fmtDuration(r.after)));
        } else {
          r.time.textContent = fmtDuration(r.now);
        }
      });
      tween(statBusy, after ? busyAfter : busyNow, fmtSteps);
      tween(statBack, after ? busyNow - busyAfter : 0, fmtSteps);
    }

    btnNow.addEventListener("click", function () { userTouched = true; setWeek(false); });
    btnAfter.addEventListener("click", function () { userTouched = true; setWeek(true); });
    statBusy._v = busyNow;
    statBack._v = 0;
    setWeek(false);

    // Draw the bars, then play the before/after once, the first time the card is on screen.
    if (!reduceMotion && hasIO) {
      var wio = new IntersectionObserver(function (entries) {
        if (entries.some(function (e) { return e.isIntersecting; })) {
          wio.disconnect();
          week.classList.add("is-in");
          setTimeout(function () { if (!userTouched) setWeek(true); }, 2200);
        }
      }, { threshold: 0.4 });
      wio.observe(week);
    } else {
      week.classList.add("is-in");
    }
  }

  /* ---------- Service tabs ----------
     Without JavaScript, every panel shows one after the other. Links to a panel's id
     (#build, #workshops, #more) open that tab. */
  var tabList = document.querySelector('[role="tablist"]');
  if (tabList) {
    var tabs = Array.prototype.slice.call(tabList.querySelectorAll('[role="tab"]'));
    var indicator = tabList.querySelector(".tab-ind");
    var section = tabList.closest("section");
    var panels = tabs.map(function (t) { return document.getElementById(t.getAttribute("aria-controls")); });

    function placeIndicator(tab) {
      if (!indicator || !tab) return;
      indicator.style.width = tab.offsetWidth + "px";
      indicator.style.transform = "translateX(" + tab.offsetLeft + "px)";
    }

    function selectTab(tab, opts) {
      opts = opts || {};
      tabs.forEach(function (t, i) {
        var on = t === tab;
        t.setAttribute("aria-selected", String(on));
        t.tabIndex = on ? 0 : -1;
        var panel = panels[i];
        if (!panel) return;
        var wasHidden = panel.hidden;
        panel.hidden = !on;
        if (on && wasHidden && opts.animate !== false && !reduceMotion) {
          panel.classList.remove("is-entering");
          void panel.offsetWidth; // restart the animation
          panel.classList.add("is-entering");
        }
      });
      placeIndicator(tab);
      if (opts.focus) tab.focus();
      if (tab.scrollIntoView && tabList.scrollWidth > tabList.clientWidth) {
        tabList.scrollTo({ left: tab.offsetLeft - 16, behavior: reduceMotion ? "auto" : "smooth" });
      }
    }

    tabs.forEach(function (tab, i) {
      tab.addEventListener("click", function () { selectTab(tab); });
      tab.addEventListener("keydown", function (e) {
        var next = null;
        if (e.key === "ArrowRight") next = tabs[(i + 1) % tabs.length];
        else if (e.key === "ArrowLeft") next = tabs[(i - 1 + tabs.length) % tabs.length];
        else if (e.key === "Home") next = tabs[0];
        else if (e.key === "End") next = tabs[tabs.length - 1];
        if (next) { e.preventDefault(); selectTab(next, { focus: true }); }
      });
    });

    function tabForHash(hash) {
      var id = (hash || "").replace("#", "");
      for (var i = 0; i < panels.length; i++) { if (panels[i] && panels[i].id === id) return tabs[i]; }
      return null;
    }

    if (section) section.classList.add("tabs-ready");
    var initial = tabForHash(location.hash) || tabs.filter(function (t) { return t.getAttribute("aria-selected") === "true"; })[0] || tabs[0];
    selectTab(initial, { animate: false });
    if (tabForHash(location.hash)) {
      var target = document.getElementById(location.hash.slice(1));
      if (target) setTimeout(function () { target.scrollIntoView(); }, 0);
    }

    document.addEventListener("click", function (e) {
      var a = e.target.closest && e.target.closest('a[href^="#"]');
      var tab = a && tabForHash(a.getAttribute("href"));
      if (tab) selectTab(tab, { animate: false });
    });
    window.addEventListener("hashchange", function () {
      var tab = tabForHash(location.hash);
      if (tab) selectTab(tab, { animate: false });
    });

    var current = function () { return tabs.filter(function (t) { return t.getAttribute("aria-selected") === "true"; })[0]; };
    window.addEventListener("resize", function () { placeIndicator(current()); });
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { placeIndicator(current()); });
  }

  /* ---------- Task calculator ---------- */
  var WEEKS_PER_YEAR = 46;
  var AI_SHARE = 0.7;
  var HOURS_PER_WORK_WEEK = 40;
  var presets = {
    invoices:  { count: 80,  minutes: 5 },
    orders:    { count: 60,  minutes: 4 },
    questions: { count: 100, minutes: 3 },
    quotes:    { count: 15,  minutes: 30 },
    report:    { count: 1,   minutes: 180 }
  };

  var task = document.getElementById("calc-task");
  var count = document.getElementById("calc-count");
  var minutes = document.getElementById("calc-minutes");
  var rate = document.getElementById("calc-rate");
  var lastResult = null;

  function num(input) {
    var v = parseFloat(input.value);
    if (!isFinite(v) || v < 0) return 0;
    var max = parseFloat(input.max);
    return isFinite(max) ? Math.min(v, max) : v;
  }

  if (task && count && minutes && rate) {
    var outHours = document.getElementById("out-hours");
    var outCost = document.getElementById("out-cost");
    var outBack = document.getElementById("out-back");
    var outWeeks = document.getElementById("out-weeks");
    var live = outHours.closest("[aria-live]");
    var pending = 0;

    function settled() { pending -= 1; if (pending <= 0 && live) live.removeAttribute("aria-busy"); }

    function calculate() {
      var c = num(count), m = num(minutes), r = num(rate);
      var hoursYear = (c * m / 60) * WEEKS_PER_YEAR;
      var costYear = hoursYear * r;
      var back = hoursYear * AI_SHARE;
      var weeks = back / HOURS_PER_WORK_WEEK;
      // Keep screen readers from announcing every frame of the count.
      if (live) live.setAttribute("aria-busy", "true");
      pending = 4;
      tween(outHours, hoursYear, fmtNumber, settled);
      tween(outCost, costYear, function (v) { return fmtEuro(Math.round(v / 10) * 10); }, settled);
      tween(outBack, back, fmtNumber, settled);
      tween(outWeeks, weeks, function (v) { return v < 10 ? fmtDecimal(v, 1) : fmtNumber(v); }, settled);
      lastResult = { label: task.options[task.selectedIndex].text, count: c, minutes: m, hours: hoursYear };
    }

    task.addEventListener("change", function () {
      var p = presets[task.value];
      if (p) { count.value = p.count; minutes.value = p.minutes; }
      calculate();
    });
    [count, minutes, rate].forEach(function (el) { el.addEventListener("input", calculate); });
    document.getElementById("calc-form").addEventListener("submit", function (e) { e.preventDefault(); });
    calculate();

    var talk = document.getElementById("calc-talk");
    var taskField = document.getElementById("f-task");
    if (talk && taskField) {
      talk.addEventListener("click", function () {
        if (!lastResult) return;
        var label = task.value === "other" ? T.otherTask : lastResult.label;
        var mins = lastResult.minutes % 1 ? fmtDecimal(lastResult.minutes, 1) : fmtNumber(lastResult.minutes);
        taskField.value = T.prefill(label, fmtNumber(lastResult.count), mins, fmtNumber(lastResult.hours));
        setTimeout(function () { taskField.focus({ preventScroll: true }); }, 600);
      });
    }
  }

  /* ---------- Copy helpers ---------- */
  function copyText(text, button, sourceEl) {
    var original = button.textContent;
    function done(ok) {
      button.textContent = ok ? T.copied : T.selectAndCopy;
      setTimeout(function () { button.textContent = original; }, 1800);
    }
    function selectFallback() {
      if (!sourceEl) return done(false);
      if (sourceEl.select) { sourceEl.focus(); sourceEl.select(); }
      else {
        var range = document.createRange();
        range.selectNodeContents(sourceEl);
        var sel = window.getSelection();
        sel.removeAllRanges();
        sel.addRange(range);
      }
      done(false);
    }
    try {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function () { done(true); }, selectFallback);
      } else { selectFallback(); }
    } catch (err) { selectFallback(); }
  }

  var copyEmail = document.getElementById("copy-email");
  var emailEl = document.getElementById("email-address");
  if (copyEmail && emailEl) {
    copyEmail.addEventListener("click", function () { copyText(emailEl.textContent.trim(), copyEmail, emailEl); });
  }

  /* ---------- Contact form ----------
     Set data-endpoint on the form (for example a Formspree URL) to send messages online.
     Without an endpoint, the visitor gets their message ready to copy into an email. */
  var form = document.getElementById("contact-form");
  if (form) {
    var errorEl = document.getElementById("form-error");
    var sentEl = document.getElementById("form-sent");
    var fallbackEl = document.getElementById("form-fallback");
    var composed = document.getElementById("f-composed");
    var copyMessage = document.getElementById("copy-message");

    function compose(data) {
      var L = T.composeLabels;
      return L.name + ": " + data.name + "\n" + L.company + ": " + (data.company || "-") + "\n" +
        L.email + ": " + data.email + "\n\n" + L.task + ":\n" + data.task;
    }

    function showFallback(data) {
      composed.value = compose(data);
      sentEl.hidden = true;
      fallbackEl.hidden = false;
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      errorEl.hidden = true;
      var data = {
        name: form.elements.name.value.trim(),
        company: form.elements.company.value.trim(),
        email: form.elements.email.value.trim(),
        task: form.elements.task.value.trim()
      };
      var missing = [];
      if (!data.name) missing.push(T.missing.name);
      if (!data.email || !form.elements.email.checkValidity()) missing.push(T.missing.email);
      if (!data.task) missing.push(T.missing.task);
      if (missing.length) {
        var list = missing.length > 1
          ? missing.slice(0, -1).join(", ") + T.and + missing[missing.length - 1]
          : missing[0];
        errorEl.textContent = T.pleaseAdd(list);
        errorEl.hidden = false;
        return;
      }

      var endpoint = form.getAttribute("data-endpoint");
      if (!endpoint) { showFallback(data); return; }

      var button = form.querySelector("button[type=submit]");
      button.disabled = true;
      button.textContent = T.sending;
      fetch(endpoint, {
        method: "POST",
        headers: { "Accept": "application/json", "Content-Type": "application/json" },
        body: JSON.stringify(Object.assign({ language: locale }, data))
      }).then(function (res) {
        if (!res.ok) throw new Error("HTTP " + res.status);
        form.reset();
        fallbackEl.hidden = true;
        sentEl.hidden = false;
      }).catch(function () {
        showFallback(data);
      }).then(function () {
        button.disabled = false;
        button.textContent = T.send;
      });
    });

    if (copyMessage) {
      copyMessage.addEventListener("click", function () { copyText(composed.value, copyMessage, composed); });
    }
  }

  /* ---------- Founding places ---------- */
  var slots = document.querySelector(".slots");
  if (slots) {
    var taken = Math.max(0, Math.min(5, parseInt(slots.getAttribute("data-taken"), 10) || 0));
    var items = slots.querySelectorAll("li");
    items.forEach(function (li, i) {
      if (i < taken) { li.classList.add("taken"); li.textContent = T.taken; }
    });
    var countEl = document.getElementById("slots-count");
    if (countEl) {
      var open = items.length - taken;
      countEl.textContent = open > 0 ? T.placesOpen(open, items.length) : T.allTaken;
    }
  }

  var year = document.getElementById("year");
  if (year) year.textContent = String(new Date().getFullYear());
})();
