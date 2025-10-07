import random
import time
import torch

# List of deities and non-deities
dud_dieties = ["Zeus","Hera","Poseidon","Demeter","Athena", "Apollo","Artemis","Ares","Aphrodite","Hephaestus", "Hermes","Hestia","Allah","Buddha","Vishnu", "Shiva","Odin","Thor","Loki","Ra"]
dud_dieties_lower = ["zeus", "hera", "poseidon", "demeter", "athena", "apollo", "artemis", "ares", "aphrodite", "hephaestus", "hermes", "hestia", "allah", "buddha", "vishnu", "shiva", "odin", "thor", "loki", "ra"]

deities = [ "Jesus", "Jesus Christ", "God","Yahweh"]
deities_lower = ["jesus", "jesus christ", "god", "yahweh"]

no_diety = ["None", "none", "none of them", "None of the above", "None Of Them", "None Of Them Are!", "None of them are real Gods", "none of them are real gods", "none of them are Real Gods", 
            "None of them are deities", "none of them are real", "None of them are real", "none of them are deities", "None of them are real deities", "none of them are real deities",
            "They're all fake", "none of the above", "No diety", "no diety", "No Diety", "no Diety", "None of Them", "none of Them", "None of them", "none of them", "No gods", "no gods",
                "No god", "no god",
    "No deity", "no deity", "No Deity", "no Deity",
    "Nope", "nope", "Nah", "nah", "none are real",
    "All fake", "all fake",
    "None are real", "none are real",
    "They’re all fake", "they are all fake", "theyre all fake",
    "Fake", "fake",
    "Not real", "not real",
    "Myth", "myth", "Myths", "myths",
    "All myths", "all myths",
    "They're Fiction", "They're All Fiction", "they're fiction", "they're all fiction",
    "Imaginary", "imaginary",
    "Doesn’t exist", "does not exist", "dont exist", "don't exist",
    "Made up", "made-up", "madeup",
    "All lies", "all lies",
    "Nothing", "nothing", "none of them are", "none of them are real", "none of them are real deities", "none of them are real gods", "None of them are real", "None of them are real deities", "None of them are real gods", 
    "None of them are real deities or gods", "None of them are real deities or gods", "None of them are real Gods", "None of them are Gods"]
all_dieties = dud_dieties + deities

def ok_diety():
    while True:
        try:     
            def super_groan():
                groan = input("That's not even an option, man. Try 'yes' or 'no': ")                
                if groan.lower() == "yes":
                    print("Alright, let's try again:")
                    return
                elif groan.lower() == "no":
                    print("Ok. Thanks for playing (quitter...)")
                    time.sleep(3)
                    exit()
                elif groan.lower() == "24633642":
                    print("K I L L C O D E  A C T I V A T E D : pr0gR@M  $HuTTtInG do0Wn . . ... . .....☠️")
                    time.sleep(3)
                    exit()
                else:
                    if "yes" not in groan:
                        super_groan()


            def bye():
                cool = input("Correct, You guessed a real diety!✝️ Do you want to play again? (yes/no): ")
                if cool.lower() == "yes":
                    print("Great! Less Go:")
                    return
                elif cool.lower() == "no":
                    print("Aight, Thanks for playing man.")
                    time.sleep(3)
                    exit()
                elif cool.lower() == "24633642":
                    print("K I L L C O D E  A C T I V A T E D : pr0gR@M  $HuTTtInG do0Wn . . ... . .....☠️")
                    time.sleep(3)
                    exit()
                else:
                    super_groan()

            
            def shrimp():
                pop = input("Correct, all of those gay chumps are fake my nigga🥳 Do you want to play again? (yes/no): ")
                if pop.lower() == "yes":
                    print("Great! Less Go:")
                    return
                elif pop.lower() == "no":
                    print("Aight, Thanks for playing man.")
                    time
                    exit()
                elif pop.lower() == "24633642":
                    print("K I L L C O D E  A C T I V A T E D : pr0gR@M  $HuTTtInG do0Wn . . ... . .....☠️")
                    time.sleep(3)
                    exit()
                else:
                    super_groan()

            
            #same as bye. but for the users who want to leave after getting a wrong answer
            def quitter():
                hat = input("INC❌RR❌CT: Not a real diety👎 Do you want to try again? (yes/no): ")
                if hat.lower() == "yes":
                    print("Cool. Let's go then.")
                    return
                elif hat.lower() == "no":
                    print("Ok. Thanks for playing (Secular kid)")
                    time
                    exit()
                elif hat.lower() == "24633642":
                    print("K I L L C O D E  A C T I V A T E D : pr0gR@M  $HuTTtInG do0Wn . . ... . .....☠️")
                    time.sleep(3)
                    exit()
                else:
                    super_groan()

            
            def steak():
                sus = input("❌ There WAS a real diety👎 Do you want to try again? (yes/no): ")
                if sus.lower() == "yes":
                    print("Cool. Let's go then.")
                    return
                elif sus.lower() == "no":
                    print("Ok. Thanks for playing (Secular kid)")
                    time.sleep(3)
                    exit()
                elif sus.lower() == "24633642":
                    print("K I L L C O D E  A C T I V A T E D : pr0gR@M  $HuTTtInG do0Wn . . ... . .....☠️")
                    time.sleep(3)
                    exit()
                else:
                    super_groan()


            selected_deities = random.sample(all_dieties, 3)
            guess = input(f"Which is diety? (choose from {selected_deities}): ")
            has_diety = any(d in selected_deities for d in deities)

            if guess not in selected_deities and guess not in no_diety and guess.lower() != "24633642" and guess not in deities and guess not in deities_lower:
                whatever_man=input("That's not even an option. Want to Try again? (yes/no): ")
                if whatever_man == "yes":
                    print("Cool, Let's go then:")
                    return
                elif whatever_man.lower() == "no":
                    print("Ok. Thanks for playing (mostly anyway).")
                    time.sleep(3)
                    exit()
                else:
                    super_groan()

            # if it has a diety, these are the ways things can play out
            elif has_diety:
                if guess in deities:
                    bye()
                elif guess in deities_lower:
                    bye()
                elif guess in dud_dieties:
                    quitter()
                elif guess in no_diety:
                    steak()
                elif guess.lower() == "24633642":
                    print("K I L L C O D E  A C T I V A T E D : pr0gR@M  $HuTTtInG do0Wn . . ... . .....☠️")
                    time.sleep(3)
                    exit()
            elif selected_deities != has_diety:
                if guess in selected_deities:
                    quitter()
                elif guess in no_diety:
                    shrimp()
                elif guess in deities:
                    bye()
                elif guess in deities_lower:
                    bye()
                elif guess.lower() == "24633642":
                    print("K I L L C O D E  A C T I V A T E D : pr0gR@M  $HuTTtInG do0Wn . . ... . .....☠️")
                    time.sleep(3)
                    exit()
        except ValueError:
                print("ValueError Caught:")
                super_groan()

    
ok_diety()
