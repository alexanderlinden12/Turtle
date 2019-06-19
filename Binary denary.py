def binary_converter(val_2):
    binary = val_2
    denary = 0
    for digit in binary:
        denary = denary * 2 + int(digit)
    print("Your denary number is: " + str(denary))

def denery_convert(val_3):
    denary = val_3
    binary = ""
    while denary>0:
        binary = str(denary%2) + binary
        denary = denary//2
    print("Your binary numer is: " + binary)

print("Vad vill du göra?")
print("1.Binary - Denary")
print("2.Denary - Binary")

val_1 = int(input("Välj antingen 1 eller 2: "))
if val_1 == 1:
            val_2 = input("Skriv in vilket binärt tal du vill översätta")
            binary_converter(val_2)
elif val_1 == 2:
            val_3 = int(input("Skriv in vilket decimalt tal du vill översätta"))
            denery_convert(val_3)
            
