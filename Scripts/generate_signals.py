import pandas as pd

# Exemple de génération de signaux (à adapter selon votre logique)
signals = [
    {"timestamp": "2024-07-17 09:00:00", "signal": "Buy"},
    {"timestamp": "2024-07-17 13:00:00", "signal": "Sell"},
    # Ajoutez d'autres signaux ici
]

# Créer un DataFrame pandas pour stocker les signaux
df = pd.DataFrame(signals)

# Chemin où sauvegarder le fichier CSV (remplacez avec votre chemin complet si nécessaire)
csv_file_path = '../data/signals.csv'

# Optionnel : sauvegarder les signaux dans un fichier CSV
df.to_csv(csv_file_path, index=False)

print(f"Signaux exportés vers '{csv_file_path}'")
