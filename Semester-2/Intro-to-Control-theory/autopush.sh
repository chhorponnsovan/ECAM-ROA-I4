#!/bin/sh
# Auto push to git repository
# Usage: autopush.sh [-g] "commit message"

run_generate=0
if [ "$1" = "-g" ]; then
  run_generate=1
  shift
fi

commit_msg=${1:-"Auto commit"}

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Error: this directory is not a git repository." >&2
  exit 1
fi

if [ "$run_generate" -eq 1 ]; then
  if [ -f "generate_review.py" ]; then
    if command -v python >/dev/null 2>&1; then
      python generate_review.py
    elif command -v python3 >/dev/null 2>&1; then
      python3 generate_review.py
    else
      echo "Error: python is not installed." >&2
      exit 1
    fi
  else
    echo "Warning: generate_review.py not found in current directory; skipping -g." >&2
  fi
fi

branch=$(git rev-parse --abbrev-ref HEAD)

git add .
if git diff --quiet --cached --ignore-submodules --; then
  echo "No changes to commit."
else
  git commit -m "$commit_msg"
fi

git push origin "$branch"