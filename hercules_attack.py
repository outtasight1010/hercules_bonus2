import random

def get_user_attack():
    user_attack = input("Which attack mode would you like to use against your enemy? 1 or 2: ")
    while user_attack!= "1" and user_attack !="2":
        print("Oops, you must choose 1 or 2.")
        user_attack = input("Which attack mode would you like to use against your enemy? 1 or 2: ")
    else:
        if user_attack=="1":
            print("You have chosen Bone crush attack!")
        elif user_attack=="2":
            print("You have chosen Boulder attack!")
        
    return user_attack

















#list of each characteristics

hero_dictionary = {"name:Hercules","health meter:20","attack power:20",
                  "attack names:Bone crush attack,Boulder attack"}
enemy1_dictionary = {"name:Nemean Lion","health meter:20","attack power:20",
                    "attack names:Bite attack","Breath attack"}
enemy2_dictionary = {"name:Lernaean Hydra","health metter:20","attack power:20",
                    "attack names:Gaze attack, Touch attack"}
enemy3_dictionary = {"name:Cerberus","health meter:20","attack power:20",
                     "attack names:Mind attack,Fear attack"}






#open welcome greeting 
print("")
print("Hi there, and welcome to the 'Ring of Power'!")
print("")
print("This is where YOU call the shots, and get to destroy your enemies however you please!")
print("Oh yeah, and by the way, you will be HERCULES:Master of the Universe!")
print("")

print("Pretty cool, right? Ok then, let's get started!")

#define 3 potential enemies/threats
print("")
print("Let's introduce your enemies:")
print("")
print("1.Nemean Lion  2.Lernaean Hydra and 3.Cerberus the Dog")
print("")








# defined user attack function above
#called user attack function below
get_user_attack()



        

user_enemy = input("Now, it's time to choose your enemy. Choose 1, 2, or 3: ")
while user_enemy!= "1" and user_enemy!= "2" and user_enemy!="3":
    print("Wrong again! Please choose 1, 2 or 3. ")
    user_enemy = input("Now, it's time to choose your enemy. Choose 1, 2, or 3: ")
else:
    if user_enemy == "1":
        print("You have summoned Nemean Lion!")
    elif user_enemy == "2":
        print("Lernaean Hydra is on his way!")
    elif user_enemy == "3":
        print("Here comes Cerberus!")

    








    
    





    

