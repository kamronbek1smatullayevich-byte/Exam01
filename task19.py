matn = input("Matn kiriting: ")

soni = 0

for harf in matn:
    if harf == "a" or harf == "e" or harf == "i" or harf == "o" or harf == "u":
        soni = soni + 1

print(soni)