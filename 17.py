baholar = {"Ali": 85, "Vali": 72, "Madina": 96, "Jasur": 68}

yuqori = [f"{ism} - {bal}" for ism, bal in baholar.items() if bal >= 90]
ortacha = sum(baholar.values()) / len(baholar)

print(f"Yuqori ball olganlar: {', '.join(yuqori)}")
print(f"O'rtacha ball: {ortacha}")