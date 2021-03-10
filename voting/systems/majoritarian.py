from .plurality import plurality
import numpy as np


def majoritarian(preferences):
    """
    Extends plurality to a majoritarian system by performing a second round with the top two candidates
    """
    # 1st Round
    first_round_results = plurality(preferences)
    frr = np.array(list(first_round_results.items()), dtype=[('name', 'U10'), ('votes', int)])
    frr = np.sort(frr, order='votes')[::-1]

    # 2nd Round with the top two candidates
    cand_first = frr[0][0]
    cand_second = frr[1][0]
    prefer_cand_first = sum([1 for p in preferences if p.index(cand_first) < p.index(cand_second)])
    prefer_cand_second = len(preferences) - prefer_cand_first
    
    second_round_results = first_round_results
    second_round_results[cand_first] = [second_round_results[cand_first], prefer_cand_first]
    second_round_results[cand_second] = [second_round_results[cand_second], prefer_cand_second]

    return second_round_results