#! /bin/bash

NAME=$1 # Repository name parameter
DSC=$2  # Reposiory descirption parameter
TYPE=$3 # Repository type parameter, Public or Private. Defaults to public.

echo "Creating repository"
gh re --new "$NAME" --description "$DSC" --type "$TYPE"
gh re --clone --repo "$NAME"

git add .
git commit -m "📦 NEW: First commit"
git push

echo ''
echo '✅ DONE '
echo ''
