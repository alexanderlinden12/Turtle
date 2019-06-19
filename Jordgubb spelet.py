print("Välkommen till vårt spel ät jordgubbarna!\n")
print("Ät jordgubbar, men var försiktig!\n")
print("Under spelets gång kommer du att mötas av många jordgubbar men all är inte goda")
print("--------------------------------------")
print("Skriv JA om du vill äta en jordgubbe och nej om du inte vill det")
print("Vissa jordgubbar kommer att kunna ge dig hp och vissa kommer att ta bort din hp, maximalt med hp är 100.")

z = True
hp = 100
if hp > 0:
    z = False
list1 =  []

print("Du ligger ute i skogen och tittar upp mot molnen och känner dig lite hungrig\n")
print("Du börjar därför dagens jakt efter jordgubbar.")
print("Lite längre fram i skogen så hittar du en jordgubbe på marken")
jordgubbe = str(input("Vill du ta den här jordgubben?"))
if jordgubbe.lower() == "ja":
    list1.append("Jordgubbe")
    print("Det här är vad du nu har i din packning")
    for i in range(len(list1)):
        print(list1[i])
    hp = hp-5
    print("Eftersom att du inte har ätit på så länge så har du", hp,"hp kvar")
    hp = hp+5
    print("Du smaskar därför i dig din goda jordgubbe och din hp är nu", hp)
    print("Efter din långa efter jordgubbar så är du trött och måste ta en liten tupplur")
    print("Du sätter på dig din solhatt och somnar in")

else:
    print("NU SÅ HAR DU INGEN JORDGUBBE(Dumt val)")
    print("Det här är vad du har plockat upp under den här rundan")
    list1.append("Inget")
    for i in range(len(list1)):
        print(list1[i])
    list1.remove("Inget")
    hp = hp-5
    print("Eftersom att du inte har ätit på så länge så har du", hp,"hp kvar")
    print("Så hungrig och trött som du är så måste du gå och lägga dig då du har en lång dag framför dig")
    hp = hp-10
    print("Nu är hela skogen mörk och du känner hur magen kurrar du måste gör allt för att hitta en jordgubbe din hp är nu",hp)
    print("Bakom dig så hör du ett ljud av jorgubbar som äts och framför dig så kan du se ett litet ljus från en stuga")
    val_1 = str(input("Skriv bak om du vill utförska ljudet eller fram om du vill utforska stugan"))
    if val_1.lower() == "bak":
        print("Du går försiktigt fram mot ljudet")
        print("Där framme så kan du se en gammal tant med en ful korg av jordgubbar som ser lite skumma ut")
        val_2 = str(input("Vill du ha en jorgubbe?, frågar tanten"))
    if val_2.lower () == "ja":
        print("Du stiger fram till tanten och räcker fram handen där du får en grön jordgubbe")
        print("Du stoppar in den i munnen och känner magen kurra och du börjar må dåligt")
        print("Den onda jorgubben gör så att du förlorar 90 hp nu har du -5 hp")
        print("DU HAR FÖRLORAT SPELET!")
        hp = hp-90
    if            
                 

