import random
import os

karakter = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&"
kata_sandi = ""

for i in range(5):
    kata_sandi+= random.choice(karakter)
    os.system('cls')
print("pw:", kata_sandi)