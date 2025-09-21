'''
### **Đề bài: Dãy Zig-Zag**
Cho một mảng gồm **n** số nguyên phân biệt, nhiệm vụ của bạn là biến đổi mảng này thành một **dãy zig-zag** bằng cách hoán đổi vị trí các phần tử.
Một dãy được gọi là **zig-zag** nếu:
* `k` phần tử đầu tiên tăng dần,
* `k` phần tử cuối cùng giảm dần,
* với `k = (n + 1) / 2`.
---
### **Dữ liệu vào (Input Format)**
* Dòng đầu: số nguyên `t`, là số bộ test.
* Với mỗi bộ test:

  * Dòng đầu: số nguyên `n`, kích thước mảng.
  * Dòng tiếp theo: gồm `n` số nguyên phân biệt `a[1], a[2], …, a[n]`.
---
### **Ràng buộc (Constraints)**
* 1 ≤ t ≤ 20
* 1 ≤ n ≤ 10000 (n là số lẻ)
* 1 ≤ a\[i] ≤ 10⁹
---
### **Dữ liệu ra (Output Format)**
Với mỗi bộ test, in ra mảng đã được biến đổi thành dãy zig-zag.
---
### **Ví dụ Input**

```
1
7
1 2 3 4 5 6 7
```

### **Ví dụ Output**

```
1 2 3 7 6 5 4

 Hiểu đơn giản: Ta cần sắp xếp mảng → đưa số lớn nhất vào giữa → đảo ngược nửa cuối để thành zig-zag.

'''

def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2)
    a[mid - 1], a[n-1] = a[n-1], a[mid - 1]

    st = mid + 2
    ed = n - 1
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed + 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)

