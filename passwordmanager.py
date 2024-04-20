import random
pasw = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
yulie = int (input("Inserisci lunghezza password 10"))
password = ""
for i in range(yulie):
    password += random.choice(pasw)
print(password)
