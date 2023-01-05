def calculate_LCM():
    print("""Bu Dastur xohlagancha son qabul qilib ularning EKUB ini yoki "HCF" sini chiqarib beradi!""")
    answer = int(input("1-chi sonni kiriting: "))
    bulinuvchilar_user = []
    sanoq = 1
    while answer != 0:
        bulinuvchilar_user.append(answer)
        sanoq += 1
        answer = int(input(f"""{sanoq}-chi sonni kiriting(agar to'xtatmoqchi bo'lsangiz "0"ni bosing): """))
    EKUB = 1
    while True:
        for i in range(2, min(bulinuvchilar_user)):
            sanoq = 0
            for a in bulinuvchilar_user:
                if a % i == 0:
                    sanoq += 1
                if sanoq == len(bulinuvchilar_user):
                    EKUB = i
                
        break            
    return EKUB
print(calculate_LCM())