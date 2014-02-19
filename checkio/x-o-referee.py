def checkio(game_result):
    tmp =[]
    tmp1= ''
    tmp2 = ''
    for i in range(0,len(game_result)):
       tmp.append(game_result[i])
       tmp.append(game_result[0][i] + game_result[1][i] + game_result[2][i])
       tmp1 += game_result[i][i]
       tmp2 += game_result[i][2-i]
    tmp.append(tmp1)
    tmp.append(tmp2)
    for x in tmp:
        if x.count("O") == 3:
            return "O"
        if x.count("X") == 3:
            return "X"
    return "D"
        

#These "asserts" using only for self-checking and not necessary for auto-testing

if __name__ == '__main__':
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"


'''
def checkio(game_result):
    # Column and row checking
    for i in range(3):
        if game_result[i][0] == game_result[i][1] == game_result[i][2]: return game_result[i][0]
        if game_result[0][i] == game_result[1][i] == game_result[2][i]: return game_result[0][i]
    # Diagonal checking
    if game_result[0][0] == game_result[1][1] == game_result[2][2]: return game_result[1][1]
    if game_result[2][0] == game_result[1][1] == game_result[0][2]: return game_result[1][1]
    return "D"
'''