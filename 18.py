shaharlar = {"Toshkent": 3000000, "Farg'ona": 300000, "Samarqand": 600000}

kop_shaharlar = [shahar for shahar, aholi in shaharlar.items() if aholi > 500000]
eng_kop = max(shaharlar, key=shaharlar.get)

print(f"500 000 dan ko'p: {', '.join(kop_shaharlar)}")
print(f"Eng ko'p aholi: {eng_kop}")