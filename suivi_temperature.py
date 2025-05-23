import csv

def lire_donnees_csv(fichier):
    jours = []
    temperatures = []
    try:
        with open(fichier, mode='r', newline='', encoding='utf-8') as f:
            lecteur = csv.DictReader(f)
            for ligne in lecteur:
                jour = ligne.get('JOUR')
                temp_str = ligne.get('TEMPERATURE')
                try:
                    temperature = float(temp_str)
                    jours.append(jour)
                    temperatures.append(temperature)
                except (ValueError, TypeError):
                    print(f"⚠️ Température invalide ignorée : {temp_str}")
    except FileNotFoundError:
        print(f"❌ Fichier introuvable : {fichier}")
    return jours, temperatures

def calcul_statistiques(temperatures):
    if not temperatures:
        return None, None, None
    moyenne = sum(temperatures) / len(temperatures)
    return moyenne, max(temperatures), min(temperatures)

def afficher_statistiques(moyenne, maximum, minimum):
    if moyenne is None:
        print("Aucune donnée disponible pour les statistiques.")
    else:
        print("\n📊 STATISTIQUES")
        print(f"→ Moyenne : {moyenne:.2f}°C")
        print(f"→ Maximum : {maximum:.2f}°C")
        print(f"→ Minimum : {minimum:.2f}°C")

def detecter_surchauffe(jours, temperatures, seuil):
    print(f"\n🌡️ Jours avec surchauffe (>{seuil}°C) :")
    alerte = False
    for jour, temp in zip(jours, temperatures):
        if temp > seuil:
            print(f"⚠️ {jour} : {temp}°C")
            alerte = True
    if not alerte:
        print("✅ Aucune surchauffe détectée.")

def demander_seuil():
    while True:
        saisie = input("👉 Entrez le seuil de surchauffe en °C (ex : 30) : ")
        try:
            return float(saisie)
        except ValueError:
            print(" Veuillez entrer un nombre valide.")

# --- CORPS DU PROGRAMME PRINCIPAL ---
fichier = 'temperatures.csv'
jours, temperatures = lire_donnees_csv(fichier)

if not jours or not temperatures:
    print(" Erreur : données insuffisantes pour l’analyse.")
else:
    moyenne, maximum, minimum = calcul_statistiques(temperatures)
    afficher_statistiques(moyenne, maximum, minimum)

    seuil = demander_seuil()
    detecter_surchauffe(jours, temperatures, seuil)
