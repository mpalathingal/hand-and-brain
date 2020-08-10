from stockfish import Stockfish

def getMove():
    move = input("Enter next move: ")
    return move

def main():
    stockfish = Stockfish("C:/Users/mpala/Downloads/stockfish-11-win/stockfish-11-win/Windows/stockfish_20011801_x64")
    moves = []
    while(stockfish.get_evaluation() != {"type":"mate", "value":0}):
        print(stockfish.get_board_visual())
        next_move = getMove()
        if stockfish.is_move_correct(next_move):
            moves.append(next_move)
        else:
            print("not a valid move")
            getMove()
        stockfish.set_position(moves)
if __name__ == "__main__":
    main()