harorat = (18, 20, 17, 23, 25, 21, 19)

yuqori_haroratlar = [h for h in harorat if h > 20]

print(f"Haroratlar: {', '.join(map(str, yuqori_haroratlar))}")
print(f"Kunlar soni: {len(yuqori_haroratlar)}")