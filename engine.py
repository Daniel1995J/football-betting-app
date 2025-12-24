def analyze_match(match):
    home, away = match.split(" vs ")
    return {
        "match": match,
        "home": home,
        "away": away,
        "home_xg": 1.75,
        "away_xg": 0.7,
        "home_win_prob": 0.62,
        "elo_diff": 115,
        "league_weight": 0.95
    }
