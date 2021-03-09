def plurality(preferences):
    """
    The candidate ranked as the 1st preference more times wins
    """
    results = {}
    candidates = preferences[0]
    electors_vote = [p[0] for p in preferences]
    for c in candidates:
        results[c] = electors_vote.count(c)
    return results