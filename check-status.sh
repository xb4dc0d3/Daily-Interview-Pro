#!/usr/bin/bash
all=$(ls --ignore={"*env","*.gitignore","*.md","*.sh"} | wc -l)
solved=$(git ls-files --cached | wc -l)
echo Problems solved: $solved
echo Problems not solved : $(($all-$solved))
echo Total all problems: $all
