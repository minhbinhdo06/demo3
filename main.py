# Khởi tạo biến tổng và danh sách lưu số
total = 0
numbers = []

print("Nhập 10 số tự nhiên (không âm):")

for i in range(10):
    while True:
        try:
            # Nhập số và kiểm tra tính hợp lệ
            num = float(input(f"Số thứ {i+1}: "))
            if num >= 0:
                total += num
                numbers.append(num)
                break  # Thoát vòng lặp nếu số hợp lệ
            else:
                print("⚠️ Vui lòng nhập số tự nhiên (không âm)!")
        except ValueError:
            print("⚠️ Đầu vào không hợp lệ. Vui lòng nhập một số!")

# In kết quả
print("\n----------------------------------")
print(f"Danh sách số đã nhập: {numbers}")
print(f"Tổng của 10 số: {total}")
print("Nhưng mà mình không biết cách tính trung bình cộng 😅")