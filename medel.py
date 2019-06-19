from statistics import *


siffror = [23,45,45,76,34,98]

def medel(siffror):
    print(mean(siffror))


b = True

while b:
    print(siffror)
    print("vad vill du göra?")
    print("1. Medelvärde")
    print("2. Lägg till fler siffror")
    print("3. Avsluta programmet")
    print("4. Ta bort siffra")
    val = input("Välj ett alternativ")

    if val == "1":
        medel(siffror)

    elif val == "2":
        siffra = int(input("Hur många siffror vill du lägga till"))
        for i in range(siffra):
            siffra1 = int(input("Skriv siffran du vill lägga till"))
            siffror.append(siffra)
         
                    

    elif val == "3":
        print("Hej då")
        b = False
    elif val == "4":
        siffra_1 = int(input("Skriv hur många siffror du vill ta bort"))
        for i in range(siffra_1):
            siffror = int(input("Skriv den siffran som du vill ta bort"))
            siffror.remove(siffra)
    
