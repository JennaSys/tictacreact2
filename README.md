# React tutorial app using Python with Transcrypt
**This is a refactored version of [tictacreact](https://github.com/JennaSys/tictacreact) that uses functional components instead of class components**

This is based on the React Tutorial: [Intro to React](https://reactjs.org/tutorial/tutorial.html)

Code is transpiled from Python to JavaScript using [Transcrypt](https://www.transcrypt.org)

```pip install transcrypt```

To build with non-minified js and python source maps:

```transcrypt --nomin --build --map tictacreact.py```

The code style here uses the approach outined in this [blog post](https://dev.to/jennasys/no-el-eliminate-explicit-calls-to-createelement-when-using-python-to-code-react-applications-5214), but more references can be found on the _[React to Python](https://pyreact.com)_ site.

![tictacreact screenshot](https://github.com/JennaSys/tictacreact2/raw/main/screenshot.png)

Live demo: [https://jennasys.github.io/tictacreact2/](https://jennasys.github.io/tictacreact2/)
