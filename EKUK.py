def bulinuvchiga_ajrat(number):
    sonlar = []
    for i in range(2, number+1):
        while number % i == 0 and number != 1:
            sonlar.append(i)
            number /= i
    return sonlar
def bulinuvchilarga_ajrat(numbers):
    bujjlar = []
    for number1 in numbers:
        bujjlar.append(bulinuvchiga_ajrat(number1))
    return bujjlar
def bulinuvchilar_finish(*bulinuvchilar):
        kopaytma = []
        for ruyxat in bulinuvchilar:
            for element in ruyxat:
                for el in element:
                    kopaytma.append([el]*element.count(el))
        return kopaytma
def EKUK_top(*bulinuvchilar):
    bulinuvchilar = list(bulinuvchilar)
    natija = 1
    new_bulinuvchilar = []
    new_new_bulinuvchilar = []
    for bulinuvchi in bulinuvchilar:
        for b in bulinuvchi:
            new_bulinuvchilar.append(b)

    for x in new_bulinuvchilar:
        if x not in new_new_bulinuvchilar: 
            new_new_bulinuvchilar.append(x)
    lugat = {}
    for b in new_new_bulinuvchilar:
        for s in b:
            if s not in lugat:
                lugat[s] = b.count(s)
            elif lugat[s] < b.count(s):
                lugat[s] = b.count(s)
            else:
                continue
    for key, val in lugat.items() :
        natija *= key ** val
    print(new_new_bulinuvchilar, lugat)
    return natija
def calculate_LCM():
    print("""Bu Dastur xohlagancha son qabul qilib ularning EKUK ini yoki "LCM" sini chiqarib beradi!""")
    answer = int(input("1-chi sonni kiriting: "))
    bulinuvchilar_user = []
    sanoq = 1
    while answer != 0:
        bulinuvchilar_user.append(answer)
        sanoq += 1
        answer = int(input(f"""{sanoq}-chi sonni kiriting(agar to'xtatmoqchi bo'lsangiz "0"ni bosing): """))
    bulinuvchilar = bulinuvchilarga_ajrat(bulinuvchilar_user)
    finish = bulinuvchilar_finish(bulinuvchilar)
    return EKUK_top(finish)







print(calculate_LCM())