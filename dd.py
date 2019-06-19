def velocity(s, t):
    if t == "0":
        print("Man kan nte dividera med noll")
    else:
        print(s/t)
    
def segment(v, t):
    print(v*t)
    
def time(s, v):


    print(s/v)

print("Välj vad du vill räkna ut av valen nedan")
print("1. Hastighet")
print("2. Tid")
print("3. Sträcka")

val = int(input("Skriv 1,2 eller 3"))
if val == 1:
    val11 = int(input("Skriv sträcka"))
    val12 = int(input("Skriv tid"))
    velocity(val11, val12)

if val == 2:
    val21 = int(input("Skriv hastighet"))
    val22 = int(input("Skriv tid"))
    segment(val21, val22)

if val == 3:
    val31 = int(input("Skriv hastighet"))
    val32 = int(input("Skriv sträcka"))
    time(val31, val32)

