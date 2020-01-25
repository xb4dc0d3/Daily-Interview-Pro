#!/usr/bin/bash
echo Problems still not solved\t: $(git ls-files --exclude *[^.md] | wc -l)
echo Total all problems\t: $(ls --ignore={"*env","*.gitignore","*.md","*.sh"} | wc -l)