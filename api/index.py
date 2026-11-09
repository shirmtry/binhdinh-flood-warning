# -*- coding: utf-8 -*-
"""Cảnh báo lũ sông Kôn – Bình Định 2026.
Tác giả: HTK · Hotline/Zalo: 0396241674 · Email: htk.contact@gmail.com
Cập nhật: 09/11/2026
"""
from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Dữ liệu mô phỏng – cập nhật 09/11/2026
# 5 trạm mực nước sông Kôn (đơn vị: mét)
STATIONS = [
    {
        "id": "binh-nghi",
        "name": "Bình Nghi",
        "location": "Tây Sơn",
        "level": 7.85,
        "trend": "rising",
        "alert1": 6.5,
        "alert2": 7.5,
        "alert3": 8.5,
        "history": {
            "labels": ["03/11", "04/11", "05/11", "06/11", "07/11", "08/11", "09/11"],
            "values": [5.20, 5.65, 6.10, 6.80, 7.15, 7.50, 7.85]
        }
    },
    {
        "id": "van-phong",
        "name": "Văn Phong",
        "location": "An Nhơn",
        "level": 5.90,
        "trend": "rising",
        "alert1": 5.0,
        "alert2": 6.0,
        "alert3": 7.0,
        "history": {
            "labels": ["03/11", "04/11", "05/11", "06/11", "07/11", "08/11", "09/11"],
            "values": [4.10, 4.45, 4.80, 5.10, 5.40, 5.65, 5.90]
        }
    },
    {
        "id": "an-hoa",
        "name": "An Hòa",
        "location": "Tuy Phước",
        "level": 4.75,
        "trend": "rising",
        "alert1": 3.5,
        "alert2": 4.2,
        "alert3": 4.8,
        "history": {
            "labels": ["03/11", "04/11", "05/11", "06/11", "07/11", "08/11", "09/11"],
            "values": [2.90, 3.20, 3.60, 3.95, 4.30, 4.55, 4.75]
        }
    },
    {
        "id": "thanh-hoa",
        "name": "Thạnh Hòa",
        "location": "Tuy Phước",
        "level": 3.10,
        "trend": "steady",
        "alert1": 3.0,
        "alert2": 3.6,
        "alert3": 4.2,
        "history": {
            "labels": ["03/11", "04/11", "05/11", "06/11", "07/11", "08/11", "09/11"],
            "values": [2.40, 2.60, 2.85, 3.00, 3.05, 3.08, 3.10]
        }
    },
    {
        "id": "binh-tuong",
        "name": "Bình Tường",
        "location": "Tây Sơn",
        "level": 22.40,
        "trend": "falling",
        "alert1": 23.0,
        "alert2": 24.5,
        "alert3": 26.0,
        "history": {
            "labels": ["03/11", "04/11", "05/11", "06/11", "07/11", "08/11", "09/11"],
            "values": [21.80, 22.60, 23.40, 23.10, 22.85, 22.60, 22.40]
        }
    }
]


def alert_level(station):
    """Trả về cấp cảnh báo 0 (bình thường), 1, 2, 3 theo ngưỡng."""
    if station["level"] >= station["alert3"]:
        return 3
    if station["level"] >= station["alert2"]:
        return 2
    if station["level"] >= station["alert1"]:
        return 1
    return 0


def station_payload():
    data = []
    for s in STATIONS:
        item = dict(s)
        item["alertLevel"] = alert_level(s)
        data.append(item)
    return {
        "river": "Sông Kôn",
        "province": "Bình Định",
        "note": "Dữ liệu mô phỏng – cập nhật 09/11/2026",
        "updatedAt": "09/11/2026 08:00",
        "stations": data
    }


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/api/stations')
def api_stations():
    return jsonify(station_payload())


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)