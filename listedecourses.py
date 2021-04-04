import json
import os

MENU = ["1: Ajouter un élément à la liste","2: Retirer un élément de la liste","3: Afficher la liste","4: Vider la liste","5: Quitter"]
CHOICES = ["1","2","3","4","5"]
filename = "courses.json"
file_path = f"{os.path.dirname(__file__)}/{filename}"

#print(type(CUR_DIR))

def printmenu():
    for instruction in MENU:
        print(instruction)
    print("-"*20)

def separator():
    print("*"*20)

#checks if the json file exist. If not then create it
#retrieves the list if not empty
def getList():
    courses = []
    if not os.path.exists(file_path):
        with open(filename,"w") as f:
            json.dump(courses,f)
    else:
        with open(filename,"r") as f:
            courses = json.load(f)
    return courses
courses = getList()

while True:
    printmenu()
    choix = input("Votre choix : ")
    if choix not in CHOICES:
        printmenu()
    if choix == "5":
        with open(filename,"w") as f :
            json.dump(courses,f)
        exit()
    elif choix == "1":
        #adds the new data to the list
        new_data = input("Entrer le nouvel élément : ")
        courses.append(new_data)
        separator()
    elif choix == "2":
        to_remove = input("Entrer l'élément à effacer : ")
        courses.remove(to_remove)
        separator()
    elif choix == "3":
        print("Contenu de la liste : ")
        print(courses)
        separator()
    elif choix == "4":
        courses.clear()