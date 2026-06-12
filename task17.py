ball = int(input("Ball: "))
if ball >= 90 and ball <= 100:
    print("Bahosi: A")
elif ball >= 80 and ball <= 89:
    print("Bahosi: B")
elif ball >= 70 and ball <= 79:
    print("Bahosi: C")
elif ball >= 60 and ball <= 69:
    print("Bahosi: D")  
elif ball >= 0 and ball <= 59:
    print("Bahosi: F")
else:
    print("Ball 0 dan 100 gacha bo‘lishi kerak.")