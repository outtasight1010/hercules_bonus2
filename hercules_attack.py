import random


#open welcome greeting 
#created function for greeting
def get_greeting():
    print("")
    print("Hi there, and welcome to the 'Ring of Power'!")
    print("")
    print("This is where YOU call the shots, and get to destroy your enemies however you please!")
    print("Oh yeah, and by the way, you will be HERCULES:Master of the Universe!")
    print("")
    print("Pretty cool, right? Ok then, let's get started!")
#define the 3 potential enemies/threats within greeting
    print("")
    print("Let's introduce your enemies:")
    print("")
    print("1.Nemean Lion  2.Lernaean Hydra and 3.Cerberus the Dog")
    print("")



#created function to ask user for mode of attack preference 
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

#created function for user enemy choice
def get_enemy_choice():

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
    
    return user_enemy
#created an attack function
#now user is ready to GO
def attack():

    game_on = input("Are you ready to attack? Please type Y for Yes, or type N for no: ")
    while game_on!= "Y" and game_on!= "N":
        print("TRY AGAIN. You must enter Y or N to proceed!")
        game_on = input("Are you ready to attack? Please type Y for Yes, or type N for no: ")
    else:
        if game_on == "N":
            print("Agh bummer, you have been hit!!")
            game_on = input("Are you ready to attack? Please type Y for Yes, or type N for no: ")
        elif game_on == "Y":
            print("ATTACK succeeded!")
            game_on = input("Are you ready to attack? Please type Y for Yes, or type N for no: ")
        
    
    return game_on



#dictionary list of each character (hero, enemies)

hero_dictionary = {"name":"Hercules","health meter":20,"attack power":20}
                  
enemy1_dictionary = {"name":"Nemean Lion","health meter":20,"attack power":20}
                    
enemy2_dictionary = {"name":"Lernaean Hydra","health meter":20,"attack power":20}
                    
enemy3_dictionary = {"name":"Cerberus","health meter":20,"attack power":20}
                     
enemy_attack_list = ["Fire attack", "Mind attack", "Bite attack", "Laser attack"]







#called greeting function:
get_greeting()


#called user attack function:
get_user_attack()


#called user enemy choice function:
get_enemy_choice()

import random
print("Your enemy's attack method/name will now be chosen randomly.")
print("")
random_attack = random.choice(enemy_attack_list)
print("Enemy attack method will be:", random_attack)
print("")
print(f'Be aware of your beginning health capacity, which is at:{20}')
print("")

#called attack function:
attack()


















              
      







    








    
    





    

