from stockfish import Stockfish
stockfish_path = "C:/Users/mpala/Downloads/stockfish-11-win/stockfish-11-win/Windows/stockfish_20011801_x64"


def getMove():
    move = input("Enter next move: ")
    return move


def main():
    stockfish = Stockfish(stockfish_path)
    moves = []
    while(stockfish.get_evaluation() != {"type":"mate", "value":0}):
        
        # display updated board
        print(stockfish.get_board_visual())
        
        # make moves as white
        next_move = getMove()
        if stockfish.is_move_correct(next_move):
            moves.append(next_move)
        else:
            print("not a valid move")
            getMove()
        stockfish.set_position(moves)
        print(stockfish.get_board_visual())

        # get bot's move
        bot_move = stockfish.get_best_move()
        print("Bot moves: " + bot_move)
        moves.append(bot_move)
        stockfish.set_position(moves)


if __name__ == "__main__":
    main()