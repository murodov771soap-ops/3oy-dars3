birinchi = {"Ali", "Madina", "Jasur", "Aziza"}
ikkinchi = {"Jasur", "Sardor", "Aziza", "Bekzod"}

faqat_1 = birinchi - ikkinchi
faqat_2 = ikkinchi - birinchi
ikkalasida = birinchi & ikkinchi

print(f"Faqat birinchi: {', '.join(faqat_1)}")
print(f"Faqat ikkinchi: {', '.join(faqat_2)}")
print(f"Ikkalasida: {', '.join(ikkalasida)}")