# __pragma__ ('skip')
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
createElement = React.createElement
useState = React.useState
useEffect = React.useEffect
createContext = React.createContext
useContext = React.useContext


def render(root_component, props, container):
    def main():
        ReactDOM.render(
            React.createElement(root_component, props),
            document.getElementById(container)
        )

    document.addEventListener("DOMContentLoaded", main)
