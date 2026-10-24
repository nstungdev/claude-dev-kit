---
project: <tên dự án>
updated: <YYYY-MM-DD>
---

# Domain: <tên dự án>

<Một đoạn ngắn: hệ thống làm gì, cho ai, các khối nghiệp vụ chính.>

## Thuật ngữ

<Thuật ngữ business và tên tương ứng trong code. Dùng để soát trục
"Đặt tên": code phải dùng đúng tên ở cột "Tên trong code", không dùng
các tên ở cột "Tránh dùng".>

| Thuật ngữ | Nghĩa | Tên trong code | Tránh dùng |
|---|---|---|---|
| <Ví (Wallet)> | <tài khoản giữ số dư của khách> | `Wallet` | `Account`, `Balance` |

## Bất biến business

<Những điều phải luôn đúng, dù dữ liệu đi qua luồng nào. Mỗi bất biến
một ID dạng INV-NN. Vi phạm bất biến là P0.>

### INV-01: <phát biểu ngắn, ví dụ: Số dư ví không bao giờ âm>

- **Chi tiết:** <điều kiện, đơn vị, cách làm tròn, ngoại lệ hợp lệ nếu có>
- **Đảm bảo ở đâu:** <`src/.../WalletService.cs`, constraint DB, validator...>
- **Nguồn:** <coder xác nhận ngày YYYY-MM-DD / ticket ABC-123 / tài liệu>

## Luồng nhạy cảm

<Các module mà thay đổi trong đó cần phỏng vấn kỹ hơn và soát business,
bảo mật chặt hơn: tiền, phân quyền, xóa dữ liệu, migration, tích hợp ngoài.>

- <Thanh toán> · `src/Api/Payments/**` · <vì sao nhạy cảm>

## Ngoại lệ

<Trường hợp team đã chấp nhận, không báo khi review. Chỉ thêm khi coder
đồng ý. Mỗi dòng: INV ID hoặc thuật ngữ · phạm vi · lý do · ngày thêm.>
