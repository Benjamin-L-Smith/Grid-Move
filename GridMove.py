#This allows the user to move a token 'A' around on a 5x5 grid.
#They can move up/down/left/right, but the respective options are not available if the user is on an edge/corner tile.

bold = "\033[1m" #bold text
nold = "\033[0m" #not bold text

def move(playerIs):
    if(playerIs==1): #this means the player is at Tile 1
        one="A"
        tiles=playerIs
    else:
        one="X"
    if(playerIs==2):
        two="A"
        tiles=playerIs
    else:
        two="X"
    if(playerIs==3):
        three="A"
        tiles=playerIs
    else:
        three="X"
    if(playerIs==4):
        four="A"
        tiles=playerIs
    else:
        four="X"
    if(playerIs==5):
        five="A"
        tiles=playerIs
    else:
        five="X"
    if(playerIs==6):
        six="A"
        tiles=playerIs
    else:
        six="X"
    if(playerIs==7):
        seven="A"
        tiles=playerIs
    else:
        seven="X"
    if(playerIs==8):
        eight="A"
        tiles=playerIs
    else:
        eight="X"
    if(playerIs==9):
        nine="A"
        tiles=playerIs
    else:
        nine="X"
    if(playerIs==10):
        ten="A"
        tiles=playerIs
    else:
        ten="X"
    if(playerIs==11):
        eleven="A"
        tiles=playerIs
    else:
        eleven="X"
    if(playerIs==12):
        twelve="A"
        tiles=playerIs
    else:
        twelve="X"
    if(playerIs==13):
        thirteen="A"
        tiles=playerIs
    else:
        thirteen="X"
    if(playerIs==14):
        fourteen="A"
        tiles=playerIs
    else:
        fourteen="X"
    if(playerIs==15):
        fifthteen="A"
        tiles=playerIs
    else:
        fifthteen="X"
    if(playerIs==16):
        sixteen="A"
        tiles=playerIs
    else:
        sixteen="X"
    if(playerIs==17):
        seventeen="A"
        tiles=playerIs
    else:
        seventeen="X"
    if(playerIs==18):
        eightteen="A"
        tiles=playerIs
    else:
        eightteen="X"
    if(playerIs==19):
        nineteen="A"
        tiles=playerIs
    else:
        nineteen="X"
    if(playerIs==20):
        twenty="A"
        tiles=playerIs
    else:
        twenty="X"
    if(playerIs==21):
        twentyOne="A"
        tiles=playerIs
    else:
        twentyOne="X"
    if(playerIs==22):
        twentyTwo="A"
        tiles=playerIs
    else:
        twentyTwo="X"
    if(playerIs==23):
        twentyThree="A"
        tiles=playerIs
    else:
        twentyThree="X"
    if(playerIs==24):
        twentyFour="A"
        tiles=playerIs
    else:
        twentyFour="X"
    if(playerIs==25):
        twentyFive="A"
        tiles=playerIs
    else:
        twentyFive="X"
    print("[ ][1][2][3][4][5]")
    print(f"[1][{one}][{two}][{three}][{four}][{five}]")
    print(f"[2][{six}][{seven}][{eight}][{nine}][{ten}]")
    print(f"[3][{eleven}][{twelve}][{thirteen}][{fourteen}][{fifthteen}]")
    print(f"[4][{sixteen}][{seventeen}][{eightteen}][{nineteen}][{twenty}]")
    print(f"[5][{twentyOne}][{twentyTwo}][{twentyThree}][{twentyFour}][{twentyFive}]")

    return tiles #this then becomes lystTiles, used to keep track of where the player has been
    #I realize I could just append 'player' instead, but I wrote this when it was past my bedtime.


count=0 #actions
x=1 #used for the while loop
player=13 #player starts at threeThree / 13
lystTiles=[13] #tracks where the player has been
dyctTiles={} #lystTiles will be reformated into this dict later
#the grid tiles are numbered so they increase left-to-right & top-to-bottom.
print("[ ][1][2][3][4][5]")
print("[1][X][X][X][X][X]")
print("[2][X][X][X][X][X]")
print("[3][X][X][A][X][X]") #the player is 'A'
print("[4][X][X][X][X][X]")
print("[5][X][X][X][X][X]")


while(x==1): #I use 'x' here because I use 'i' later, and that code was written first.
    stop=input("Press ENTER to continue or type 'no' to stop. ")
    if(stop.lower()=="no"):
        x+=1
    else:
        if(player!=1 and player!=2 and player!=3 and player!=4 and player!=5 and player!=6 and player!=11 and player!=16 and player!=21 and player!=22 and player!=23 and player!=24 and player!=25 and player!=10 and player!=15 and player!=20):
            user=str(input("Would you like to move Up[w], Left[a], Down[s], or Right[d]? "))
            if(user.lower()=="w" or user=="8"):
                player-=5 #moves the player Up 1 tile
            elif(user.lower()=="a" or user=="4"):
                player-=1  #moves the player Left 1 tile
            elif(user.lower()=="s" or user=="2"):
                player+=5  #moves the player Down 1 tile
            elif(user.lower()=="d" or user=="6"):
                player+=1  #moves the player Right 1 tile
        elif(player==2 or player==3 or player==4):
            user=input("Would you like to move Left[a], Down[s], or Right[d]? ")
            if(user.lower()=="a" or user=="4"):
                player-=1  #moves the player Left 1 tile
            elif(user.lower()=="s" or user=="2"):
                player+=5  #moves the player Down 1 tile
            elif(user.lower()=="d" or user=="6"):
                player+=1  #moves the player Right 1 tile
            else:
                print(f"{bold}[Error - You cannot move off the grid]{nold}")
        elif(player==6 or player==11 or player==16):
            user=input("Would you like to move Up[w], Down[s], or Right[d]? ")
            if(user.lower()=="w" or user=="8"):
                player-=5 #moves the player Up 1 tile
            elif(user.lower()=="s" or user=="2"):
                player+=5  #moves the player Down 1 tile
            elif(user.lower()=="d" or user=="6"):
                player+=1  #moves the player Right 1 tile
            else:
                print(f"{bold}[Error - You cannot move off the grid]{nold}")
        elif(player==22 or player==23 or player==24):
            user=input("Would you like to move Up[w], Left[a], or Right[d]? ")
            if(user.lower()=="w" or user=="8"):
                player-=5 #moves the player Up 1 tile
            elif(user.lower()=="a" or user=="4"):
                player-=1  #moves the player Left 1 tile
            elif(user.lower()=="d" or user=="6"):
                player+=1  #moves the player Right 1 tile
            else:
                print(f"{bold}[Error - You cannot move off the grid]{nold}")
        elif(player==10 or player==15 or player==20):
            user=input("Would you like to move Up[w], Left[a], Down[s]? ")
            if(user.lower()=="w" or user=="8"):
                player-=5 #moves the player Up 1 tile
            elif(user.lower()=="a" or user=="4"):
                player-=1  #moves the player Left 1 tile
            elif(user.lower()=="s" or user=="2"):
                player+=5  #moves the player Down 1 tile
            else:
                print(f"{bold}[Error - You cannot move off the grid]{nold}")
        elif(player==1):
            user=input("Would you like to move Down[s] or Right[d]? ")
            if(user.lower()=="s" or user=="2"):
                player+=5  #moves the player Down 1 tile
            elif(user.lower()=="d" or user=="6"):
                player+=1  #moves the player Right 1 tile
            else:
                print(f"{bold}[Error - You cannot move off the grid]{nold}")
        elif(player==5):
            user=input("Would you like to move Left[a] or Down[s]? ")
            if(user.lower()=="a" or user=="4"):
                player-=1  #moves the player Left 1 tile
            elif(user.lower()=="s" or user=="2"):
                player+=5  #moves the player Down 1 tile
            else:
                print(f"{bold}[Error - You cannot move off the grid]{nold}")
        elif(player==21):
            user=input("Would you like to move Up[w] or Right[d]? ")
            if(user.lower()=="w" or user=="8"):
                player-=5 #moves the player Up 1 tile
            elif(user.lower()=="d" or user=="6"):
                player+=1  #moves the player Right 1 tile
            else:
                print(f"{bold}[Error - You cannot move off the grid]{nold}")
        elif(player==25):
            user=input("Would you like to move Up[w] or Left[a]? ")
            if(user.lower()=="w" or user=="8"):
                player-=5 #moves the player Up 1 tile
            elif(user.lower()=="a" or user=="4"):
                player-=1  #moves the player Left 1 tile
            else:
                print(f"{bold}[Error - You cannot move off the grid]{nold}")
        lystTiles.append(move(player)) #this returns the where the player is, as well as the updated grid.


for i in lystTiles: #puts number in dict, and counts repeats
    if i in dyctTiles:
        dyctTiles[i]+=1
    else:
        dyctTiles[i]=1
print("")
print("Behold, all spaces you moved to, and how many times you went there:")
print("note: tiles are orderd from top-to-bottom, and from left-to-right.")
print(dyctTiles)



'''
started work on: [March 6th] at [7AM]
most recent update on: [March 15th] at [11PM]
estimated hours worked on: [2 hours, 28 minutes]
'''