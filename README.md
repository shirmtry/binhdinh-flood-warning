# binhdinh-flood-warning — Cảnh báo lũ sông Kôn · Bình Định 2026

Ứng dụng web **Python Flask** theo dõi mực nước sông Kôn và cảnh báo lũ cho vùng hạ lưu Tuy Phước – An Nhơn trong mùa mưa lũ 2026.

- Tác giả: **HTK** · Hotline/Zalo: **0396241674** · Email: **htk.contact@gmail.com**
- Cập nhật: **09/11/2026**
- Dữ liệu: **Dữ liệu mô phỏng – cập nhật 09/11/2026** (mock JSON, không phải số liệu quan trắc chính thức)

## Vấn đề

Tháng 10–11/2026, cao điểm mùa mưa lũ 2026 và bão miền Trung, lũ sông Kôn dâng cao nhanh, đe dọa nhấn chìm các vùng trũng Tuy Phước và An Nhơn. Bão số 9, 10/2026 đổ bộ Quy Nhơn – Phù Cát – Hoài Nhơn gây ngập úng đô thị, sạt lở An Lão – Vĩnh Thạnh – Tây Sơn, mất điện diện rộng 3–7 ngày. Người dân cần một kênh theo dõi mực nước trực quan và nhận cảnh báo sớm.

## Tính năng

- **5 trạm mực nước sông Kôn**: Bình Nghi (Tây Sơn), Văn Phong (An Nhơn), An Hòa (Tuy Phước), Thạnh Hòa (Tuy Phước), Bình Tường (Tây Sơn).
- **Biểu đồ Chart.js** đường mực nước 7 ngày (03/11 – 09/11/2026) cho cả 5 trạm.
- **Ngưỡng cảnh báo cấp 1/2/3** riêng từng trạm, mã màu: vàng (cấp 1), cam (cấp 2), đỏ (cấp 3), xanh (bình thường).
- **Nút "Nhận cảnh báo qua Zalo"** → https://zalo.me/0396241674.
- Trang chủ mô tả bối cảnh lũ sông Kôn 2026, dashboard hoạt động với mock data qua route `/api/stations`, trang About, trang 404 có hotline.
- Giao diện tiếng Việt, responsive (375px và 1440px).

## Công nghệ

- Python 3 + **Flask** (backend, render Jinja2, JSON API)
- **Chart.js 4** (CDN) cho biểu đồ mực nước
- HTML/CSS/JavaScript thuần (frontend)
- Deploy: **Vercel** (`@vercel/python`, rewrite toàn bộ về `api/index.py`)

## Cách chạy local

```bash
py -m venv venv
venv/Scripts/python.exe -m pip install -r requirements.txt
venv/Scripts/python.exe api/index.py
# Mở http://127.0.0.1:5000
```

Kiểm tra import không side-effect:

```bash
venv/Scripts/python.exe -c "import sys; sys.path.insert(0,'api'); import index"
```

## Cấu trúc

```
api/index.py         # Flask app: /, /dashboard, /about, /api/stations, 404 handler
templates/           # base, index, dashboard, about, 404 (Jinja2)
static/css/style.css
static/js/dashboard.js
requirements.txt     # flask
vercel.json          # rewrites → /api/index
```

## Deploy

Link deploy (Vercel production): **https://binhdinh-flood-warning.vercel.app** (xem thêm `deploy_url.txt`).

```bash
vercel --prod --yes
```

## 📞 Liên hệ HTK – 0396241674 – 09/11/2026

- **Hotline/Zalo:** 0396241674 — gọi `tel:0396241674`
- **Zalo:** https://zalo.me/0396241674 (nhận cảnh báo lũ qua Zalo)
- **Email:** htk.contact@gmail.com

© 2026 HTK · Hotline/Zalo: 0396241674 · Email: htk.contact@gmail.com