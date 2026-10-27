A = (3, 7)
B = (8, 2)

a_yigindi = sum(A)
b_yigindi = sum(B)

print(f"A yig'indisi: {a_yigindi}")
print(f"B yig'indisi: {b_yigindi}")

if a_yigindi > b_yigindi:
    print("A yig'indisi katta")
elif b_yigindi > a_yigindi:
    print("B yig'indisi katta")
else:
    print("Yig'indilar teng")