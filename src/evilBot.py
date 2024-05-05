'''
Python Chess Bot Challenge 
---------------------------
- Token limitation (1024 tokens) and language limitation
- Only editing the think function (which you will submit)
- Evaluate board using evaluate_board(board) function
- See documentation of python-chess here https://python-chess.readthedocs.io/en/latest/

Allowed to import these modules:
- time
- numpy
- from uci import * (eg. evaluate_board)
- chess.* - except chess.engine
'''

'''
evilBot - an example bot for the chess challenge
'''

def think(board):
  from uci import evaluate_board
  bestScore = -30000
  bestMove = None
  for move in board.legal_moves:
    board.push(move)
    score = -evaluate_board(board)
    board.pop()
    if score > bestScore:
      bestScore = score
      bestMove = move

  return bestMove
