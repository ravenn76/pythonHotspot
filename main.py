from dep.module_import import *
from dep.file_import import *

def show_menu():
    '''
    Print the menu with the option
    '''

    #print(art("Pythonspot"))
    
    print("\t1 - Run\n",
          "\t2 - Config"
          )
    
    uchoice = int(input("Choose a option : "))
    return uchoice


def main():
    uchoice = show_menu()

    if uchoice == 1:
        run()

    elif uchoice == 2:
        config()
        
    else :
        print("Unknow option")

main()
