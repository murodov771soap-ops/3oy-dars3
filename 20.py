ovozlar = {
    "Ali": "Python",
    "Vali": "JavaScript",
    "Madina": "Python",
    "Jasur": "C++",
    "Aziza": "Python",
    "Sardor": "JavaScript"
}

natija = {}
for til in ovozlar.values():
    natija[til] = natija.get(til, 0) + 1

for til, son in natija.items():
    print(f"{til}: {son} ta ovoz")

golib = max(natija, key=natija.get)
print(f"G'olib: {golib}")