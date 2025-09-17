'''Bài 22: Viết chương trình liệt kê, đếm và tính tổng các ước số của số nguyên dương
n (n nhập từ bàn phím).
Nhap n: 1966 
Cac uoc so: 1 2 983 1966
Co 4 uoc so, tong la: 2952'''
import math

n = int(input("nhập vào 1 số nguyên: "))
arr = []
sum = 0
for i in range(1,int(math.sqrt(n)+1)):
    if(n % i == 0):
        arr.append(i)
        sum += i
        if n // i != i:
            arr.append(n // i)
            sum += (n // i)
arr.sort()
for i in arr:
    print(i, end=" ")
print()
print(sum)
