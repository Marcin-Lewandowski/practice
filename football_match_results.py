import random

# Team strengths
team_strengths = {
    "Brazil": 95,
    "Poland": 70,
    "Argentina": 80,
    "Germany": 85,
    "Spain": 82,
    "Italy": 89,
    "France": 90,
    "Denmark": 67,
    "Russia": 65,
    "USA": 80,
}

# List of teams
teams = list(team_strengths.keys())

# Function to simulate a match
def match_result(strength1, strength2):
    total_strength = strength1 + strength2
    probability_team1 = strength1 / total_strength
    result_team1 = random.random() < probability_team1
    result_team2 = not result_team1
    return result_team1, result_team2

# Generate match results
match_results = {}
for i, team1 in enumerate(teams):
    for team2 in teams[i+1:]:
        strength1 = team_strengths[team1]
        strength2 = team_strengths[team2]
        result_team1, result_team2 = match_result(strength1, strength2)
        match = f"{team1} vs {team2}"
        # Check if the match result or its reverse already exists in the dictionary
        if match not in match_results and f"{team2} vs {team1}" not in match_results:
            match_results[match] = (result_team1, result_team2)

# Display results
for match, result in match_results.items():
    team1, team2 = match.split(" vs ")
    result_team1, result_team2 = result
    if result_team1:
        print(f"{team1} {random.randint(1, 4)} - {random.randint(0, 3)} {team2}")
    else:
        print(f"{team1} {random.randint(0, 3)} - {random.randint(1, 4)} {team2}")
