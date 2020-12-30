#!/bin/sh
# Reset GH Pages branch to grab any changes in main branch
git branch -f gh-pages main
git checkout gh-pages
git push origin +HEAD

# Build app
transcrypt --nomin --build --map tictacreact

# Deploy
touch .nojekyll
git add ./.nojekyll
git add ./__target__/
git commit -m "GH Deployment"
git push origin gh-pages

# Go back to main branch
git checkout main
