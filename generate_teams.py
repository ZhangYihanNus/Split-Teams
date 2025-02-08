#!/usr/bin/env python3

import csv
import sys
import random
from math import ceil

def read_csv(file_name):
    people = []
    
    with open(file_name, newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip header row if present
        for row in csvreader:
            # If row has fewer than 3 columns, fill in empty strings for missing columns
            people.append([row[0] if len(row) > 0 else '',
                           row[1] if len(row) > 1 else '',
                           row[2] if len(row) > 2 else ''])
    return people

def create_teams(people):
    teams = {f"Team {i+1}": [] for i in range(8)}  # Initialize teams
    team_count = len(people)

    # place people that needs to be separated to start of list
    separate_group = [person for person in people if person[2] == "1"]
    non_separate_group = [person for person in people if person[2] != "1"]
    random.shuffle(separate_group)
    random.shuffle(non_separate_group)
    rearranged = separate_group + non_separate_group
    
    for i, person in enumerate(rearranged):
        team_num = i % 8  # Distribute people evenly across teams
        team_name = f"Team {team_num + 1}"
        teams[team_name].append(person)
    
    return teams

def print_teams(teams):
    for team_name, members in teams.items():
        print(f"{team_name}:")
        print("number of people: " + f"{len(members)}")
        if not members:
            print("  No members")
        for member in members:
            # Print each member's information
            print(f'{member[2]:<2}', end='')
            print(" | ", end='')
            print(f'{member[1]:<8}', end='')
            print(" | ", end='')
            print(f'{member[0]}')
        print()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <csv_file>")
        sys.exit(1)

    file_name = sys.argv[1]
    people = read_csv(file_name)
    teams = create_teams(people)
    print_teams(teams)
