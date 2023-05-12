from dataclasses import dataclass
import typing

from pyreact import render, useState, component, createContext, useContext
from pyreact import Button, Div, Li, Ol

Ctx = createContext()
CtxProvider = component(Ctx.Provider)


class IProps(object):
    def _attributes(self):
        return [attr for attr in dir(self) if attr.startswith('set') or (not attr.startswith('__') and not callable(getattr(self, attr)))]

    def toDict(self):
        return {attr: getattr(self, attr) for attr in self._attributes()}


@dataclass(frozen=True)
class ISquare:
    idx: int = None


@component
def Square(props):
    Props = ISquare(**props)

    ctx = useContext(Ctx)
    squares = ctx['squares']
    onClick = ctx['onClick']

    return Button({'className': 'square',
                   'onClick': lambda: onClick(Props.idx)
                   }, squares[Props.idx])


@dataclass(frozen=True)
class IRow:
    rowNum: int = None


@component
def Row(props):
    Props = IRow(**props)

    row = [Square({'idx': (Props.rowNum * 3) + col_num}) for col_num in range(3)]
    return Div({'className': 'board-row'}, row)


@component
def Board():
    rows = [Row({'rowNum': row_num}) for row_num in range(3)]
    return Div(None, rows)


@dataclass(frozen=True)
class IMoves(IProps):
    numMoves: int = None
    setStepNumber: 'typing.Callable' = None


@component
def Moves(props):
    # numMoves = props['numMoves']
    # setStepNumber = props['setStepNumber']

    Props = IMoves(**props)

    @component
    def MoveButton(_props):
        move = _props['move']
        desc = ('Go to move #' + str(move)) if move > 0 else 'Go to game start'
        return Li({'key': move},
                  Button({'className': 'move-history',
                          'onClick': lambda: Props.setStepNumber(move)
                          }, desc)
                  )

    return [MoveButton({'move': move}) for move in range(Props.numMoves)]


@component
def Game():
    history, setHistory = useState([{'squares': [None for _ in range(9)]}])
    stepNumber, setStepNumber = useState(0)

    board = history[stepNumber]
    xIsNext = (stepNumber % 2) == 0
    winner = calculate_winner(board['squares'])

    if winner is not None:
        status = f"Winner: {winner}"
    elif stepNumber == 9:
        status = "No Winner"
    else:
        status = f"Next player: {'X' if xIsNext else 'O'}"

    def handle_click(i):
        new_squares = list(board['squares'])
        if winner or new_squares[i]:  # Already winner or square not empty
            return  # Nothing to do

        new_squares[i] = 'X' if xIsNext else 'O'

        tmp_history = history[:stepNumber + 1]  # Slice in case step changed
        new_history = [{'squares': move['squares']} for move in tmp_history]
        new_history.append({'squares': new_squares})
        setHistory(new_history)
        setStepNumber(len(new_history) - 1)

    return CtxProvider({'value': {'squares': board['squares'],
                                  'onClick': handle_click}
                        },
                       Div({'className': 'game'},
                           Div({'className': 'game-board'},
                               Board(None),
                               Div({'className': 'game-status'}, status),
                               ),
                           Div({'className': 'game-info'}, 'Move History',
                               Ol(None,
                                  # Moves({'numMoves': len(history), 'setStepNumber': setStepNumber})
                                  Moves(**(IMoves(numMoves=len(history), setStepNumber=setStepNumber).toDict()))
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
