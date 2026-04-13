import json
import sys

email = sys.argv[1]

with open('linkedin_users.json') as f:
    data = json.load(f)

user = next((u for u in data["users"] if u["email"] == email), None)

if not user:
    print("User not found")
    sys.exit(1)

score = 0

if user["connections"] >= 500:
    score += 2
if user["experience"] >= 3:
    score += 2
if user["skills"] >= 5:
    score += 1
if user["certifications"] >= 1:
    score += 1
if user["activity"] == "high":
    score += 2

print(score)
