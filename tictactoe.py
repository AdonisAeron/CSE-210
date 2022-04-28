'''
TicTacToe
Author: Trevor Jones
'''

def main():

    pOne = ["x"]
    pTwo = ["o"]
    pOne.append(input("Please state Player One's name: "))
    pTwo.append(input("Please state Player Two's name: "))
    Participents = [pOne, pTwo]
    game = create()
    player = pChange(["Hold", ""], Participents)
    state = 0

    while(state == 0):

        display(game)
        action(player, game)
        state, winner = win(game, Participents)
        player = pChange(player, Participents)

    display(game)

    if(state == 2):

        print(f"\n{winner} Wins!")

    elif(state == 1):

        print("\nIt's a Draw!")

def create():

    game = []

    for space in range(9):
        game.append(space + 1)

    return game

def display(game):

    print(f"\n {game[0]} | {game[1]} | {game[2]} \
        \n---+---+---\
        \n {game[3]} | {game[4]} | {game[5]} \
        \n---+---+---\
        \n {game[6]} | {game[7]} | {game[8]} ")

def action(player, game):

    space = int(input(f"{player[1]}'s turn! Please choose your next move! "))
    game[space - 1] = player[0]

def pChange(player, cPlayers):

    if player[0] == "Hold" or player[0] == 'o':
        return cPlayers[0]

    elif player[0] == 'x':
        return cPlayers[1]

def win(game, cPlayers):

    if((game[0] == game[1] == game[2] or game[0] == game[3] == game[6] or game[0] == game[4] == game[8])):

        if(game[0] == (cPlayers[0][0])):

            winner = cPlayers[0][1]
            state = 2

        elif(game[0] == (cPlayers[1][0])):

            winner = cPlayers[1][1]
            state = 2

        return state, winner

    elif((game[3] == game[4] == game[5] or game[2] == game[4] == game[6] or game[1] == game[4] == game[7] )):

        if(game[4] == (cPlayers[0][0])):

            winner = cPlayers[0][1]
            state = 2

        elif(game[4] == (cPlayers[1][0])):

            winner = cPlayers[1][1]
            state = 2

        return state, winner

    elif((game[6] == game[7] == game[8] or game[2] == game[5] == game[8] )):

        if(game[8] == (cPlayers[0][0])):

            winner = cPlayers[0][1]
            state = 2

        elif(game[8] == (cPlayers[1][0])):

            winner = cPlayers[1][1]
            state = 2

        return state, winner

    for space in range(9):

        if (game[space] != 'x' and game[space] != 'o'): 
            
            state = 0
            break
        
        else:

            state = 1

    if(state == 0 or state == 1):

        return state, "draw"

    else:

        state = 0

        return state, "cont"


if __name__ == "__main__":
    main()