// Cảnh báo lũ sông Kôn – Bình Định 2026 · HTK 0396241674
// Dữ liệu mô phỏng – cập nhật 09/11/2026
(function () {
  "use strict";

  var COLORS = { 0: "#1a936f", 1: "#e6b800", 2: "#e8710a", 3: "#d7263d" };
  var STATUS_TEXT = {
    0: "Bình thường",
    1: "Cảnh báo cấp 1",
    2: "Cảnh báo cấp 2",
    3: "Cảnh báo cấp 3 – nguy hiểm"
  };
  var SERIES_COLORS = ["#0b5fa5", "#e8710a", "#1a936f", "#8e44ad", "#d7263d"];

  function stationCard(s) {
    var lv = s.alertLevel;
    var div = document.createElement("div");
    div.className = "card station-card lv" + lv;
    div.innerHTML =
      "<h3>Trạm " + s.name + " <small>(" + s.location + ")</small></h3>" +
      '<p class="station-level">' + s.level.toFixed(2) + " m</p>" +
      '<p class="station-status status-' + lv + '">' + STATUS_TEXT[lv] +
      '<span class="trend-' + s.trend + '"></span></p>' +
      '<p class="thresholds">Ngưỡng: Cấp 1 ≥ ' + s.alert1.toFixed(1) +
      " m · Cấp 2 ≥ " + s.alert2.toFixed(1) +
      " m · Cấp 3 ≥ " + s.alert3.toFixed(1) + " m</p>";
    return div;
  }

  function renderCards(stations) {
    var wrap = document.getElementById("station-cards");
    wrap.innerHTML = "";
    stations.forEach(function (s) { wrap.appendChild(stationCard(s)); });
  }

  function renderChart(stations) {
    var ctx = document.getElementById("levelChart");
    if (!ctx || typeof Chart === "undefined") { return; }
    var labels = stations[0].history.labels;
    var datasets = stations.map(function (s, i) {
      var color = SERIES_COLORS[i % SERIES_COLORS.length];
      return {
        label: "Trạm " + s.name + " (cấp " + (s.alertLevel || "bình thường") + ")",
        data: s.history.values,
        borderColor: color,
        backgroundColor: color + "33",
        tension: 0.3,
        pointRadius: 3,
        fill: false
      };
    });
    new Chart(ctx, {
      type: "line",
      data: { labels: labels, datasets: datasets },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { position: "bottom" },
          title: {
            display: true,
            text: "Mực nước sông Kôn (m) – Dữ liệu mô phỏng – cập nhật 09/11/2026"
          },
          tooltip: {
            callbacks: {
              afterLabel: function (item) {
                var s = stations[item.datasetIndex];
                return "Ngưỡng cấp 1/2/3: " + s.alert1 + " / " + s.alert2 + " / " + s.alert3 + " m";
              }
            }
          }
        },
        scales: {
          y: { title: { display: true, text: "Mực nước (m)" } },
          x: { title: { display: true, text: "Ngày (tháng 11/2026)" } }
        }
      }
    });
  }

  function init() {
    fetch("/api/stations")
      .then(function (r) { return r.json(); })
      .then(function (payload) {
        var note = document.getElementById("data-note");
        if (note && payload.note) { note.textContent = payload.note; }
        renderCards(payload.stations);
        renderChart(payload.stations);
      })
      .catch(function () {
        var wrap = document.getElementById("station-cards");
        if (wrap) {
          wrap.innerHTML =
            '<div class="card"><p>Không tải được dữ liệu. Vui lòng thử lại hoặc gọi Hotline HTK ' +
            '<a href="tel:0396241674">0396241674</a>.</p></div>';
        }
      });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () { setTimeout(init, 0); });
  } else {
    init();
  }
})();