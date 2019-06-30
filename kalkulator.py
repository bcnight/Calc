## membuat kalkulator

def tambah(num1, num2):
    return num1 + num2

def kurang(num1, num2):
    return num1 - num2

def kali(num1, num2):
    return num1 * num2

def bagi(num1, num2):
    return num1 / num2

def mod(num1, num2):
    return num1 % num2


print()
print("++++++++++++++++++++++++++++++++++++")
print("+++++++ K A L K U L A T O R ++++++++")
print("++++++++++++++++++++++++++++++++++++")
print()
print("1. Penjumalahan ")
print("2. Pengurangan  ")
print("3. Perkalian    ")
print("4. Pembagian    ")
print("5. Modulus      ")
print()
print("++++++++++++++++++++++++++++++++++++")
print()

pilihan = str(input("Pilihan: [1/2/3/4/5] > "))

num1 = int(input("Masukkan bilangan pertama > "))
num2 = int(input("Masukkan bilangan kedua > "))

if pilihan is "1":
    print(num1,"+",num2,"=", tambah(num1, num2))

elif pilihan is "2":
    print(num1,"-",num2,"=", kurang(num1, num2))

elif pilihan is "3":
    print(num1,"x",num2,"=", kali(num1, num2))

elif pilihan is "4":
    print(num1,"/",num2,"=", bagi(num1, num2))

elif pilihan is "5":
    print(num1,"%",num2,"=", mod(num1, num2))

else:
    print("inputan salah")
# if inputan_dari_user is '1':
#     tambah()

# elif inputan_dari_user is '2':
#     kurang()

# elif inputan_dari_user is '3':
#     kali()

# elif inputan_dari_user is '4':
#     bagi()

