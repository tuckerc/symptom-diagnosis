#!/usr/bin/env python3

import csv


def get_symptom():
    print("\nPick one of the following options that best matches your symptom:")
    print("1. Abdominal pain, long-term")
    print("2. Cold and flu")
    print("3. Tooth problems")
    return input()


def diagnose(file):
    with open(file) as file:
        reader = csv.reader(file, delimiter="#")
        next_row = 1
        current_row = 0
        for row in reader:
            current_row += 1
            if next_row == current_row:
                answer = input(f"{row[0]} ")
                while answer.lower() not in ("y", "yes", "n", "no"):
                    answer = input(f"\n{row[0]}")
                if answer == "y":
                    if str(row[1]).isdigit():
                        next_row = current_row + int(row[1])
                    else:
                        print(f"\nDiagnosis: {row[1]}")
                        print(f"Treatment: {row[3]}")
                else:
                    if len(row) > 2:
                        next_row = current_row + int(row[2])


print("We apologize, but the doctor is only treating high priority patients during the pandemic. Use this tool to "
      "diagnose your condition, and schedule an appointment only as necessary.")

symptom = get_symptom()

while symptom not in ("1", "2", "3"):
    get_symptom()

if symptom == "1":
    diagnose("abdominal_pain_long_term.csv")
elif symptom == "2":
    diagnose("cold_and_flu.csv")
elif symptom == "3":
    diagnose("tooth_problems.csv")
