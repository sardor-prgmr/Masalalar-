def katak():
    k1 = input("Turgan katakni kiriting: ")
    k2 = input("Borishi kerak bo'lgan katakni kiriting: ")
    return k1, k2
def harfdan_songa(kataklar):
    katak1 = kataklar[0]
    katak2 = kataklar[1]
    harfdan_songa = {"a": 1,
    "b" : 2,
    "c" : 3,
    "d" : 4,
    "e" : 5,
    "f" : 6,
    "g" : 7,
    "h" : 8}
    a_tuliq = []
    b_tuliq = []
    for harf in katak1:
        a_tuliq.append(harf)
    for harf in katak2:
        b_tuliq.append(harf)
    x1 = a_tuliq[0]
    y1 = int(a_tuliq[1])
    x2 = b_tuliq[0]
    y2 = int(b_tuliq[1])
    if x1 in harfdan_songa.keys() and x2 in harfdan_songa.keys():
        if (y1 > 8 or y1 < 1) and (y2 > 8 or y2 < 1):
            x1, x2 = f"{katak1} - katak mavjud emas!", f"{katak2} - katak mavjud emas!"
            print(x1, x2)
            return x1, x2
        elif y1 > 8 or y1 < 1:
            x1 = f"{katak1} - katak mavjud emas!"
            print(x1)
            return x1
        elif y2 > 8 or y2 < 1:
            x2 = f"{katak2} - katak mavjud emas!"
            print(x2)
            return x2
        elif (y2 <= 8 and y2 >= 1) and (y1 <=8 and y1 <= 1):
            x1 = harfdan_songa[x1]
            x2 = harfdan_songa[x2]
            return x1, y1, x2, y2
    elif x1 not in harfdan_songa.keys() and x2 not in harfdan_songa.keys():
        x1, x2 = f"{katak1} - katak mavjud emas!", f"{katak2} - katak mavjud emas!"
        print(x1, x2)
        return x1, x2
    elif x1.lower() not in harfdan_songa.keys() or x2.lower() not in harfdan_songa.keys():
        if x2.lower() not in harfdan_songa.keys():
            if y1 > 8 or y1 < 1:
                x1 = f"{katak1} - katak mavjud emas!"
                print(x1)
            x2 = f"{katak2} - katak mavjud emas!"
            print(x2)
            return x2, x1
        elif x1.lower() not in harfdan_songa.keys():
            if y2 > 8 or y2 < 1:
                x2 = f"{katak2} - katak mavjud emas!"
                print(x2)
            x1 = f"{katak1} - katak mavjud emas!"
            print(x1)
            return x1, x2
def xatomi(list):
    list1 = list[:]
    if len(list) != 4:
        while True:
            print("Iltimos qayta urinib kuring!")
            list1 = harfdan_songa(katak())
            if len(list1) == 4:
                print(list1)
                break
    return list1
def yurishlar_soni(list):
    x1 = list[0]
    y1 = list[1]
    x2 = list[2]
    y2 = list[3]
    xod = 0
    while x1 != x2 or y1 != y2:
        if abs(x1-x2) >= 2:
            if x1 > x2:
                x1 -= 2
            else:
                x1 += 2
        elif abs(x1-x2) == 1:
            if x1 > x2:
                x1 -= 1
            else:
                x1 += 1 
        if abs(y1-y2) >= 2:
            if y1 > y2:
                y1 -= 2
            else:
                y1 += 2
        elif abs(y1-y2) == 1:
            if y1 > y2:
                y1 -= 1
            else:
                y1 += 1  
        xod += 1
    return xod
print(yurishlar_soni(xatomi(harfdan_songa(katak()))))