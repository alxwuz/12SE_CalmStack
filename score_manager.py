import json
import os

score_file = "scores.json"

def load_scores():
    if not os.path.exists(score_file) or os.path.getsize(score_file) == 0:
        return {}
    with open(score_file, "r") as f:
        return json.load(f)

def save_scores(scores):
    with open(score_file, "w") as f:
        json.dump(scores, f, indent=2)

def update_user_score(username, new_score):
    scores = load_scores()
    
    if username not in scores or new_score > scores[username]:
        scores[username] = new_score
        save_scores(scores)
        return True
    return False

def get_user_high_score(username):
    scores = load_scores()
    return scores.get(username, 0)