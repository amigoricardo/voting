from voting.preferences import random_preferences
from voting.systems import plurality, majoritarian, procon, ranked

preferences = random_preferences.get_random_preferences(
        10000, 
        ['Andreia', 'Beatriz', 'Carla', 'Daniela', 'Elisa'],
        [1, 100, 5, 100, 5],
        [4, 2, 0.5, 2, 0.5]
    )
# preferences = random_preferences.get_random_preferences(
#     10000, 
#     ['Andreia', 'Beatriz', 'Carla', 'Daniela', 'Elisa', 'F', 'G', 'H', 'I', 'J'],
#     [1, 100, 5, 100, 5, 0.01, 0.01, 0.01, 0.01, 0.01],
#     [4, 2, 0.5, 2, 0.5, 1, 1, 1, 1, 1]
# )

print('Votação normal com primeiro e segundo turno:')
major_results = majoritarian.majoritarian(preferences)
print(major_results)
print('--------------------------------------------')

print('Novo sistema:')
procon_results = procon.procon(preferences)
print(procon_results)
print('--------------------------------------------')

print('Preferências em pares de candidatos:')
ranked_results = ranked.ranked(preferences)
print(ranked_results)
print('--------------------------------------------')