import random
from copy import deepcopy


def get_random_preferences(
    n_electors, 
    candidates_name, 
    candidates_notability=None, 
    candidates_rejection=None):
    """
    Generates random rankings of preference for each elector
    Args:
        n_electors (int): number of electors
        candidates_name (string array): array of candidates names 
        candidates_notability (float array): array of Notability score. 
            It dictates how known is a candidate, for either good or bad reasons.
        candidates_rejection (float array): array of Rejection level. Neutral by default.
    """
    preferences = []
    if not candidates_rejection:
        candidates_rejection = [1 for _ in candidates_name]
    for _ in range(n_electors):
        cnam = deepcopy(candidates_name)
        cnot = deepcopy(candidates_notability)
        prefs = []
        for _ in candidates_name:
            cand = random.choices(cnam, cnot)[0]
            i = cnam.index(cand)
            cnam.pop(i)
            cnot.pop(i)
            prefs.append(
                [
                    cand, 
                    random.choices(
                        ['+', '-'], 
                        [1, candidates_rejection[candidates_name.index(cand)]]
                    )[0]
                ]
            )
        positive_prefs = [c[0] for c in prefs if c[1]=='+']
        negative_prefs = [c[0] for c in prefs if c[1]=='-']
        full_preferences = positive_prefs + list(reversed(negative_prefs))
        preferences.append(full_preferences)
    return preferences