# React tutorial app using Python with Transcrypt
**This is a refactored version of [tictacreact](https://github.com/JennaSys/tictacreact) that uses functional components instead of class components**

The [no-el branch](https://github.com/JennaSys/tictacreact2/tree/no-el) also uses the createElement component decorator as described in this [blog post](https://dev.to/jennasys/no-el-eliminate-explicit-calls-to-createelement-when-using-python-to-code-react-applications-5214).  

Based on React Tutorial: [Intro to React](https://reactjs.org/tutorial/tutorial.html)

Code is transpiled from Python to JavaScript using [Transcrypt](https://www.transcrypt.org)

```pip install transcrypt```

To build with non-minified js and python source maps:

```transcrypt --nomin --build --map tictacreact.py```

![tictacreact screenshot](https://github.com/JennaSys/tictacreact2/raw/main/screenshot.png)

Live demo: [https://jennasys.github.io/tictacreact2/](https://jennasys.github.io/tictacreact2/)
