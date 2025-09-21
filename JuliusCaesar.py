'''vMật mã Caesar là gì?
Mật mã Caesar là một trong những phương pháp mã hóa đơn giản và cổ xưa nhất, được đặt theo tên của Julius Caesar.
Nguyên lý của nó là dịch chuyển mỗi chữ cái trong văn bản gốc đi một số vị trí cố định (số k) trong bảng chữ cái. Khi dịch chuyển, nếu vượt quá cuối bảng chữ cái (chữ 'z'), nó sẽ quay lại từ đầu (chữ 'a').

Ví dụ: Nếu k = 3, chữ 'a' sẽ trở thành 'd', 'b' thành 'e', và cứ thế. Chữ 'x' sẽ trở thành 'a', 'y' thành 'b', và 'z' thành 'c'.

2. Các tham số trong đề bài
s (string): Đây là chuỗi văn bản gốc cần mã hóa (cleartext). Chuỗi này chỉ chứa các ký tự ASCII hợp lệ và không có khoảng trắng.

k (int): Đây là số nguyên biểu thị số vị trí dịch chuyển. Giá trị của k nằm trong khoảng từ 0 đến 100.
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z              '''

n = int(input("nhập vào độ dài của chuỗi: "))
sr = input("nhập vào mật mã: ")
if (len(sr) > n):
    sr = sr[:n]
k = int(input("nhập vào k: "))

for i in sr:
    if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
        if i.islower():
            print(chr((ord(i) - ord('a') + k) % 26 + ord('a')), end="")
             
        else:
            print(chr((ord(i) - ord('A') + k) % 26 + ord('A'))  , end="")
    else:
        print(i ,end="")
        
        

