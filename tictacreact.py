from pyreact import render, useState, useEffect, createElement as el
from pyreact import createContext, useContext


Ctx = createContext()


def Square(props):
    idx = props['idx']

    ctx = useContext(Ctx)
    squares = ctx['squares']
    onClick = ctx['onClick']

    return el('button', {'className': 'square',
                         'onClick': lambda: onClick(idx)
                         }, squares[idx])


def Row(props):
    rowNum = props['rowNum']

    row = [el(Square, {'idx': (rowNum * 3) + col_num}) for col_num in range(3)]
    return el('div', {'className': 'board-row'}, row)


def Board():
    rows = [el(Row, {'rowNum': row_num}) for row_num in range(3)]
    return el('div', None, rows)


def Moves(props):
    numMoves = props['numMoves']
    setStepNumber = props['setStepNumber']

    def get_move(move):
        desc = ('Go to move #' + str(move)) if move > 0 else 'Go to game start'
        return el('li', {'key': move},
                  el('button', {'className': 'move-history',
                                'onClick': lambda: setStepNumber(move)
                                }, desc)
                  )

    return [get_move(move) for move in range(numMoves)]


def Game():
    board, setBoard = useState({'squares': [None for _ in range(9)]})
    history, setHistory = useState([board])
    stepNumber, setStepNumber = useState(0)
    xIsNext, setXIsNext = useState(True)
    winner, setWinner = useState(False)

    def handle_click(i):
        new_squares = list(board['squares'])
        if winner or new_squares[i]:
            return  # Nothing to do

        new_squares[i] = 'X' if xIsNext else 'O'

        tmp_history = history[:stepNumber + 1]
        new_history = [{'squares': move['squares']} for move in tmp_history]
        new_history.append({'squares': new_squares})
        setHistory(new_history)
        setStepNumber(len(new_history) - 1)

    if winner is not None:
        status = f"Winner: {winner}"
    elif stepNumber == 9:
        status = "No Winner"
    else:
        status = f"Next player: {'X' if xIsNext else 'O'}"

    def updateBoard():
        setBoard(history[stepNumber])
        setXIsNext((stepNumber % 2) == 0)

    useEffect(updateBoard, [stepNumber])
    useEffect(lambda: setWinner(calculate_winner(board['squares'])), [board])

    return el(Ctx.Provider, {'value': {'squares': board['squares'],
                                       'onClick': handle_click}
                             },
              el('div', {'className': 'game'},
                 el('div', {'className': 'game-board'},
                    el(Board, None),
                    el('div', {'className': 'game-status'}, status),
                    ),
                 el('div', {'className': 'game-info'}, 'Move History',
                    el('ol', None,
                       el(Moves, {'numMoves': len(history),
                                  'setStepNumber': setStepNumber}
                          )
                       )
                    )
                 )
              )


# Render the component in a 'container' div
render(Game, None, 'root')


def calculate_winner(squares):
    lines = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    for line in lines:
        a, b, c = line
        if squares[a] and (squares[a] == squares[b]) and (squares[a] == squares[c]):
            return squares[a]
    return None
