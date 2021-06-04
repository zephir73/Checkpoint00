#!/bin/sh

awk -F "|" '{print$7}' evil_corp_council_members.csv >> ssh_infected_key.txt

