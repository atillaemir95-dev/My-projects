from datetime import date
dogum_yili = int(input("Birth Year? "))
dogum_ayi = int(input("Birth Month? "))
dogum_günü = int(input("Birthday? "))
dogum_tarihi = date(dogum_yili,dogum_ayi,dogum_günü)
bugun = date.today()

yas = bugun.year - dogum_tarihi.year

# doğum günü daha gelmediyse -1 yapar
if (bugun.month, bugun.day) < (dogum_tarihi.month, dogum_tarihi.day):
    yas = yas - 1
print("Your age :", yas)