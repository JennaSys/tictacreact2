#!/bin/sh
git branch -f gh-pages main
git checkout gh-pages
git push origin +HEAD

transcrypt --nomin --build --map tictacreact.py

git add ./__target__/
git commit -m "GH Deployment"
git push origin gh-pages

git checkout main
