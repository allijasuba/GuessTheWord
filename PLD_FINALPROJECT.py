import random
import time

level_1 = ["mulan", "frozen", "starwars", "avengers"]
level_2 = ["calculus", "science", "history", "programming", "physics", "arts", "statistics", "chemistry"]
level_3 = ["astronaut", "architect", "geologist", "psychiatrist", "artist", "actor",
           "botanist", "secretary", "chemist", "biologist", "athlete", "professor"]

all_levels = [level_1, level_2, level_3]


print("                         WHAT'S THE WORD!!!")
time.sleep(3)
print("""        Instructions: The Players have 5 chances to guess the 
        correct words on each levels. Each words have their specific 
        Topic and Description to help the players guess the word. 
        If the players finds difficulties in solving the missing word, 
        they can ask for ‘Help’ and a clue will be given to players. 
        If the user guessed it right, the player can proceed to the next 
        level of the game. If not, the game is over.\n\n\n""")
time.sleep(10)

name = input("Enter your name:\n")
print("Hi", name)


def nxt_lvl():
    i = 3
    while i != 0:
        print(i)
        i -= 1
        time.sleep(1)


def loop():
    lvl_num = 0
    while lvl_num != 3:
        word = str.lower(random.choice(all_levels[lvl_num]))
        lvl_num += 1

        def desc():
            if word in level_1:
                if word == level_1[0]:
                    print("""Description:\tA girl disguises as a male warrior and joins the imperial 
army in order to prevent her sick father from being forced 
to enlist as he has no male heir""")
                elif word == level_1[1]:
                    print("Description:\t OST: Let it Go ")
                elif word == level_1[2]:
                    print("Description:\tFrom a Galaxy far far away")
                elif word == level_1[3]:
                    print("Description:\tGroup of superheroes who fights the evil Loki")
            if word in level_2:
                if word == level_2[0]:
                    print("Description:\tproperties of derivatives and integral function.")
                if word == level_2[1]:
                    print("Description:\tapplication of knowledge and understanding based on evidence")
                if word == level_2[2]:
                    print("Description:\tstudy of the past")
                if word == level_2[3]:
                    print("Description:\tactivity of writing computer programs")
                if word == level_2[4]:
                    print("Description:\tdeals with properties of matter and energy")
                if word == level_2[5]:
                    print("Description:\tapplication of human creative skill")
                if word == level_2[6]:
                    print("Description:\tcollecting and analyzing numerical data")
                if word == level_2[7]:
                    print("Description:\tdeals with properties, composition, and structure of substances")
            if word in level_3:
                if word == level_3[0]:
                    print("""Description:\tperson trained, equipped, and deployed by a human 
spaceflight program to command, pilot, or serve 
as a crew member of a spacecraft.""")
                if word == level_3[1]:
                    print("Description:\tis a person who plans, designs and oversees the construction of buildings. ")
                if word == level_3[2]:
                    print("""Description:\tscientist who studies the solid, liquid, and gaseous 
matter that constitutes the Earth and other terrestrial 
planets, as well as the processes that shape them. """)
                if word == level_3[3]:
                    print("""Description:\ta medical doctor (an M.D. or D.O.) who specializes 
in mental health, including substance use disorders. """)
                if word == level_3[4]:
                    print("Description:\tperformer, such as a singer, actor, or dancer.")
                if word == level_3[5]:
                    print("Description:\tprofession is acting on the stage, in movies, or on television.")
                if word == level_3[6]:
                    print("""Description:\tscientist who specializes in plant biology, and is 
an expert on varieties of vegetation including, algae, 
grass, cacti, flowers, moss, trees, shrubs and edibles, 
including herbs, fruits and vegetables. """)
                if word == level_3[7]:
                    print("""Description:\tperson employed by an individual or in an office to 
                    assist with correspondence, keep records, make 
                    appointments, and carry out similar tasks.""")
                if word == level_3[8]:
                    print("Description:\texpert in chemistry; a person engaged in chemical research or experiments.")
                if word == level_3[9]:
                    print("""Description:\tprofessional who has specialized knowledge in the 
field of biology, understanding the underlying mechanisms 
that govern the functioning of biological systems within 
fields such as health, technology and the environment. """)
                if word == level_3[10]:
                    print("Description:\tperson who is proficient in sports and other forms of physical exercise.")
                if word == level_3[11]:
                    print("Description:\tteacher of the highest rank in a college or university.")

        def clue():
            if word in level_1:
                if word == level_1[0]:
                    print("Clue:\tHas a pet Dragon")
                elif word == level_1[1]:
                    print("Clue:\tAnna and Elsa")
                elif word == level_1[2]:
                    print("Clue:\tLuke, I am your Father!")
                elif word == level_1[3]:
                    print("Clue:\tthey are consist of Iron Man, Captain America and others")
            if word in level_2:
                if word == level_2[0]:
                    print("Clue:\tlimits")
                if word == level_2[1]:
                    print("Clue:\tknowledge")
                if word == level_2[2]:
                    print("Clue:\tknowledge acquired by investigation")
                if word == level_2[3]:
                    print("Clue:\tPython")
                if word == level_2[4]:
                    print("Clue:\ttrajectory")
                if word == level_2[5]:
                    print("Clue:\tcreative activity, such as painting, music, literature, and dance.")
                if word == level_2[6]:
                    print("Clue:\tmean, median, mode")
                if word == level_2[7]:
                    print("Clue:\tThermodynamics")
            if word in level_3:
                if word == level_3[0]:
                    print("Clue:\tneil armstrong")
                if word == level_3[1]:
                    print("Clue:\tFloorplan")
                if word == level_3[2]:
                    print("Clue:\tearth")
                if word == level_3[3]:
                    print("Clue:\tmental health")
                if word == level_3[4]:
                    print("Clue:\tmusic, theatre, concert")
                if word == level_3[5]:
                    print("Clue:\tmelo, romcom, action")
                if word == level_3[6]:
                    print("Clue:\tplants and trees")
                if word == level_3[7]:
                    print("Clue:\tschedules, meetings")
                if word == level_3[8]:
                    print("Clue:\tchemical reactions")
                if word == level_3[9]:
                    print("Clue:\tenvironment")
                if word == level_3[10]:
                    print("Clue:\tplayer")
                if word == level_3[11]:
                    print("Clue:\tlecturer")

        x1 = [0]

        def box():
            print("There are", len(word), "letters")
            b = []
            box_con = 0
            while len(word) != box_con:
                box_con += 1
                b.append("[]")
                b1 = ''.join(b)
                if len(word) == box_con:
                    print(b1)

        def main():
            i = 5
            desc()
            while i != 0:
                print("Guess the word:")
                box()
                guess = str.lower(input())
                if guess == "help":
                    if x1[0] >= 0:
                        clue()
                        x1.clear()
                        x1.append(1)
                elif len(word) == len(guess):
                    if guess != word:
                        i -= 1
                        print("Wrong you only have", i, "chances left")
                        if i == 2 and x1[0] == 0:
                            clue()
                        elif i == 0:
                            print("Game Over!!!")
                            exit()
                        continue
                    elif guess == word:
                        print("Correct")
                        while lvl_num < 3:
                            key = input("Do you want to proceed to the next level? YES/NO\n")
                            if str.lower(key) == "yes":
                                nxt_lvl()
                                break
                            elif str.lower(key) == "no":
                                key1 = input("Do you want to quit? YES/NO\n")
                                if str.lower(key1) == "yes":
                                    print("Goodbye!")
                                    exit()
                                elif str.lower(key1) == "no":
                                    continue
                    break
                else:
                    print("Invalid Input")

        main()

        continue

    print("Congratulations you won!!!")


loop()
