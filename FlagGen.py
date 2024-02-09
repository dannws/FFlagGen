import os, random, time
import requests as r
import pyfiglet



os.system(f'title dannw on dc ^')



def clear():
    os.system("cls")
    print(
        pyfiglet.figlet_format(
            "                                        FlagGen                                                     "
        )
    )
    print("")
    print("                                                   (MADE by dannw)")
    print("                                                    (im mentally)")
    print("                                                     (unstable!)")
    print("                         ")
    print("                         ")
    print("                         ")
    print("                         ")
    print("                         ")


clear()





headers = {'Accept': 'application/json'}

faglist = r.get("https://raw.githubusercontent.com/dannws/allfaglist/main/ALLFFLAGS.txt", headers=headers)
bleh = faglist.json()
woof = bleh[random.randint(1,8478)]


print(f"ur fflag is: {woof}")

def anotherflag():
    woof = bleh[random.randint(1,8478)]
    print()
    print("Choose Y/N")
    yesorno = input("another flag? ")
    print()
    loweryes = yesorno.lower()
    if loweryes == "y":
        print(f"ur fflag is: {woof}")
    elif loweryes != "y":
        os.system('cls')
        print("ok bye bye i mog you")
        time.sleep(2)
        quit()



while True:
    anotherflag()
    





