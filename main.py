from voting.preferences import random_preferences
from voting.systems import plurality, majoritarian, procon, ranked
import pprint

preferences = random_preferences.get_random_preferences(
        1000, 
        ['Lula', 'Bolso', 'Ciro', 'Marina', 'Amoedo'],
        [30, 30, 5, 5, 1],
        [30, 30, 0.5, 0.5, 4]
    )
# pprint.pprint(preferences)

major_results = majoritarian.majoritarian(preferences)
print(major_results)

procon_results = procon.procon(preferences)
print(procon_results)

ranked_results = ranked.ranked(preferences)
print(ranked_results)