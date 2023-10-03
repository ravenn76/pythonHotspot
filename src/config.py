import dep.module_import
import os

def get_parameter():
    parameters = os.listdir("config")
    parameter = {}
    for nbr,idx in enumerate(parameters):

        parameter[nbr+1] = f"{idx.replace('.config','')}"
    return parameter

def edit_parameter(parameter):
    print("Current value :",open(parameter).read())
    is_modified = input("Change the file (Y/n) ? : ")
    if is_modified == "Y":
        with open(parameter,'w+') as file:
            file.write(input("New value : "))

def config():
    print("Welcome to the config editor which parameter would you like to change ?\n"+"="*71+"\n")
    dic = get_parameter()
    for idx in dic:
        print("\t" + str(idx) + " - " + dic[idx] + "\n")

    uchoice = int(input("Enter paramater ID : "))
    file = f"config/{dic[uchoice]}.config"
    if os.path.isfile(file) == True:
        edit_parameter(file)
    else :
        print("The paramater doesn't exists")

