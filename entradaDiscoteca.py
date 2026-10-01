edat = int(input("Introdueix la teva edat: "))
res = True
res_final = False

if edat >= 18: 
    print("Tens entrada?")
    print(
        "1. Si\n"
        "2. No\n"
        )
    entrada = int(input())
    if entrada == 1:
        print("Portes la roba adecuada?")
        print(
            "1. Si\n"
            "2. No\n"
            )
        roba = int(input())
        if roba == 1:
            res_final = True
            print("Pots entrar\n")
        else:
            res = False
    else:
        res = False
else:
    res = False

if res == False:
    print("No pots entrar\n")

    


