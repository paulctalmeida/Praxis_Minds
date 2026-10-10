/* Praxis Minds website: week planner, task calculator, contact form. No dependencies. */
(function () {
  "use strict";

  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function fmtDuration(hours) {
    var total = Math.round(hours * 60);
    var h = Math.floor(total / 60);
    var m = total % 60;
    if (h && m) return h + " h " + m + " min";
    if (h) return h + " h";
    return m + " min";
  }

  function fmtNumber(n) {
    return Math.round(n).toLocaleString("en-GB");
  }

  /* ---------- Week planner ---------- */
  var week = document.getElementById("week");
  if (week) {
    var btnNow = document.getElementById("week-now");
    var btnAfter = document.getElementById("week-after");
    var statBusy = document.getElementById("stat-busy");
    var statBack = document.getElementById("stat-back");
    var busyNow = 0;
    var busyAfter = 0;

    week.querySelectorAll(".blk.busy").forEach(function (el) {
      busyNow += parseFloat(el.style.getPropertyValue("--d")) || 0;
      busyAfter += parseFloat(el.style.getPropertyValue("--a")) || 0;
    });

    var userTouched = false;

    function setWeek(after) {
      week.classList.toggle("is-after", after);
      btnNow.setAttribute("aria-pressed", String(!after));
      btnAfter.setAttribute("aria-pressed", String(after));
      statBusy.textContent = fmtDuration(after ? busyAfter : busyNow);
      statBack.textContent = after ? fmtDuration(busyNow - busyAfter) : "0 h";
    }

    btnNow.addEventListener("click", function () { userTouched = true; setWeek(false); });
    btnAfter.addEventListener("click", function () { userTouched = true; setWeek(true); });
    setWeek(false);

    // Play the before/after once, the first time the planner is on screen.
    if (!reduceMotion && "IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (entries) {
        if (entries.some(function (e) { return e.isIntersecting; })) {
          io.disconnect();
          setTimeout(function () { if (!userTouched) setWeek(true); }, 1600);
        }
      }, { threshold: 0.5 });
      io.observe(week);
    }
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

  function calculate() {
    var c = num(count), m = num(minutes), r = num(rate);
    var hoursYear = (c * m / 60) * WEEKS_PER_YEAR;
    var costYear = hoursYear * r;
    var back = hoursYear * AI_SHARE;
    var weeks = back / HOURS_PER_WORK_WEEK;
    document.getElementById("out-hours").textContent = fmtNumber(hoursYear);
    document.getElementById("out-cost").textContent = "€" + fmtNumber(Math.round(costYear / 10) * 10);
    document.getElementById("out-back").textContent = fmtNumber(back);
    document.getElementById("out-weeks").textContent = weeks < 10 ? weeks.toFixed(1) : fmtNumber(weeks);
    lastResult = { label: task.options[task.selectedIndex].text, count: c, minutes: m, hours: hoursYear };
  }

  if (task && count && minutes && rate) {
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
        var label = task.value === "other" ? "A task" : lastResult.label;
        taskField.value = label + ": about " + fmtNumber(lastResult.count) + " a week, " +
          lastResult.minutes + " minutes each (roughly " + fmtNumber(lastResult.hours) + " hours a year).";
        setTimeout(function () { taskField.focus({ preventScroll: true }); }, 450);
      });
    }
  }

  /* ---------- Copy helpers ---------- */
  function copyText(text, button, sourceEl) {
    var original = button.textContent;
    function done(ok) {
      button.textContent = ok ? "Copied" : "Select and copy";
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
      return "Name: " + data.name + "\nCompany: " + (data.company || "-") + "\nEmail: " + data.email +
        "\n\nThe task:\n" + data.task;
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
      if (!data.name) missing.push("your name");
      if (!data.email || !form.elements.email.checkValidity()) missing.push("a valid email address");
      if (!data.task) missing.push("the task");
      if (missing.length) {
        var list = missing.length > 1
          ? missing.slice(0, -1).join(", ") + " and " + missing[missing.length - 1]
          : missing[0];
        errorEl.textContent = "Please add " + list + ".";
        errorEl.hidden = false;
        return;
      }

      var endpoint = form.getAttribute("data-endpoint");
      if (!endpoint) { showFallback(data); return; }

      var button = form.querySelector("button[type=submit]");
      button.disabled = true;
      button.textContent = "Sending…";
      fetch(endpoint, {
        method: "POST",
        headers: { "Accept": "application/json", "Content-Type": "application/json" },
        body: JSON.stringify(data)
      }).then(function (res) {
        if (!res.ok) throw new Error("HTTP " + res.status);
        form.reset();
        fallbackEl.hidden = true;
        sentEl.hidden = false;
      }).catch(function () {
        showFallback(data);
      }).then(function () {
        button.disabled = false;
        button.textContent = "Send";
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
      if (i < taken) { li.classList.add("taken"); li.textContent = "Taken"; }
    });
    var countEl = document.getElementById("slots-count");
    if (countEl) {
      var open = items.length - taken;
      countEl.textContent = open > 0 ? open + " of " + items.length + " places open" : "All founding places are taken";
    }
  }

  var year = document.getElementById("year");
  if (year) year.textContent = String(new Date().getFullYear());
})();
