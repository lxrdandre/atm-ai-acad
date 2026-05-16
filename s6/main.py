import json

with open("monsters.json", "r") as f:
    try:
        monsters = json.load(f)
    except FileNotFoundError:
        print("Error: monsters.json not found")
        exit(1)

def calculate_total_score(scores):
    """
    Calculate the total score of a monster.
    If a monster has no scores, total score = 0.
    """
    return sum(scores) if scores else 0

def calculate_average_score(scores):
    """
    Calculate the average round score.
    If a monster has no scores, average = 0.
    """
    return sum(scores) / len(scores) if scores else 0

def find_best_round(scores):
    """
    Find the best round score.
    If a monster has no scores, best round = None.
    """
    return max(scores) if scores else None

def find_worst_round(scores):
    """
    Find the worst round score.
    If a monster has no scores, worst round = None.
    """
    return min(scores) if scores else None

def assign_rank_label(total_score):
    """
    Assign a rank based on total score:
    Legend if total >= 40, Elite if total >= 25, Fighter if total >= 10,
    Rookie if total >= 0, Fallen if total < 0.
    """
    if total_score >= 40:
        return "Legend"
    elif total_score >= 25:
        return "Elite"
    elif total_score >= 10:
        return "Fighter"
    elif total_score >= 0:
        return "Rookie"
    else:
        return "Fallen"

def check_stability(scores):
    """
    Decide whether the monster is "stable" or "unstable".
    "Stable" if no negative round scores.
    "Unstable" if at least one round score is negative.
    """
    return "Stable" if all(score >= 0 for score in scores) else "Unstable"

def build_processed_monster_summary(monster):
    """
    Build a processed monster dict combining all calculated metrics.
    Output structure for a monster:
    {
        "name": "...",
        "element": "...",
        "total": ...,
        "average": ...,
        "best": ...,
        "worst": ...,
        "rank": "...",
        "stability": "..."
    }
    """
    return {
        "name": monster["name"],
        "element": monster["element"],
        "total": calculate_total_score(monster["scores"]),
        "average": calculate_average_score(monster["scores"]),
        "best": find_best_round(monster["scores"]),
        "worst": find_worst_round(monster["scores"]),
        "rank": assign_rank_label(calculate_total_score(monster["scores"])),
        "stability": check_stability(monster["scores"])
    }

def find_monsters_by_rank(processed_monsters, target_rank):
    """
    Return a list of monster names with that target rank.
    """
    return [monster["name"] for monster in processed_monsters if monster["rank"] == target_rank]

def find_element_team(processed_monsters, target_element):
    """
    Return all monster names of that target element.
    """
    return [monster["name"] for monster in processed_monsters if monster["element"] == target_element]

def print_tournament_report(processed_monsters):
    """
    Print all processed monster summaries.
    Also print:
    - total number of monsters
    - average tournament total score
    - highest scoring monster
    - lowest scoring monster
    - how many monsters are in each rank
    - how many are stable vs unstable
    - all monsters of a chosen element
    - all monsters whose best round was at least 20
    """
    print("\n")
    print("Tournament Report")
    print("Total number of monsters: ", len(processed_monsters))
    print("Average tournament total score: ", sum([monster["total"] for monster in processed_monsters]) / len(processed_monsters))
    print("Highest scoring monster: ", max([monster["total"] for monster in processed_monsters]))
    print("Lowest scoring monster: ", min([monster["total"] for monster in processed_monsters]))
    print("Number of monsters in each rank: ", {rank: len(find_monsters_by_rank(processed_monsters, rank)) for rank in ["Legend", "Elite", "Fighter", "Rookie", "Fallen"]})
    print("Number of stable vs unstable monsters: ", {stability: len([monster for monster in processed_monsters if monster["stability"] == stability]) for stability in ["Stable", "Unstable"]})
    print("All monsters of a chosen element: ", {element: find_element_team(processed_monsters, element) for element in ["fire", "water", "earth", "air", "dark", "lightning"]})
    print("All monsters whose best round was at least 20: ", [monster["name"] for monster in processed_monsters if monster["best"] is not None and monster["best"] >= 20])
    print("\n")

def main():
    # TODO: loop over all `monsters` and process them into a new list
    processed_monsters = []
    for monster in monsters:
        processed_monsters.append(build_processed_monster_summary(monster))
    # TODO: generate the tournament report and print
    print_tournament_report(processed_monsters)

if __name__ == "__main__":
    main()
