# Project 2 - Grade Tracker
# Author: Emre Nazli

import csv

scores = []
highest_name = ""
highest_score = 0
lowest_name = ""
lowest_score = 100

grades = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "F": 0
}

with open("grades.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["name"]
        score = float(row["score"])

        scores.append(score)

        if score > highest_score:
            highest_score = score
            highest_name = name

        if score < lowest_score:
            lowest_score = score
            lowest_name = name

        if score >= 90:
            grades["A"] += 1
        elif score >= 80:
            grades["B"] += 1
        elif score >= 70:
            grades["C"] += 1
        elif score >= 60:
            grades["D"] += 1
        else:
            grades["F"] += 1

average = sum(scores) / len(scores)

print("=== Grade Summary ===")
print(f"Total students: {len(scores)}")
print(f"Average score: {average:.1f}")
print(f"Highest score: {highest_name} ({highest_score})")
print(f"Lowest score: {lowest_name} ({lowest_score})")

print("\nGrade distribution:")
for grade, count in grades.items():
    print(f"{grade}: {count}")
