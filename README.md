# Prompting Techniques

Tìm hiểu và thử nghiệm các kỹ thuật Prompting trên các mô hình ngôn ngữ lớn phổ biến như GPT, Claude, Grok... để giải quyết các bài toán cụ thể.

# Cài đặt các thư viện cần thiết
```
pip install langchain langchain-openai
pip install python-dotenv
```

# Các roles cơ bản trong 1 cuộc hội thoại

|Role|Mô tả|
|---|---|
|system|Đưa ra hướng dẫn tổng thể, thiết lập bối cảnh cho mô hình AI|
|user|Đại diện cho người dùng, gửi yêu cầu hoặc câu hỏi tới mô hình|
|assistant|Phản hồi từ mô hình AI dựa trên các prompt và bối cảnh đã thiết lập|


# Giải thích 1 số tham số
## model
* Xác định tên hoặc loại mô hình sẽ sử dụng, ví dụ: "gpt-3.5-turbo", "gpt-4o".
* Mỗi model có khả năng, tốc độ và chi phí khác nhau.

## temperature
* Điều chỉnh mức độ ngẫu nhiên (randomness) trong câu trả lời. 
* Giá trị từ 0 đến 2 (thường dùng 0–1). 
  * Thấp (0–0.3): Trả lời chắc chắn, nhất quán, ít sáng tạo (phù hợp với dịch thuật, chuẩn hóa, phân loại). 
  * Cao (0.7–1): Trả lời đa dạng, sáng tạo hơn, đôi khi có thể "bịa" thông tin. 
* Ví dụ:
  * temperature=0: "Paris is the capital of France." (luôn trả lời giống nhau)
  * temperature=1: "Paris is France’s capital, a city known for romance and the Eiffel Tower." (câu trả lời đa dạng hơn)

## max_tokens
* Số lượng tối đa token (từ, dấu câu, ký tự) mà model sẽ sinh ra trong một lần trả lời.
* Giới hạn này giúp kiểm soát độ dài và chi phí của phản hồi. 
* Ví dụ:
  * max_tokens=50: Trả lời ngắn gọn.
  * max_tokens=500: Cho phép trả lời dài, chi tiết.

## top_p (nucleus sampling)
* Điều chỉnh phạm vi lựa chọn từ tiếp theo dựa trên xác suất cộng dồn.
* Giá trị từ 0 đến 1:
  * Thấp (0.1–0.3): Chỉ chọn từ trong nhóm xác suất cao nhất, câu trả lời nhất quán, ít sáng tạo. 
  * Cao (0.7–1): Cho phép chọn cả những từ ít phổ biến hơn, tăng sự đa dạng. 
* Thường chỉ nên điều chỉnh một trong hai: temperature hoặc top_p, không nên thay đổi cả hai cùng lúc.

## frequency_penalty
* Phạt khi model lặp lại từ hoặc cụm từ đã dùng nhiều lần. 
* Giá trị từ -2.0 đến 2.0
* Cao: Giảm lặp lại, khuyến khích sự đa dạng.

## presence_penalty
* Khuyến khích model đưa ra chủ đề mới, tránh lặp lại ý cũ. 
* Giá trị từ -2.0 đến 2.0
