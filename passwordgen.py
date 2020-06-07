#Lachlan Lawrence - Outcome 2 Python Password Generator
import sys
import os

end = False
menu = 0

#Defines Colors
class color:
   PURPLE = '\033[1;35;48m'
   CYAN = '\033[1;36;48m'
   BOLD = '\033[1;37;48m'
   BLUE = '\033[1;34;48m'
   GREEN = '\033[1;32;48m'
   YELLOW = '\033[1;33;48m'
   RED = '\033[1;31;48m'
   BLACK = '\033[1;30;48m'
   UNDERLINE = '\033[4;37;48m'
   END = '\033[1;37;0m'

while not end:
    #Main Menu (Select Options)
    if menu == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(color.PURPLE)
        print("██████╗░░█████╗░░██████╗░██████╗░░░░░░░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░")
        print("██╔══██╗██╔══██╗██╔════╝██╔════╝░░░░░░██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗")
        print("██████╔╝███████║╚█████╗░╚█████╗░█████╗██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝")
        print("██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗╚════╝██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗")
        print("██║░░░░░██║░░██║██████╔╝██████╔╝░░░░░░╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║")
        print("╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░░░░░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝")        
        print(color.BLUE +'{:^80s}'.format("Made by Papa.Snags"))
        print('{:^80s}'.format("Discord: Papa.Snags#1555"))
        print('{:^80s}'.format("Website: papa-snags.com"))
        print('{:^80s}'.format("Twitter: @PapaSnags"))
        print("")
        print(color.GREEN + "1. 8-Character's Long Password (Weak)" )
        print("2. 16-Character's Long Password (Strong)" )
        print("3. 25-Character's Long Password (Very Strong)")
        print("4. Exit" + color.END + color.RED)
        #Option Select
        opt = input( "Please Select an Option (1-3): " + color.END)
        #Changes Menu 
        if opt == "1":
            menu = 1
        if opt == "2":
            menu = 2
        if opt == "3":
            menu = 3
        if opt == "4":
            menu = 4

    #Menu 1 (8 Length)
    if menu == 1:
        #Header
        os.system('cls' if os.name == 'nt' else 'clear')
        print(color.PURPLE + "8-Character Long Password" + color.END)
        from random import *
        #Sets Password character list
        lists = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
        #Selects Random characters from list
        password =  "".join(choice(lists) for x in range(8))
        #Prints Password
        print("Password:", password)
        print(color.GREEN + "1. Main Menu")
        print(color.GREEN + "2. Regenerate")
        print(color.GREEN + "3. Exit" + color.END + color.RED)
        opt = input("Please Select an Option (1-3): " + color.END)
        if opt == "1":
            menu = 0
        if opt == "2":
            menu = 1
        if opt == "3":
            menu = 4

    #Menu 2 (16 Length)
    if menu == 2:
        #Header
        os.system('cls' if os.name == 'nt' else 'clear')
        print(color.PURPLE + "16-Character Long Password" + color.END)
        from random import *
        #Sets Password character list
        lists = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
        #Selects Random characters from list
        password =  "".join(choice(lists) for x in range(16))
        #Prints Password
        print("Password:", password)
        print(color.GREEN + "1. Main Menu")
        print(color.GREEN + "2. Regenerate")
        print(color.GREEN + "3. Exit" + color.END + color.RED)
        opt = input("Please Select an Option (1-3): " + color.END)
        if opt == "1":
            menu = 0
        if opt == "2":
            menu = 2
        if opt == "3":
            menu = 4

    #Menu 3 (25 Length)
    if menu == 3:
        #Header
        os.system('cls' if os.name == 'nt' else 'clear')
        print(color.PURPLE + "25-Character Long Password" + color.END)
        from random import *
        #Sets Password character list
        lists = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
        #Selects Random characters from list
        password =  "".join(choice(lists) for x in range(25))
        #Prints Password
        print("Password:", password)
        print(color.GREEN + "1. Main Menu")
        print(color.GREEN + "2. Regenerate")
        print(color.GREEN + "3. Exit" + color.END + color.RED)
        opt = input("Please Select an Option (1-3): " + color.END)
        if opt == "1":
            menu = 0
        if opt == "2":
            menu = 3
        if opt == "3":
            menu = 4

    #Menu 4 (Exits Program)
    if menu == 4:
        #End Program / Resets Text Clears
        os.system('cls' if os.name == 'nt' else 'clear')
        exit()