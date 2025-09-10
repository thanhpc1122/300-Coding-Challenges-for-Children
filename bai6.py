# Viết chương trình nhập vào ba số nguyên. Hãy in ba số này ra màn hình theo
# thứ tự tăng dần và chỉ dùng tối đa một biến phụ.
# Nhap a, b, c: 5 3 4
# Tang dan: 3 4 5

def swap(a,b):
    temp = b
    b = a
    a = temp
    return a,b

print("nhập a,b,c")
a,b,c = map(int,input().split())

if a > b:
    a,b = swap(a,b)
if a > c:
    a,c = swap(a,c)
if b > c:
    b,c = swap(b,c)
print(a,b,c)