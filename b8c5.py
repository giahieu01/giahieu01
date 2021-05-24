def Sequential_Search(arr, n, x):
    for i in range(n):
        if (arr[i] == x):
            return i
    return -1

arr=[]
n =int(input('Co bao nhieu item: '))
for k in range(n):
    item=input('Nhap item: ')
    arr.append(item)
x =input('Nhap vao item can tim: ')
n= len(arr)
result = Sequential_Search(arr, n, x)
if (result == -1):
    print("Phan tu khong co trong mang")
else:
    print("Phan tu co trong mang", 'va co vi tri:',result)