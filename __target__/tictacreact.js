// Transcrypt'ed from Python, 2021-01-11 16:10:46
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {createContext, useContext} from './pyreact.js';
import {createElement as el, render, useState} from './pyreact.js';
var __name__ = '__main__';
export var Ctx = createContext ();
export var Square = function (props) {
	var idx = props ['idx'];
	var ctx = useContext (Ctx);
	var squares = ctx ['squares'];
	var onClick = ctx ['onClick'];
	return el ('button', dict ({'className': 'square', 'onClick': (function __lambda__ () {
		return onClick (idx);
	})}), squares [idx]);
};
export var Row = function (props) {
	var rowNum = props ['rowNum'];
	var row = (function () {
		var __accu0__ = [];
		for (var col_num = 0; col_num < 3; col_num++) {
			__accu0__.append (el (Square, dict ({'idx': rowNum * 3 + col_num})));
		}
		return __accu0__;
	}) ();
	return el ('div', dict ({'className': 'board-row'}), row);
};
export var Board = function () {
	var rows = (function () {
		var __accu0__ = [];
		for (var row_num = 0; row_num < 3; row_num++) {
			__accu0__.append (el (Row, dict ({'rowNum': row_num})));
		}
		return __accu0__;
	}) ();
	return el ('div', null, rows);
};
export var Moves = function (props) {
	var numMoves = props ['numMoves'];
	var setStepNumber = props ['setStepNumber'];
	var get_move = function (move) {
		var desc = (move > 0 ? 'Go to move #' + str (move) : 'Go to game start');
		return el ('li', dict ({'key': move}), el ('button', dict ({'className': 'move-history', 'onClick': (function __lambda__ () {
			return setStepNumber (move);
		})}), desc));
	};
	return (function () {
		var __accu0__ = [];
		for (var move = 0; move < numMoves; move++) {
			__accu0__.append (get_move (move));
		}
		return __accu0__;
	}) ();
};
export var Game = function () {
	var __left0__ = useState ([dict ({'squares': (function () {
		var __accu0__ = [];
		for (var _ = 0; _ < 9; _++) {
			__accu0__.append (null);
		}
		return __accu0__;
	}) ()})]);
	var history = __left0__ [0];
	var setHistory = __left0__ [1];
	var __left0__ = useState (0);
	var stepNumber = __left0__ [0];
	var setStepNumber = __left0__ [1];
	var board = history [stepNumber];
	var xIsNext = __mod__ (stepNumber, 2) == 0;
	var winner = calculate_winner (board ['squares']);
	if (winner !== null) {
		var status = 'Winner: {}'.format (winner);
	}
	else if (stepNumber == 9) {
		var status = 'No Winner';
	}
	else {
		var status = 'Next player: {}'.format ((xIsNext ? 'X' : 'O'));
	}
	var handle_click = function (i) {
		var new_squares = list (board ['squares']);
		if (winner || new_squares [i]) {
			return ;
		}
		new_squares [i] = (xIsNext ? 'X' : 'O');
		var tmp_history = history.__getslice__ (0, stepNumber + 1, 1);
		var new_history = (function () {
			var __accu0__ = [];
			for (var move of tmp_history) {
				__accu0__.append (dict ({'squares': move ['squares']}));
			}
			return __accu0__;
		}) ();
		new_history.append (dict ({'squares': new_squares}));
		setHistory (new_history);
		setStepNumber (len (new_history) - 1);
	};
	return el (Ctx.Provider, dict ({'value': dict ({'squares': board ['squares'], 'onClick': handle_click})}), el ('div', dict ({'className': 'game'}), el ('div', dict ({'className': 'game-board'}), el (Board, null), el ('div', dict ({'className': 'game-status'}), status)), el ('div', dict ({'className': 'game-info'}), 'Move History', el ('ol', null, el (Moves, dict ({'numMoves': len (history), 'setStepNumber': setStepNumber}))))));
};
render (Game, null, 'root');
export var calculate_winner = function (squares) {
	var lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]];
	for (var line of lines) {
		var __left0__ = line;
		var a = __left0__ [0];
		var b = __left0__ [1];
		var c = __left0__ [2];
		if (squares [a] && squares [a] == squares [b] && squares [a] == squares [c]) {
			return squares [a];
		}
	}
	return null;
};

//# sourceMappingURL=tictacreact.map