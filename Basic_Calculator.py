number = int(input("Birinci sayıyı gir: "))
number2 = int(input("İkinci sayıyı gir: "))
symbol = input("İşlemi seç (+, -, *, /,%,**): ")
if symbol == "+":
    sonuc = number + number2
elif symbol == "-":
    sonuc = number - number2
elif symbol == "*":
    sonuc = number * number2
elif symbol == "/":
    sonuc = number / number2
elif symbol == "%":
    sonuc = (number * number2) / 100
elif symbol == "**":
    sonuc = number ** number2

else:
    sonuc = "Geçersiz İşlem"

print("Sonuç", sonuc)

