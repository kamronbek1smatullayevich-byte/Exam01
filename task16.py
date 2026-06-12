age = int(input("Yoshingiz: "))

if age < 7:
    result = f"Yakuniy narx: 50_000 so'm, 50% chegirma"
    print(result)
elif age > 7 and age < 17:
    result = f"Yakuniy narx: 80_000 so'm, 20% chegirma" 
    print(result)
elif age > 60:
    result = f"Yakuniy narx: 70_000 so'm, 30% chegirma"   
    print(result)
        