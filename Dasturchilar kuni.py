oylar = {
    1 : 30,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30, 
    7 : 31,
    8 : 31,
    9 : 30, 
    10 : 31,
    11 : 30,
    12 : 31
}
yil = int(input("Yilni kiriting: "))
kerak = 255
oy = 0
kun = 0
if yil % 4 == 0:
    oylar[2] = 29
while kerak != 0:
    oy += 1
    if kerak >= 28:
        kerak = kerak - oylar[oy]
    else:
        kun = kerak
        kerak = 0
if kun < 10:
    kun = f"0{kun}"
if oy < 10:
    oy = f"0{oy}"
sana = f"{kun}/{oy}/{yil}"
print(sana)