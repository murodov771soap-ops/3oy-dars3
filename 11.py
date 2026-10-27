matematika = {"Ali", "Vali", "Madina", "Jasur", "Aziza"}
ingliz = {"Madina", "Jasur", "Sardor", "Aziza", "Malika"}

ikkalasida = matematika & ingliz
faqat_bittasida = matematika ^ ingliz

print(f"Ikkala kursda: {', '.join(sorted(ikkalasida))}")
print(f"Faqat bitta kursda: {', '.join(sorted(faqat_bittasida))}")