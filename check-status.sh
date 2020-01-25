#!/usr/bin/bash
echo Problems still not solved: $(git ls-files --exclude *[^.md] | wc -l)
echo Total all problems: $(ls --ignore={"*env","*.gitignore","*.md","*.sh"} | wc -l)