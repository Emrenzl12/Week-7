# starter.py - Event Log Reporter
# Project 3 | Intermediate | 35-45 minutes

import csv

room_counts = {}
type_counts = {}
day_attendees = {}
all_events = []

with open("bookings.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        room = row["room"]
        event_type = row["event_type"]
        date = row["date"]
        attendees = int(row["attendees"])

        room_counts[room] = room_counts.get(room, 0) + 1
        type_counts[event_type] = type_counts.get(event_type, 0) + 1
        day_attendees[date] = day_attendees.get(date, 0) + attendees

        all_events.append(row)

busiest_day = max(day_attendees, key=day_attendees.get)
busiest_count = day_attendees[busiest_day]

large_events = [
    row for row in all_events
    if int(row["attendees"]) > 50
]

large_events_sorted = sorted(
    large_events,
    key=lambda row: int(row["attendees"]),
    reverse=True
)

print("=== Community Centre Booking Report ===")

print("\nBookings by Room:")
for room in sorted(room_counts):
    print(f"  {room}: {room_counts[room]} events")

print("\nBookings by Event Type:")
for event_type in sorted(type_counts):
    print(f"  {event_type}: {type_counts[event_type]} events")

print(f"\nBusiest Day: {busiest_day} ({busiest_count} total attendees)")

print("\nLarge Events (> 50 attendees):")
for event in large_events_sorted:
    print(
        f"  {event['date']} | {event['room']} | "
        f"{event['event_type']} | {event['attendees']} attendees"
    )
