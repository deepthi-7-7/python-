import random

name=input("Please enter your name: ")
print("\n")
print("Hey ",name, "! Welcome to the zombie apocalypse!\n")
print("You are a survivor trying to reach a safe zone.")
print("Along the way, you must make tough decisions about who to trust and how to stay alive.")
print("\n")


location = ["hospital","supermarket","police station"]
health = 100
supplies = ["bandages", "food"]
weapons = ["knife"]

choose=input("Choose a number to know your location [1,2,3]: ")

random.shuffle(location)

num=dict(zip(range(1, 4), location))

location= num[int(choose)]

while True:
    print("\nCurrent location: " +location)
    print("Health: " + str(health))
    print("Supplies: " + str(supplies))
    print("Weapons: " + str(weapons))

    print("\n")

    if location=="hospital":
        # Encounter random event
        print("Now you gotten into a hospital. Let's see what will u encounter next\n")

        encounter = ["zombie", "hostile survivor", "supply cache","bandits"]

        choice=input("Choose one number to check which place you encountered[1,2,3,4]: ")
        random.shuffle(encounter)

        en=dict(zip(range(1,5),encounter))

        encounter=en[int(choice)]

        print("\nYou encounter a " + encounter + "!")

        if encounter == "zombie":
            # Fight the zombie
            print("You must fight the zombie!")
            if "knife" in weapons:
                print("You use your knife to defeat the zombie!")
                weapons.remove("knife")

                print("\nCurrent location: " +location)
                print("Health: " + str(health))
                print("Supplies: " + str(supplies))
                print("Weapons: " + str(weapons))
                print("\n")


            else:
                print("You don't have any weapons to fight the zombie!")
                health -= 25
                supplies.remove("bandages")

                print("\nCurrent location: " +location)
                print("Health: " + str(health))
                print("Supplies: " + str(supplies))
                print("Weapons: " + str(weapons))
                print("\n")


        elif encounter == "hostile survivor":
            # Decide whether to fight or flee
           
            decision = input("Do you want to fight or flee? ")
            if decision == "fight" and "knife" in weapons:
                print("You use your knife to defeat the hostile survivor!")
                weapons.remove("knife")

                print("\nCurrent location: " +location)
                print("Health: " + str(health))
                print("Supplies: " + str(supplies))
                print("Weapons: " + str(weapons))
                print("\n")

            else:
                print("You either don't have a knife or decide to flee!")
                location = random.choice(["hospital", "supermarket", "police station"])
                print("\nCurrent location: " +location)
                print("Health: " + str(health))
                print("Supplies: " + str(supplies))
                print("Weapons: " + str(weapons))
                print("\n")

        elif encounter == "supply cache":
            # Find supplies and weapons
            print("You find a supply cache! and filled your bag.")
            supplies += ["bandages", "food"]
            weapons += ["bat"]

            print("\nCurrent location: " +location)
            print("Health: " + str(health))
            print("Supplies: " + str(supplies))
            print("Weapons: " + str(weapons))
            print("\n")

        elif encounter == "bandits":
            # Fight the zombie
            print("You must fight the bandits!")
            if "bat" in weapons:
                print("You use your bat to defeat the bandits!")
                weapons.remove("bat")

                print("\nCurrent location: " +location)
                print("Health: " + str(health))
                print("Supplies: " + str(supplies))
                print("Weapons: " + str(weapons))
                print("\n")

            else:
                print("You don't have any weapons to fight the bandits!")
                supplies.remove("food","bandages")

                print("\nCurrent location: " +location)
                print("Health: " + str(health))
                print("Supplies: " + str(supplies))
                print("Weapons: " + str(weapons))
                print("\n")

    elif location=="supermarket":
        print("Now you gotten into a supermarket. Let's see what will u encounter next\n")
        # Encounter random event

        encounter = ["zombie", "hostile survivor", "supply cache","bandits"]
        
        choice=input("Choose one number to check which place you encountered[1,2,3,4]: ")
        random.shuffle(encounter)

        en=dict(zip(range(1,5),encounter))

        encounter=en[int(choice)]


        print("\nYou encounter a " + encounter + "!")

        if encounter == "zombie":
            # Fight the zombie
            print("You must fight the zombie!")
            if "knife" in weapons:
                print("You use your knife to defeat the zombie!")
                weapons.remove("knife")

                print("\nCurrent location: " +location)
                print("Health: " + str(health))
                print("Supplies: " + str(supplies))
                print("Weapons: " + str(weapons))
                print("\n")

            else:
                print("You don't have any weapons to fight the zombie!")
                health -= 25
                supplies.remove("bandages")

                print("\nCurrent location: " +location)
                print("Health: " + str(health))
                print("Supplies: " + str(supplies))
                print("Weapons: " + str(weapons))
                print("\n")

        elif encounter == "hostile survivor":
            # Decide whether to fight or flee
            
            decision = input("Do you want to fight or flee? ")
            if decision == "fight" and "knife" in weapons:
                print("You use your knife to defeat the hostile survivor!")
                weapons.remove("knife")

                print("\nCurrent location: " +location)
                print("Health: " + str(health))
                print("Supplies: " + str(supplies))
                print("Weapons: " + str(weapons))
                print("\n")

            else:
                print("You either don't have a knife or decide to flee!")
                location = random.choice(["hospital", "supermarket", "police station"])

                print("\nCurrent location: " +location)
                print("Health: " + str(health))
                print("Supplies: " + str(supplies))
                print("Weapons: " + str(weapons))
                print("\n")


        elif encounter == "supply cache":
            # Find supplies and weapons
            print("You find a supply cache! and filled your bag.")
            supplies += ["bandages", "food"]
            weapons += ["bat"]

            print("\nCurrent location: " +location)
            print("Health: " + str(health))
            print("Supplies: " + str(supplies))
            print("Weapons: " + str(weapons))
            print("\n")
        
        elif encounter == "bandits":
            # Fight the zombie
            print("You must fight the bandits!")
            if "bat" in weapons:
                print("You use your bat to defeat the bandits!")
                weapons.remove("bat")

                print("\nCurrent location: " +location)
                print("Health: " + str(health))
                print("Supplies: " + str(supplies))
                print("Weapons: " + str(weapons))
                print("\n")

            else:
                print("You don't have any weapons to fight the bandits!")
                supplies.remove("food","bandages")

                print("\nCurrent location: " +location)
                print("Health: " + str(health))
                print("Supplies: " + str(supplies))
                print("Weapons: " + str(weapons))
                print("\n")


    elif location=="police station":
        print("Now you gotten into a police station. Let's see what will u encounter next\n")
        # Encounter random event


        encounter = ["zombie", "hostile survivor", "supply cache","bandits"]
        
        choice=input("Choose one number to check which place you encountered[1,2,3,4]: ")
        random.shuffle(encounter)

        en=dict(zip(range(1,5),encounter))

        encounter=en[int(choice)]


        print("\nYou encounter a " + encounter + "!")

        if encounter == "zombie":
            # Fight the zombie
            print("You must fight the zombie!")
            if "knife" in weapons:
                print("You use your knife to defeat the zombie!")
                weapons.remove("knife")

                print("\nCurrent location: " +location)
                print("Health: " + str(health))
                print("Supplies: " + str(supplies))
                print("Weapons: " + str(weapons))
                print("\n")

            else:
                print("You don't have any weapons to fight the zombie!")
                health -= 25
                supplies.remove("bandages")

                print("\nCurrent location: " +location)
                print("Health: " + str(health))
                print("Supplies: " + str(supplies))
                print("Weapons: " + str(weapons))
                print("\n")


        elif encounter == "hostile survivor":
            # Decide whether to fight or flee
            
            decision = input("Do you want to fight or flee? ")
            if decision == "fight" and "knife" in weapons:
                print("You use your knife to defeat the hostile survivor!")
                weapons.remove("knife")

                print("\nCurrent location: " +location)
                print("Health: " + str(health))
                print("Supplies: " + str(supplies))
                print("Weapons: " + str(weapons))
                print("\n")

            else:
                print("You either don't have a knife or decide to flee!")
                location = random.choice(["hospital", "supermarket", "police station"])

                print("\nCurrent location: " +location)
                print("Health: " + str(health))
                print("Supplies: " + str(supplies))
                print("Weapons: " + str(weapons))
                print("\n")

        elif encounter == "supply cache":
            # Find supplies and weapons
            print("You find a supply cache! and filled your bag.")
            supplies += ["bandages", "food"]
            weapons += ["bat"]

            print("\nCurrent location: " +location)
            print("Health: " + str(health))
            print("Supplies: " + str(supplies))
            print("Weapons: " + str(weapons))
            print("\n")

        elif encounter == "bandits":
            # Fight the zombie
            print("You must fight the bandits!")
            if "bat" in weapons:
                print("You use your bat to defeat the bandits!")
                weapons.remove("bat")

                print("\nCurrent location: " +location)
                print("Health: " + str(health))
                print("Supplies: " + str(supplies))
                print("Weapons: " + str(weapons))
                print("\n")

            else:
                print("You don't have any weapons to fight the bandits!")
                supplies.remove("food","bandages")

                print("\nCurrent location: " +location)
                print("Health: " + str(health))
                print("Supplies: " + str(supplies))
                print("Weapons: " + str(weapons))
                print("\n")

    # Decide whether to move to a new location

    if location == "safe haven":
        print("\nCongratulations, you have reached the safe haven and survived the zombie apocalypse!")
        break

    decision = input("Do you want to stay or move to a new location? ").lower()
    if decision == "move":
        if location == "hospital":
            location = random.choice(["supermarket", "police station", "safe haven"])
        elif location == "supermarket":
            location = random.choice(["hospital", "police station", "safe haven"])
        elif location == "police station":
            location = random.choice(["hospital", "supermarket", "safe haven"])


    # Check if player has lost the game
    if health <= 0:
        print("\nYou have died and the zombie apocalypse continues...")
        break


