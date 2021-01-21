#!/bin/bash
shopt -s extglob

for i in {1..24}
do
	mkdir "../Day$i"
	git remote add -f "day$i" "git@github.com:rcs-tringuyen/tryhackme_christmas_day$i"
	git merge "day$i/main" --allow-unrelated-histories -m "yes"
	git mv ../!(Day*) "../Day$i"
	git add .
	git commit -m "Add day$i"
done