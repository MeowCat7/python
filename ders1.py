import random
sifre=int(input("parola uzunluğu kaçtır?"))
karakterler="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
karakter=random.choice(karakterler)
print(karakter)
for in range(sifre):
