print('''
     ,----.    ,-.   ,----.,------. ,-.   ,-.,-. ,-.
    / ,-,_/  ,'  |  / /"P /`-, ,-','  |  / //  |/ /
   / / __  ,' ,| | / ,---'  / / ,' ,| | / // J P /
  / '-' /,' ,--. |/ /      / /,' ,--. |/ // /|  /
  `----''--'   `-'`'.--""""--.--'   `-'`' `' `-'
  nnnnnnnnnnnnnnnn,'.n*""""*N.`.#######################
  NNNNNNNNNNNNNNN/ J',n*""*n.`L \##### ### ### ### ####
                : J J___/\___L L :#####################
  nnnnnnnnnnnnnn{ [{ `.    ,' }] }## ### ### ### ### ##
  NNNNNNNNNNNNNN: T T /,'`.\ T J :#####################
                 \ L,`*n,,n*',J /
  nnnnnnnnnnnnnnnn`. *n,,,,n* ,'nnnnnnnnnnnnnnnnnnnnnnn
  NNNNNNNNNNNNNNNNNN`-..__..-'NNNNNNNNNNNNNNNNNNNNNNNNN
  ,-.    ,-.  ,-. ,----. ,----.,-. ,----.   ,-. 
  |  `.  \  `.|  \\  .--`\ \"L \\ \\ .-._\  |  `. o!0
  | |. `. \ \ ` L \\  __\ \ .  < \ \\ \  __ | |. `.
  | .--. `.\ \`-'\ \\ `---.\ \L `.\ \\ `-` \| .--. `. 
  `-'   `--``'    `-'`----' `-'`-' `' `----'`-'   `--'
''')

print("Welcome to Tresure Island! Choose you next step carefully!")
print("Your mission is to save the princess!")

choice1 = input('You\'re starting this mission on a different island, deep in the woods. You are hiking up on a mountain so you can make it to the port, but you hit a crosssign on the trail. Where do you want to go? Type "left" or "right": ').lower()

if choice1 == "left":
    choice2 = input('You\'ve made it to the beach. The water is not to deep, but you are a bit afraid of the water. There are boats coming from time to time and they can pick you up and take you to the next island. What do you want to do? Type "wait" to wait for a boat or "swim" to try to get there faster: ').lower()
    if choice2 == "wait":
        choice3 = input("You arrived at he island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which colour do you choose?  ").lower()
        if choice3 == "red":
            print("It's a room full of fire! Gaaaaame oooover!!")
        elif choice3 == "blue":
            print("It's a room full of dragons!!! Game over!")
        elif choice3 == "yellow":
            print("Yuuuuu Huuuuuu! You've made to the princes and saved her!!")
        else:
            print("This dooe doesn't exists. Game over!")
    else:
        print("You've made it to the location to late. So pay attention to your loved ones today and make sure you are not going to get there too late when they need you ! ")
else:
    print("You fell of a cliff. Game over!")






