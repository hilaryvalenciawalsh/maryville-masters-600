import time
import random

villians = ["Moff Gideon", "Dark Trooper", "Dr. Perishing"]
villiansIntro = [" will lightsaber you!", " will trap you!", " will kill you!"]

def line_printing(message):
    print(message)
    time.sleep(2.5)
def intro():
    line_printing("\n\n\nThe Child has been taken by the evil Moff Gideon!")
    line_printing("It's your job as the Mandalorian to save The Child!")
    line_printing("You've found the Imperial Light Cruiser, and have managed to make your way in.....")
    line_printing("Will you save The Child?") 
intro()
def skywalker():
    line_printing("\n\n\nThe Child has been saved...")
    line_printing("There is a loud sound, and the doors to the Imperial Light Cruiser's control center start to open...")
    line_printing("Luke Skywalker and R2-D2 walk in to take The Child to learn how to use his Force...")
    line_printing("The Child gives you a hug, and as Luke picks up The Child... you say your final goodbye...") 

class theChildDrawing:
    print("....................................................................." + "\n"
"................................................................................" + "\n"
"................../((#/........................................................." + "\n"
"....................((#((#%#...................................................." + "\n"
"....................(######(/#%%#......./((/...................................." + "\n"
".....................#####((#((############(((#(((,............................." + "\n"
".......................#((((*/((###(((((%%####(/((///..........................." + "\n"
"..........................//(((((#* , ./####(////((////,........................" + "\n"
"............................######(((((((#//(/.. /*(/**/((((((/................." + "\n"
"................................/****(##((/(//    /*,*,*,.,,,,,,,*/(((*........." + "\n"
"........................##((/*,**/**//((*,**///((/**,...,,,******///***/,*,....." + "\n"
"........................##(######******,...,,**,,,..**/((/,***//////(/.........." + "\n"
"........................#(#((###(#/.,**(((((/(((//////**,,......................" + "\n"
"........................*#(((((((./(((/((//////*//**,*,,,......................." + "\n"
".......................*(((/(((**((((((/////*/****,,..,****,...................." + "\n"
"..................(////*(///(##((*  *((///****  ,****,,,*////*.................." + "\n"
"................(/(((((/*/(//****///***,.,...,***,,,,*////***//*(..............." + "\n"
"............../(((/(((((/**/((///((/(**,/,/*//*/*,*///(/,**,,,*/((*............." + "\n"
".............#(((((*/*(((/*/((((((/*,**//*//****//(((((,*,,**/*((/((,..........." + "\n"
"...........(#*(((((//**/((//(((((///*/((//(*///(((((((/,.*///((//((((/.........." + "\n"
"..........##(#((/((*(/**/((/((((*//*(((//((/*/(((((////.,*/*/*//(/(/(/(/........" + "\n"
"............((((///*(/**/((((((/,///(///,/(/*/((/////(/,...,./(((***,  ........." + "\n"
"................/**,#(**//((((/**/*////*/(//////(///((/,.,. *//*,..............." + "\n"
".............../#(,.((**/////(/**//*////(///////////(/*,,. ,*/*,,*,............." + "\n"
"............../(//**((/*/(//((/,*/*//**///*****//**///*,,,...,, .,*/............" + "\n"
"..............,#**.(/////(/((/,*//*///**/***///(/*////*..........,*,............" + "\n"
"...................((/////(///,*/*/////,/*////((**//*/*,........................" + "\n"
".................(((/////((//,*///*///*,(/*(((/*,*******........................" + "\n"
"................/*(/////(((/**/(//*((///((,//,.,*,******,......................." + "\n"
"................((((////((///((((//(////(((/**/,*****,,,,,,....................." + "\n"
"................*////(/(((//(((((///*////((***,*********,,*,...................." + "\n"
"...................,,/////((((((/*//*//////*,*******,.,,,,,,...................." + "\n"
"............................*//*//////*//***/*,,**..,..........................." + "\n"
"...............................*,**,,(..........................................")

class theMandalorian:
    def __init__(self, name, beskar, armor):
        self.name = name
        self.level = 0
        self.beskar = beskar
        self.armor = armor
    def __str__(self):
        ret = "\n"
        ret += "SAVING THE CHILD " + "\n"
        ret += "Level : " + str(self.level) + "\n"
        ret += "Beskar : " + str(self.beskar) + "\n"
        ret += "Armor : " + str(self.armor) + "\n"
        return ret

class Villian:
    def __init__(self, name, level, introduction, negativeArmor):
        self.name = name
        self.level = level
        self.introduction = introduction
        self.negativeArmor = negativeArmor
    def __str__(self):
        ret = "\n"
        ret += "Villian : " + self.name + "\n"
        ret += "Level : " + str(self.level) + "\n"
        ret += "Introduction : " + str(self.introduction) + "\n"
        ret += "negativeArmor : " + str(self.negativeArmor) + "\n"
        return ret


def play(mandalorian, evilDudes, steps):
    for i in range(1, steps+1): 
        input("\n----- Press enter to walk into the Imperial Light Crusier. -----\n") 
        mandalorian.level = i 
        print(mandalorian.name + " is in space " + str(mandalorian.level))
        for evil in evilDudes:
            if mandalorian.level == evil.level: 
                mandalorian.armor -= evil.negativeArmor 
                print("You are getting ambushed by " + evil.name + ". " + evil.introduction + " You lost " + str(evil.negativeArmor) + " pieces of armor! 👺")
                break
        else: 
            pickup = random.randint(10, 20)
            mandalorian.beskar += pickup
            print("You found " + str(pickup) + " Beskar! 💸")
        if mandalorian.armor <= 0:
            print("\n\n" + mandalorian.name + " did not save The Child 😢")
            break
    else:
        print("\n\nThis is the way! " + mandalorian.name + " has taken over the Imperial Light Cruiser, you've saved The Child!") 
        skywalker()
        
def main():
    steps = 10
    mando = theMandalorian("The Mandalorian", 0, 30)
    num_theVillians = random.randint(int(0.2*steps), int(0.6*steps)) 
    theVillians = []
    for _ in range(num_theVillians):
        Villian_name, Villian_intro = random.choice(villians), random.choice(villiansIntro)
        Villian_level, Villian_negativeArmor = random.randint(1, steps), random.randint(5, 15)
        theVillians.append(Villian(Villian_name, Villian_level, Villian_name + Villian_intro, Villian_negativeArmor))
    play(mando, theVillians, steps) 
    print("\n\nThanks for playing Saving The Child, here are your totals:") 
    print(mando)

if __name__ == "__main__":
    main()