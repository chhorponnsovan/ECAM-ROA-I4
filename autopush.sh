#!/bin/sh
# Auto push to git repository
# Usage: ./autopush.sh "commit message"

commit_msg=${1:-"Auto commit"}
branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)
if [ -z "$branch" ]; then
  branch="master"
fi

git add .
if git diff --quiet --cached --ignore-submodules --; then
  echo "No changes to commit."
else
  git commit -m "$commit_msg"
fi

git push origin "$branch"