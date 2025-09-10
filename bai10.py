'''Bài 10: Số bảo hiểm xã hội của Canada (SIN - Canadian Social Insurance Number)
là một số có 9 chữ số, được kiểm tra tính hợp lệ như sau:
- Số phải nhất (vị trí là 1, tính từ phải sang), là số kiểm tra (check digit).
- Trọng số được tính từ phải qua trái (không tính check digit), bằng s1 + s2:
+ s1 là tổng các số có vị trí lẻ.
+ Các số có vị trí chẵn nhân đôi. Nếu kết quả nhân đôi có hai chữ số thì kết quả là
tổng của hai chữ số này. s2 là tổng các kết quả.
SIN hợp lệ có tổng trọng số với số kiểm tra chia hết cho 10.
Ví dụ: SIN 193456787
- Số kiểm tra là 7 (màu xanh tô đậm).
- Trọng số là tổng của s1 và s2, với:
+ s1 = 1 + 3 + 5 + 7 = 16
+ Các số có vị trí chẵn nhân đôi: (9 * 2) (4 * 2) (6 * 2) (8 * 2)  18 8 12 16
s2 = (1 + 8) + 8 + (1 + 2) + (1 + 6) = 27
Trọng số bằng s1 + s2 = 16 + 27 = 43.
Vì tổng trọng số với số kiểm tra 43 + 7 = 50 chia hết cho 10 nên số SIN hợp lệ.
Viết chương trình nhập một số SIN. Kiểm tra xem số SIN đó có hợp lệ hay không.
Nhập 0 để thoát.'''

def sum_of_digits(str):
    return int(str[0]) + int(str[1])
user_input = "99"

while user_input != '0':
    oldChars = 0
    evenChars = 0
    user_input = input("nhấn 0 để thoát: ")
    if user_input != '0':
        last_index = int(user_input[len(user_input)- 1])
        for i in range(0,len(user_input) -1 , 2):
            oldChars += int(user_input[i])
        for y in range(1,len(user_input)-1,2):
            if (int(user_input[y]) * 2 >= 10):
                evenChars += sum_of_digits(str(int(user_input[y]) * 2))
                # print(f"vòng lặp Y các số đc + là {sum_of_digits(str(int(user_input[y]) * 2))} ")
            else:
                evenChars += int(user_input[y]) * 2
                # print(f"vòng lặp Y các số đc + là {int(user_input[y]) * 2} ")
        sum = oldChars + evenChars + last_index
        if(sum % 10 == 0):
            print("hợp lệ")
        else:
            print("ko hợp lệ")



    