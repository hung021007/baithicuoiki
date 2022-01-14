tendem = str(input("Nhập tên đệm và tên: "))
n = int(input("Nhập số kí tự của chữ cái trong tên: "))
def Tongsokitu(n):
    s = 0
    while n > 0:
        s = s + n % 10
        n = int(n / 10)
    return s
print("Tổng các chữ số của", n, "là", Tongsokitu(n))