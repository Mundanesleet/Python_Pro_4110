import random
elements = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_length = int(input("Introduzca la longitud del pase: "))

password = ""
for i in range(pass_length):
    password += random.choice(elements)

print(password)