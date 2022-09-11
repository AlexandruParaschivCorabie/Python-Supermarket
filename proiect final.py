import sys
from random import randrange
iesire = 0
iesire_2 = 0
ziua_saptamanii = 0
selectare_client_firma=0
print(50 * "#")
print("Buna ziua! Bine ati venit in supermarket-ul nostru!")
print(50 * "#")
print("Sunt aici sa cumpar in calitate de client sau firma:")
print(" 1. Client")
print(" 2. Firma")

while not iesire:
    selectare_client_firma = int(input('\nAlegeti tipul de cumparator [1-2] : '))
    if (selectare_client_firma == 1):
        print("Bine ati venit!")
        break
    else:
        if (selectare_client_firma == 2):
            print(
                "\nClientii care se incadreaza in persoana juridica primesc discount-ul de 20% la cumparaturi de peste 2.000lei.\nontinuati navigarea in magazin?\n")
            print("1.Da \n2.Nu")
            selectare_da_nu = int(input('\nAlege-ti optiunea[1-2] : '))
            while not iesire_2:
                if selectare_da_nu == 1:
                    break
                elif selectare_da_nu == 2:
                    print("O zi buna!")
                    sys.exit()
                else:
                    selectare_da_nu = int(input('\nAlege-ti optiunea[1-2] : '))
        elif selectare_client_firma != 1 and selectare_client_firma != 2:
            print("\n!Numar gresit de optiune. Introduce-ti un numar valid aflat in lista de optiuni!")
            continue
        iesire = 1
iesire = 0
print(28 * "-")
print(" In ce zi a saptamanii suntem astazi?")
print(28 * "-")
print(" 1. Luni")
print(" 2. Marti")
print(" 3. Miercuri")
print(" 4. Joi")
print(" 5. Vineri")
print(" 6. Sambata")
print(" 7. Duminica")
print(28 * "-")

while not iesire:
    ziua_saptamanii = int(input('Alegeti o zi a saptamanii [1-7] : '))
    if ziua_saptamanii == 1:
        print(" \nLuni se ofera dicount pentru produsele de pe raionul 1")
        ziua_saptamanii = 1
    elif ziua_saptamanii == 2:
        print("\n Marti se ofera dicount pentru produsele de pe raionul 2  ")
        ziua_saptamanii = 2
    elif ziua_saptamanii == 3:
        print("\n Miercuri se ofera dicount pentru produsele de pe raionul 3")
        ziua_saptamanii = 3
    elif ziua_saptamanii == 4:
        print("\n Joi se ofera dicount pentru produsele de pe raionul 4")
        ziua_saptamanii = 4
    elif ziua_saptamanii == 5:
        print("\n Vineri se ofera dicount pentru produsele de pe raionul 5")
        ziua_saptamanii = 5
    elif ziua_saptamanii == 6:
        print("\n Sambata se ofera dicount pentru produsele de pe raionul 6")
        ziua_saptamanii = 6
    elif ziua_saptamanii == 7:
        print("\n Duminica se ofera dicount pentru produsele de pe raionul 7")
        ziua_saptamanii = 7
    else:
        print("\n!Numar gresit de optiune. Introduce-ti un numar valid aflat in lista de optiuni!")
        continue
    iesire = 1
iesire = 0
cantitate = 0
pret = 0
suma_bani = 0
x = 0
y = 0
z = 0

def produs(suma_bani):
    pret, cantitate = int(x), float(y)
    suma_bani = pret * cantitate
    return suma_bani


print("selectati un raion:")
for i in range(1, 4):
    print(i, ".", "Raionul ", i)
print("4.Verificare suma cumparaturi")
print("5.Mergi la casa")

while True:

    selectare_raion = int(input('\nAlegeti raionul [1-3] : '))

    if selectare_raion == 1:
        print("Raionul 1:Fructe si legume")
        print("1.  banane")
        print("2.  mere")
        print("3.  pere")
        print("4.Inapoi")

        selectare_raion_1 = int(input('\nAlegeti din  raionul 1 [1-3] : '))

        if selectare_raion_1 == 1:
            x = 5
            y = int(input('\nNr de kg de banane: '))
            z = (produs(suma_bani)) + z
            if ziua_saptamanii == 1 or ziua_saptamanii == 3:
                z -= 10 / 100 * z
            print("\nSelectati un raion:")
            for i in range(1, 4):
                print(i, ".", "Raionul ", i)
            print("4.Verificare suma cumparaturi")
            print("5.Mergi la casa")
            continue


        elif selectare_raion_1 == 2:
            x = 3
            y = int(input('\nNr de kg de mere: '))
            z = (produs(suma_bani)) + z
            if ziua_saptamanii == 1 or ziua_saptamanii == 3:
                z -= 10 / 100 * z
            print("\nSelectati un raion:")
            for i in range(1, 4):
                print(i, ".", "Raionul ", i)
            print("4.Verificare suma cumparaturi")
            print("5.Mergi la casa")
            continue

        elif selectare_raion_1 == 3:
            x = 4
            y = int(input('\nNr de kg de pere: '))
            z = (produs(suma_bani)) + z
            if ziua_saptamanii == 1 or ziua_saptamanii == 3:
                z -= 10 / 100 * z
            print("\nSelectati un raion:")
            for i in range(1, 4):
                print(i, ".", "Raionul ", i)
            print("4.Verificare suma cumparaturi")
            print("5.Mergi la casa")
            continue

        elif selectare_raion_1 == 4:
            print("\nSelectati un raion:")
            for i in range(1, 4):
                print(i, ".", "Raionul ", i)
            print("4.Verificare suma cumparaturi")
            print("5.Mergi la casa")
            continue

    if selectare_raion == 2:

        print("Raionul 2:Produse animale")

        print("1.  piept de pui")

        print("2.  oua")

        print("3.  carne de vita")

        print("4.Inapoi")

        selectare_raion_2 = int(input('\nAlegeti din  raionul 2 [1-3] : '))

        if selectare_raion_2 == 1:

            x = 5

            y = int(input('\nNr de kg de piept de pui: '))

            z = (produs(suma_bani)) + z

            if ziua_saptamanii == 2 or ziua_saptamanii == 4:
                z -= 10 / 100 * z

            print("\nSelectati un raion:")

            for i in range(1, 4):
                print(i, ".", "Raionul ", i)
            print("4.Verificare suma cumparaturi")
            print("5.Mergi la casa")

            continue



        elif selectare_raion_2 == 2:

            x = 3

            y = int(input('\nNr de oua: '))

            z = (produs(suma_bani)) + z

            if ziua_saptamanii == 2 or ziua_saptamanii == 4:
                z -= 10 / 100 * z

            print("\nSelectati un raion:")

            for i in range(1, 4):
                print(i, ".", "Raionul ", i)
            print("4.Verificare suma cumparaturi")
            print("5.Mergi la casa")

            continue


        elif selectare_raion_2 == 3:

            x = 4

            y = int(input('\nNr de kg de carne de vita: '))

            z = (produs(suma_bani)) + z

            if ziua_saptamanii == 2 or ziua_saptamanii == 4:
                z -= 10 / 100 * z

            print("\nSelectati un raion:")

            for i in range(1, 4):
                print(i, ".", "Raionul ", i)
            print("4.Verificare suma cumparaturi")
            print("5.Mergi la casa")

            continue


        elif selectare_raion_2 == 4:

            print("\nSelectati un raion:")

            for i in range(1, 4):
                print(i, ".", "Raionul ", i)
            print("4.Verificare suma cumparaturi")
            print("5.Mergi la casa")

            continue

    if selectare_raion == 3:

        print("Raionul 3:Produse pentru igiena personala")

        print("1.  sapun")

        print("2.  sampon")

        print("3.  gel de dus")

        print("4.Inapoi")

        selectare_raion_3 = int(input('\nAlegeti din  raionul 2 [1-3] : '))

        if selectare_raion_3 == 1:

            x = 5

            y = int(input('\nNr de bucati sapun: '))

            z = (produs(suma_bani)) + z

            if ziua_saptamanii == 3 or ziua_saptamanii == 5:
                z -= 10 / 100 * z

            print("\nSelectati un raion:")

            for i in range(1, 4):
                print(i, ".", "Raionul ", i)
            print("4.Verificare suma cumparaturi")
            print("5.Mergi la casa")

            continue



        elif selectare_raion_3 == 2:

            x = 3

            y = int(input('\nNr de bucati sampon: '))

            z = (produs(suma_bani)) + z

            if ziua_saptamanii == 3 or ziua_saptamanii == 5:
                z -= 10 / 100 * z

            print("\nSelectati un raion:")

            for i in range(1, 4):
                print(i, ".", "Raionul ", i)
            print("4.Verificare suma cumparaturi")
            print("5.Mergi la casa")

            continue


        elif selectare_raion_3 == 3:

            x = 4

            y = int(input('\nNr de bucati gel de dus: '))

            z = (produs(suma_bani)) + z

            if ziua_saptamanii == 3 or ziua_saptamanii == 5:
                z -= 10 / 100 * z

            print("\nSelectati un raion:")

            for i in range(1, 4):
                print(i, ".", "Raionul ", i)
            print("4.Verificare suma cumparaturi")
            print("5.Mergi la casa")

            continue


        elif selectare_raion_3 == 4:

            print("\nSelectati un raion:")

            for i in range(1, 4):
                print(i, ".", "Raionul ", i)
            print("4.Verificare suma cumparaturi")
            print("5.Mergi la casa")

            continue

    if selectare_raion == 4:

        print("\n1.Verificare suma cumparaturi\n2.Iesire")

        selectare_raion_4 = int(input('\nAlegeti optiunea [1-2] : '))

        if selectare_raion_4 == 1:

            print("Suma cumparaturilor pana acum este de:",z ,"lei fara TVA")
            print("Suma cumparaturilor pana acum este de:", z+ 90/100*z, "lei cu TVA")


            print("\nSelectati un raion:")

            for i in range(1, 4):
                print(i, ".", "Raionul ", i)
            print("4.Verificare suma cumparaturi")
            print("5.Mergi la casa")

            continue



        elif selectare_raion_4 == 2:

            print("\nSelectati un raion:")

            for i in range(1, 4):
                print(i, ".", "Raionul ", i)
            print("4.Verificare suma cumparaturi")
            print("5.Mergi la casa")

            continue

    if selectare_raion == 5:
        print("\nBun venit la casa de marcat!\n")
        print("\n1.Plata cumparaturi\n2.Iesire")

        selectare_raion_5 = int(input('\nAlegeti optiunea [1-2] : '))

        if selectare_raion_5 == 1:

            print("\nSuma cumparaturilor pana acum este de:",z+90/100*z ,"lei cu TVA\nContinuati plata?\n\n1.Da\n2.Nu")
            finalizare_cumparaturi=int(input('Alegeti optiunea [1-2] :'))
            if finalizare_cumparaturi == 1:
                print(50 * "*")
                print("\nBON FISCAL")
                print(50 * "*")
                print("\nNR BON FISCAL:", randrange(220, 844),"\n")
                print(50 * "*")
                if selectare_client_firma == 1:
                    print("TIP CLIENT: PERSOANA FIZICA\n")
                if selectare_client_firma == 2:
                    print("TIP CLIENT: PERSOANA JURIDICA\n")
                if ziua_saptamanii==1:
                    print("Luni")
                elif ziua_saptamanii==2:
                    print("Marti")
                elif ziua_saptamanii==3:
                    print("Miercuri")
                elif ziua_saptamanii==4:
                    print("Joi")
                elif ziua_saptamanii==5:
                    print("Vineri")
                elif ziua_saptamanii==6:
                    print("Sambata")
                elif ziua_saptamanii==7:
                    print("Duminica")
                print(randrange(1,30),".",randrange(1,12),".2022\n")
                print(50 * "*")
                print("\nTRANZACRIE APROBATA\n")
                print(50 * "*")
                if selectare_client_firma==1:
                    print("\nSuma platita:", z, "lei fara TVA")
                    print("Suma platita:", z + 90 / 100 * z, "lei cu TVA\n")
                if selectare_client_firma==2:
                    print("\nSuma platita:", z, "lei fara TVA")
                    print("Suma platita:", z + 90 / 100 * z, "lei cu TVA\n")
                if selectare_client_firma==2 and z>19999:
                    print("\nSuma platita-reducere firma:", z-20/100*z, "lei fara TVA")
                    print("Suma platita-reducere firma:", z-20/100*z + 90 / 100 * z, "lei cu TVA\n")
                print(50 * "*")
                print("\nMultumim pentru ca ati cumparat de la magazinul nostru! O zi buna! \n")
                print(50 * "*")
                break

            print("\nSelectati un raion:")
            for i in range(1, 4):
                print(i, ".", "Raionul ", i)
            print("4.Verificare suma cumparaturi")
            print("5.Mergi la casa")
            continue



        elif selectare_raion_5 == 2:

            print("\nSelectati un raion:")

            for i in range(1, 4):
                print(i, ".", "Raionul ", i)
            print("4.Verificare suma cumparaturi")
            print("5.Mergi la casa")
            continue


    else:
        print("Numar gresit de optiune.")












