#1 savarjisho
print("romeli imperiis mier agebuli wyal-momaragebis sistema funqionirebs dgesac?:")
ans=("1. shumerta, 2. selchukta,  3. romis,  4. mongolta")
ans_1=input("enter answer:").lower()

if int(ans_1)==3 or ans_1=="romis":
    print("sworia!")
elif int(ans_1)==1 or int(ans_1)==2  or int(ans_1)==4 or ans_1=="shumerta" or  ans_1=="selchukta" or ans_1=="mongolta":
        print("ara! swori pasuxia romis!")
else:
    print("error")


#2 savarjisho 
choose=input("choose one prodact: laptop, personal computer or phone:").lower()

if choose=="laptop" or choose=="personal computer" or choose=="phone":
    a=int(input("enter max_budget:"))
    if a==5000 and choose=="laptop":
        print("hp, lenovo, asus")
    
    elif a==5000 and choose=="personal computer":
                print("asus, ultra, lenovo ")
    elif a==5000 and choose=="phone":
                print("sumsung, apple, google pixel")
    else:
        print("budget isn't enough")


#3 savarjisho
print("romeo dgas okianestan da unda wavides princesas gadasarchenat koshkisken. koshks rom miagwios aris ori gza. pirveli agmosavletit, sadac mouwevs gaiaros tye, patara mdinare da qvewarmavlebit savse ormo. meore gza ufro moklea, magram mouwevs gadaiaros tovliani mtebi da moklas gveleshapi")
way=input("enter your choose:").lower()
if way=="east":
    equipment=input("choose equipment:sword,Shield, paddles or gun: ").lower()
    if equipment=="paddles":
        print("you can take a sword, go to forest, take across river, kill snakes and will  see a queen")
    elif equipment=="sword" or equipment=="Shield" or equipment=="gun":
            print(" you have one more life and can go to forest")
elif way=="north-east":
    equipment=input("choose equipment:sword,Shield, paddles or gun: ").lower()
    if equipment=="sword":
        print("you can take a Shield, go to mountine, kill dragone and will  see a queen")
    elif equipment=="paddles" or equipment=="Shield" or equipment=="gun":
            print(" you have one more life and can go to forest")
else:
    print(" you cann't choose other way and log out")


#4 savarjisho
ans_1=input("girchevnia amoxsna amocanebi tu wero sheni naazrevi?:").lower()
ans_2=input("romeli girchevnia imushao ofisshi tu saxlidan mushaobas anicheb upiratesobas?:").lower()
ans_3=input("mogwons xalxis daxmareba da mattan komunikacia?:").lower()

if ans_1=="amocanebis amoxsna" and  ans_2=="ofisshi" and ans_3=="ara":
    print("you can learn math, Physics, science ")
    if ans_1=="amocanebis amoxsna" and ans_2=="ofisshi" and ans_3=="ara":
        ans_4=input("marto girchevnia ofisshi yofna tu kolegebtan ertad:")
    elif ans_4=="tanamshromlebtan ertad":
        print("you can learn accounting")
elif ans_1=="wera" and ans_2=="ofisshi" and ans_3=="ki":
    print("you can learn humanities, low ")
    if ans_1=="wera" and ans_2=="ofisshi" or ans_3=="ki":
        ans_4=input("marto girchevnia ofisshi yofna tu kolegebtan ertad:")
        if ans_4=="marto":
            print("you can learn humanities")
        else:
            print("you can learn low")
else:
    print("you have many chooses")

