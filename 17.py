ombor = {"olma": 12, "banan": 8, "anor": 15, "uzum": 6}

max_mahsulot = max(ombor, key=ombor.get)
min_mahsulot = min(ombor, key=ombor.get)
jami = sum(ombor.values())

print(f"Eng ko'p: {max_mahsulot} ({ombor[max_mahsulot]} ta)")
print(f"Eng kam: {min_mahsulot} ({ombor[min_mahsulot]} ta)")
print(f"Jami mahsulot: {jami} ta")