# Project 1 - Language Poll Analyser
# Author: Emre Nazli

import csv

counts = {}
total = 0

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        language = row["language"]

        if language in counts:
            counts[language] += 1
        else:
            counts[language] = 1

        total += 1

sorted_languages = sorted(
    counts.items(),
    key=lambda x: x[1],
    reverse=True
)

print("=== Language Popularity Report ===")

for i, (language, count) in enumerate(sorted_languages, start=1):
    print(f"{i}. {language}: {count} students")

print(f"\nTotal responses: {total}")
