def procon(preferences):
    """
    Each elector has one vote in favour and one against. 
    Final candidate score is given by the subtraction of votes against from the votes in favour.
    """
    results = {}
    candidates = preferences[0]
    votes_favour = [p[0] for p in preferences]
    votes_against = [p[-1] for p in preferences]
    for c in candidates:
        results[c] = votes_favour.count(c) - votes_against.count(c)
    return results