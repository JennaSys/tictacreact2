# __pragma__ ('skip')
"""
These JavaScript object stubs are just to
quiet the Python linter and are ignored by transcrypt as long
as they are imported inside of pragma skip/noskip lines.
"""


class React:
    createElement = None
    useState = None
    useEffect = None
    createContext = None
    useContext = None


class ReactDOM:
    render = None


class document:
    getElementById = None
    addEventListener = None


# __pragma__ ('noskip')


# Map React javaScript objects to Python identifiers
# createElement = React.createElement
useState = React.useState
useEffect = React.useEffect
createContext = React.createContext
useContext = React.useContext


def component(react_component):
    def react_element(props, *children):
        return React.createElement(react_component, props, *children)

    return react_element


# Wrap native html elements
Form = component('form')
Label = component('label')
Input = component('input')
Ol = component('ol')
Li = component('li')
Option = component('option')
Button = component('button')
Div = component('div')
Span = component('span')
P = component('p')
A = component('a')
Img = component('img')
H1 = component('h1')
H2 = component('h2')


# Wrap the ReactDOM.render method to hide JavaScript details
def render(root_component, props, container):
    def main():
        ReactDOM.render(
            root_component(props),
            document.getElementById(container)
        )

    document.addEventListener("DOMContentLoaded", main)
