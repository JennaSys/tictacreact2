// Transcrypt'ed from Python, 2022-01-24 13:38:42
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
var __name__ = 'pyreact';
export var useState = React.useState;
export var useEffect = React.useEffect;
export var createContext = React.createContext;
export var useContext = React.useContext;
export var component = function (component) {
	var react_element = function (props) {
		var children = tuple ([].slice.apply (arguments).slice (1));
		return React.createElement (component, props, ...children);
	};
	return react_element;
};
export var Form = component ('form');
export var Label = component ('label');
export var Input = component ('input');
export var Ol = component ('ol');
export var Li = component ('li');
export var Option = component ('option');
export var Button = component ('button');
export var Div = component ('div');
export var Span = component ('span');
export var P = component ('p');
export var A = component ('a');
export var Img = component ('img');
export var H1 = component ('h1');
export var H2 = component ('h2');
export var render = function (root_component, props, container) {
	var main = function () {
		ReactDOM.render (root_component (props), document.getElementById (container));
	};
	document.addEventListener ('DOMContentLoaded', main);
};

//# sourceMappingURL=pyreact.map