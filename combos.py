def combo_multi_matches(matches):
    odds = 1.0
    explanation = []
    for m in matches[:3]:
        odds *= 1.45
        explanation.append({
            "match": m["match"],
            "pick": "Doble oportunidad local",
            "reason": f"xG {m['home_xg']} vs {m['away_xg']} | ELO +{m['elo_diff']}"
        })
    return {"type":"COMBINADA MULTI","odds":round(odds,2),"explanation":explanation}

def combo_same_match(match):
    return {
        "type":"COMBINADA DEL PARTIDO",
        "match":match["match"],
        "odds":2.15,
        "picks":[
            ("Doble oportunidad local","Alta probabilidad"),
            ("Under 3.5 goles","Ritmo bajo"),
            ("Ambos NO anotan","xG visitante bajo")
        ]
    }
