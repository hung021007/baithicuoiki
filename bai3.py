name = input("Nhập Họ và tên : ")
so = input("Nhập một số : ")
dao_nguoc = so[::-1]
print(name)
if so == dao_nguoc:
    print(so, " là số nghịch đảo!")
else:
    print(so, " không phải là số nghịch đảo")