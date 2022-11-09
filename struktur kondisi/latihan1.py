# menerima input yang diketik dan penyimpannya didalam variable
bilangansatu = input("masukan bilangan pertama : ")
bilangankedua = input("masukan bilangan kedua : ")

# mengkonversi input string ke integer karena method input() selalu mengembalikan type data string
bilangansatu = int(bilangansatu)
bilangankedua = int(bilangankedua)

# mengecek untuk menentukan bilangan terbesar dari kedua bilangan
if bilangansatu > bilangankedua:
    print("bilangan ", bilangansatu, "lebih besar dari bilangan", bilangankedua)
else:
    print("bilangan ", bilangankedua, "lebih besar dari bilangan", bilangansatu)
    