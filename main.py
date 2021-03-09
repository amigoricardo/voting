from voting.preferences import random_preferences
from voting.systems import plurality, majoritarian

preferences = random_preferences.get_random_preferences(
        1000, 
        ['Lula', 'Bolso', 'Ciro', 'Marina', 'Amoedo'],
        [30, 30, 5, 5, 1]
    )

results = majoritarian.majoritarian(preferences)
print(results)