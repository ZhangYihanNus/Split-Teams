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
                           int(row[2]) if (len(row) > 2 and row[2] != '') else 10])
    return people

def create_teams(people, num):
    teams = {f"Team {i+1}": [] for i in range(num)}  # Initialize teams
    team_count = len(people)

    # randomize the order and sort again
    random.shuffle(people)
    people.sort(key=lambda x:x[2])
    
    # # rearrange people
    # rearranged = {}
    # for person in people:
    #     if (person[2] in rearranged.keys()): 
    #         rearranged[person[2]].append(person)
    #     else:
    #         rearranged[person[2]] = [person]
    # # print(rearranged)
    
    for i, person in enumerate(people):
        team_num = i % num  # Distribute people evenly across teams
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
    teams = create_teams(people, 8)
    print_teams(teams)
