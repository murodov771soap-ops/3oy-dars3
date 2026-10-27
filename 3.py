ombor = 12

while ombor > 0:
    sotildi = int(input("Sotildi: "))
    if sotildi <= ombor:
        ombor -= sotildi
        print(f"Qoldi: {ombor}")
    else:
        print("Omborda bunday miqdorda daftar yo'q!")

print("Ombor bo'sh")