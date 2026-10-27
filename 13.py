ali = {"komediya", "sarguzasht", "fantastika"}
vali = {"fantastika", "drama", "komediya"}

umumiy = ali & vali
faqat_bittasiga = ali ^ vali

print(f"Umumiy janrlar: {', '.join(umumiy)}")
print(f"Faqat bittasiga yoqadi: {', '.join(faqat_bittasiga)}")