list2d = []
x = int(input("Baris:"))
y = int(input("Kolom:"))
for i in range(x):
    temp = []
    for j in range(y):
        temp.append(int(input()))
    list2d.append(temp)
print(list2d)