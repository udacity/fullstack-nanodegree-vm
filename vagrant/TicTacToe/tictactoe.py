#
import io


current_positions = {"t l" : " ", "t c" : " ", "t r" : " ",
    "c l" : " ", "c c" : " ", "c r" : " ",
    "b l" : " ", "b c" : " ", "b r" : " "}
current_player= "X"

def disp_board(current_positions):  
    board = """
     {t l} | {t c} | {t r}
    -----------
     {c l} | {c c} | {c r} 
    -----------
     {b l} | {b c} | {b r}
    """.format(**current_positions)
    print board
def user_move(current_positions, current_player):
    # Viable options:
    possible_moves = []
    user_promt = "Please pick your move from the options below!"
    for pos in current_positions:
        if current_positions[pos] == " ":
            possible_moves.append(pos)
            user_promt += "\n" + pos
    user_promt += "\n"
    # Evaluate chosen option 
    valid_input = False
    user_choice = raw_input(user_promt).lower()
    while not user_choice in possible_moves:
        user_choice = raw_input(user_promt).lower()
    # Update dicts positions and current_player
    current_positions[user_choice] = current_player #chosen pos from valid options gets player value
    if current_player == "X":
        current_player="O"
    elif current_player=="O":
        current_player="X"
    return current_positions, current_player

def is_game_over(current_positions):
    # Only 8 ways to win and only 1 possible winner!!
    winners = [["t l","t c", "t r"],
                ["c l","c c", "c r"],
                ["b l","b c", "b r"],
                ["t l","c l", "b l"],
                ["t c","c c", "b c"],
                ["t r","c r", "b r"],
                ["t l","c c", "b r"],
                ["t r","c c", "b l"]]
    for win in winners:
        first_required_pos = current_positions[win[0]]
        if first_required_pos != " ":
            possibly_won = True 
            for value in win:
                if current_positions[value] != first_required_pos:
                    possibly_won = False
                    break
            if possibly_won:
                return first_required_pos + " Wins!"
    is_draw = True
    for pos in current_positions:
        if current_positions[pos] == " ":
            is_draw = False
            return False
    if is_draw:
        return "Draw!"

def play_game():
    current_positions = {"t l" : " ", "t c" : " ", "t r" : " ",
    "c l" : " ", "c c" : " ", "c r" : " ",
    "b l" : " ", "b c" : " ", "b r" : " "}
    current_player = "X"
    result = False
    while not result:
        dis_board(current_positions)
        current_positions, current_player = user_move(current_positions, current_player)
        result = is_game_over(current_positions)
        if result:
            print "GAME OVER"
            print "Result: ", result


play_game()

    