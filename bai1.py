ten = str(input("Nhập tên: "))
n = int(input("số kí tự trong tên:"))
print("tên")
khoangcach = ""
for i in range(1, n+1):
    khoangcach = khoangcach + "{" +  str(i) + ":" + str(i*i) + "}" + ","
print(khoangcach)