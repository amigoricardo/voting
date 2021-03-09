from itertools import combinations
import pandas as pd

def ranked(preferences):
    happiness = pd.DataFrame({'preferred': preferences[0]}, columns=['preferred']+preferences[0]).set_index('preferred')
    pairs = combinations(preferences[0], 2)
    for pair in pairs:
        prefers_first_over_second = sum([1 for p in preferences if p.index(pair[0]) < p.index(pair[1])])
        happiness[pair[0]][pair[1]] = prefers_first_over_second
        happiness[pair[1]][pair[0]] = len(preferences) - prefers_first_over_second
    return happiness