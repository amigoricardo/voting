import random
from copy import deepcopy


def get_random_preferences(n_electors, candidates_names, candidates_notabilities=None):
    """
    Generates random rankings of preference for each elector
    Args:
        n_electors (int): number of electors
        candidates_names (string array): array of candidates names 
        candidates_notabilities (float array): array of Notability score. 
            It dictates how known is a candidate, for either good or bad reasons.
    """
    preferences = []
    for _ in range(n_electors):
        cnam = deepcopy(candidates_names)
        cnot = deepcopy(candidates_notabilities)
        prefs = []
        for _ in candidates_names:
            cand = random.choices(cnam, cnot)[0]
            i = cnam.index(cand)
            cnam.pop(i)
            cnot.pop(i)
            prefs.append([cand, random.choice(['+', '-'])])
        positive_prefs = [c[0] for c in prefs if c[1]=='+']
        negative_prefs = [c[0] for c in prefs if c[1]=='-']
        full_preferences = positive_prefs + list(reversed(negative_prefs))
        preferences.append(full_preferences)
    return preferences