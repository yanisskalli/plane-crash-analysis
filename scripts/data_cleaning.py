import pandas as pd

# Chargement du csv dans le dataframe 
df = pd.read_csv("..\data\plane_crash.csv")

# Standardisation des noms de colonne, notamment le traitement des espaces 
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Conversion des dates et suppression des lignes sans dates
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df.dropna(subset=['date'])

# Conversion des colonnes numériques 
cols_to_clean = ['aboard', 'fatalities'] # Définition des colonnes à traiter dans cols_to_clean
for col in cols_to_clean :
    df[col] = pd.to_numeric(df[col], errors='coerce')
    df[col] = df[col].fillna(0) # On remplace les valeurs nul par 0.

# Suppression des lignes incomplètes dans les colonnes operator, location et summary
df = df.dropna(subset=['operator', 'location', 'summary'])


# Sauvegarde des données nettoyés
df.to_csv("../data/plane_crash_clean.csv", index=False)
 
print("Nettoyage réussi")

