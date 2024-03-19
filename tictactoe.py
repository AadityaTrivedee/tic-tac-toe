from termcolor import colored
#Defining initial values for players
pointindexX = 0
pointindexO = 0
flag = False

# ask() function works for repetition of game rounds
def ask():
    global question
    question = input("Do you want to play? Y/N: ").upper()
    if question == "Y":
        play()
    else :
        print(colored('\033[1m' + "-------------", "red"))
        print(colored('\033[1m' + "|TIC TAC TOE|", "red"))
        print(colored('\033[1m' + "-------------", "red"))
        print(colored('\033[1m' + "|FINAL SCORE|", "red"))
        print('\033[1m' + ( colored( "|","red") + colored("  X  ","green") + '\033[1m' + colored("|","red") + '\033[1m' + colored("  O  ","blue") + '\033[1m' + colored("|", "red")))
        print(colored('\033[1m' + "-------------", "red"))
        print(colored('\033[1m' + "| ","red"), '\033[1m' + colored(pointindexX,"green"),  colored('\033[1m' + " | ","red"), '\033[1m' + colored(pointindexO,"blue") , colored('\033[1m' + " |","red"))
        print(colored('\033[1m' + "-------------", "red"))
        print("Thanks")

# play() function initialises the game and allows users to play
def play():
    A = ["1","2","3","4","5","6","7","8","9"]
    player1 = colored('\033[1m' + "X", "green")
    player2 = colored('\033[1m' + "O", "blue")
    def board():
        print(colored('\033[1m' + "-------------", "red"))
        print(colored('\033[1m' + "|TIC TAC TOE|", "red"))
        print(colored('\033[1m' + "-------------", "red"))
        print(colored('\033[1m' + "|SCORE BOARD|", "red"))
        print('\033[1m' + ( colored( "|","red") + colored("  X  ","green") + '\033[1m' + colored("|","red") + '\033[1m' + colored("  O  ","blue") + '\033[1m' + colored("|", "red")))
        print(colored('\033[1m' + "-------------", "red"))
        print(colored('\033[1m' + "| ","red"), '\033[1m' + colored(pointindexX,"green"),  colored('\033[1m' + " | ","red"), '\033[1m' + colored(pointindexO,"blue") , colored('\033[1m' + " |","red"))
        print(colored('\033[1m' + "-------------", "red"))
        print(colored('\033[1m' + "|","red"), A[0], colored('\033[1m' + "|","red"), A[1], colored('\033[1m' +"|","red") , A[2], colored('\033[1m' +"|","red"))
        print(colored('\033[1m' + "-------------", "red"))
        print(colored('\033[1m' + "|","red"), A[3], colored('\033[1m' +"|","red"), A[4], colored('\033[1m' +"|","red") , A[5], colored('\033[1m' +"|","red"))
        print(colored('\033[1m' + "-------------", "red"))
        print(colored('\033[1m' + "|","red"), A[6], colored('\033[1m' +"|","red"), A[7], colored('\033[1m' +"|","red") , A[8], colored('\033[1m' +"|","red"))
        print(colored('\033[1m' + "-------------", "red"))

    #turn() function initiates turns for players to play.
    def turn(var):
        move = int(input(f"Player {var}, \033[1m Enter a number from 1 to 9:"))
        if A[move-1] is not player1 and A[move-1] is not player2:
            A[move-1] = var
            board()
        else:
            print(colored('\033[1m' + "Opps! Already Occupied.", "red"))
            turn(var)

    #winc() is a function for defining winning conditions for the players.
    def winc():
        global pointindexX
        global pointindexO
        win_conditions = [(0,1,2),(0,3,6),(0,4,8),(1,4,7),(2,5,8),(3,4,5),(6,7,8),(2,4,6)]
        for i, j, k in win_conditions:
            if A[i] == A[j] == A[k] and A[i] not in ["1","2","3","4","5","6","7","8","9"]:
                print(colored('\033[1m' + "THE WINNER IS ", "red") + A[i])
                if A[i] is player1:
                    pointindexX +=1
                elif A[i] is player2:
                    pointindexO +=1
                ask()
                return True      

    #tie() function defines ways the game might be tied.
    def tie():
        if all(i == player1 or i == player2 for i in A) :
            print(colored('\033[1m' + "IT IS A TIE.", "red"))
            ask()
            return True
            
    #win() function loops to check if a player has won or not. 
    def win():
            global flag
            while flag is not True:
                turn(player1)
                flag = winc()
                if flag is True:
                    break
                else:
                    L = tie()
                    if L is True:
                        break
                    else:
                        turn(player2)
                        flag = winc()
                        if flag is True:
                            break
                        else:
                            L = tie()
                            if L is True:
                                break
                            else:
                                continue
    board()
    win()
ask()
