#!/bin/sh

rm evil_corp_council_members.csv 
sed -n -e '/215/,/222/p' log_terminal_CDG.csv | tail -n 7 >> evil_corp_council_members.csv
