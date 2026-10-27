jami = 0
soni = 0

while True:
    xarajat = float(input())
    if xarajat == 0:
        break
    jami += xarajat
    soni += 1

print(f"Jami: {int(jami)}")
print(f"Kiritilgan xarajatlar soni: {soni}")
if soni > 0:
    ortacha = jami / soni
    print(f"O'rtacha: {ortacha:.2f}")