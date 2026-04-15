[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=23574054&assignment_repo_type=AssignmentRepo)
# Day 10 Lab: Data Pipeline & Data Observability

**Student Email:** 26ai.quanmv@vinuni.edu.vn
**Name:** Mai Văn Quân
**ID:** 2A202600475

---

## Mo ta

Bài lab này tập trung vào việc xây dựng một đường ống dữ liệu (ETL pipeline) tự động bằng Python và thư viện Pandas. Mục tiêu là trích xuất dữ liệu từ file JSON, kiểm tra và làm sạch (loại bỏ các bản ghi lỗi, giá trị âm), biến đổi dữ liệu (tính toán giá giảm, chuẩn hóa văn bản) và tải vào file CSV. Sau khi hoàn thiện ETL, bài lab thực hiện mô phỏng (Agent Simulation) để minh chứng tầm quan trọng của chất lượng dữ liệu: so sánh cách một AI Agent ra quyết định khi được cung cấp dữ liệu sạch (Clean Data) so với dữ liệu bị nhiễm bẩn (Garbage Data).

---

## Cach chay (How to Run)

### Prerequisites
```bash
pip install pandas
```

### Chay ETL Pipeline
```bash
python solution.py
```

### Chay Agent Simulation (Stress Test)
```bash
# Mo ta cach ban chay thi nghiem Clean vs Garbage data
```

---

## Cau truc thu muc

```
├── solution.py              # ETL Pipeline script
├── processed_data.csv       # Output cua pipeline
├── experiment_report.md     # Bao cao thi nghiem
└── README.md                # File nay
```

---

## Ket qua

- **Tổng số records đầu vào:** 5 records (đọc từ file `raw_data.json`).
- **Số records bị loại (chứa lỗi):** 2 records (không vượt qua khâu Validate).
- **Số records hợp lệ (đã xử lý):** 3 records.
- **Đầu ra:** Pipeline chạy thành công, biến đổi và lưu 3 records sạch vào file `processed_data.csv`.
