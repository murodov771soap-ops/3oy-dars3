ruxsat = {"matematika", "ingliz", "informatika", "fizika"}
tanlangan = {"ingliz", "informatika", "tarix"}

ruxsat_etilgan = tanlangan & ruxsat
ruxsat_etilmagan = tanlangan - ruxsat

print(f"Ruxsat etilgan: {', '.join(ruxsat_etilgan)}")
print(f"Ruxsat etilmagan: {', '.join(ruxsat_etilmagan)}")