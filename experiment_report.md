# Experiment Report: Data Quality Impact on AI Agent

**Student ID:** AI20K-2A202600475
**Name:** Mai Văn Quân
**Date:** 15-04-2026

---

## 1. Ket qua thi nghiem

Chay `agent_simulation.py` voi 2 bo du lieu va ghi lai ket qua:

| Scenario | Agent Response | Accuracy (1-10) | Notes |
|----------|----------------|-----------------|-------|
| Clean Data (`processed_data.csv`) | Based on my data, the best choice is Laptop at $1200. | 9 | Gợi ý logic, phù hợp với mặt hàng điện tử tiêu dùng thông thường. |
| Garbage Data (`garbage_data.csv`) | Based on my data, the best choice is Nuclear Reactor at $999999. | 1 | Gợi ý hoàn toàn phi lý, AI bị đánh lừa bởi dữ liệu rác (outlier/poisoned data).|

---

## 2. Phan tich & nhan xet

### Tai sao Agent tra loi sai khi dung Garbage Data?

Khi AI Agent phải đưa ra quyết định dựa trên một tập dữ liệu bị nhiễm bẩn (Garbage Data), toàn bộ bối cảnh logic của nó bị phá vỡ. Các bản ghi "độc hại" (poisoned records) thường chứa các vấn đề nghiêm trọng như giá trị ngoại lai cực lớn (outliers - ví dụ: giá $999999), sai lệch ngữ nghĩa (Nuclear Reactor nằm trong danh sách mua sắm), hoặc các giá trị Null/Duplicate không được xử lý. 

Agent hoạt động dựa trên cơ chế tìm kiếm, tính toán trọng số và tổng hợp thông tin từ ngữ cảnh được cung cấp. Nếu đầu vào không đi qua một ETL pipeline chuẩn mực để lọc rác (validation/cleansing), Agent sẽ mù quáng coi những dữ liệu lỗi đó là "sự thật" (facts). Hậu quả là nó sẽ tối ưu hóa hoặc đề xuất dựa trên các thông số ảo này, dẫn đến những quyết định sai lệch, thiếu an toàn và không thể sử dụng được trong các môi trường AI thực chiến. Điều này chứng minh Data Observability là lớp phòng thủ đầu tiên và quan trọng nhất.

---

## 3. Ket luan

**Quality Data > Quality Prompt?** (Dong y hay khong? Giai thich ngan gon.)

Đồng ý. Nguyên lý "Garbage In, Garbage Out" (GIGO) luôn đúng với mọi hệ thống AI. Một prompt (câu lệnh) dù xuất sắc, chi tiết và tối ưu đến đâu cũng không thể bù đắp được việc cung cấp một tập dữ liệu đầu vào chứa toàn thông tin sai lệch. Trong các ứng dụng thực chiến, nền tảng dữ liệu sạch, đáng tin cậy (Clean Data) mới là yếu tố quyết định giới hạn trần về độ thông minh và tính chính xác của mô hình.
