import json

nome_file = "tv_shows_and_movies_sample.json"
with open(nome_file, "r") as file:
    stringa_json = file.read()
oggetto_python = json.loads(stringa_json)

while True:
    print("\nScegli un'opzione:")
    print("1 - Cerca film per titolo")
    print("2 - Ordina film per rating (decrescente)")
    print("3 - Filtra film per genere")
    print("4 - Filtra film per produttore")
    print("0 - Esci")
    print("non c'è più la mafia di una volta -tony pitony")

    scelta = input("Inserisci il numero dell'opzione desiderata: ")

    if scelta == "0":
        print("\nUscita dal programma in corso... ")
        break

    elif scelta == "1":
        titolo_cercato = input("\nInserisci il titolo del film:\n")
        trovato = False
        for elem in oggetto_python:
            if elem["titolo"].lower() == titolo_cercato.lower():
                print("\nFilm trovato:")
                print(f"Titolo: {elem['titolo']}")
                print(f"Produttore: {elem['produttore']}")
                print(f"Anno di produzione: {elem['data_produzione']}")
                print(f"Genere: {elem['genere']}")
                print(f"Durata: {elem['durata']} minuti")
                print(f"Rating: {elem['rating_imdb']}")
                trovato = True
                break
        if not trovato:
            print("\nTitolo non trovato. Riprova.")

    elif scelta == "2":
        ordinati = sorted(oggetto_python, key=lambda x: x["rating_imdb"], reverse=True)
        print("\nFilm ordinati per rating (dal più alto):")
        for film in ordinati:
            print(f"{film['titolo']} - Rating: {film['rating_imdb']}")

    elif scelta == "3":
        genere_cercato = input("\nInserisci il genere da cercare (es. Drammatico):\n").lower()
        risultati = []
        for film in oggetto_python:
            generi = [g.strip().lower() for g in film["genere"].split(",")]
            if genere_cercato in generi:
                risultati.append(film)
        if risultati:
            print(f"\nFilm che includono il genere '{genere_cercato}':")
            for film in risultati:
                print(f"{film['titolo']} - Genere: {film['genere']}")
        else:
            print("\nNessun film trovato con quel genere.")

    elif scelta == "4":
        produttore_cercato = input("\nInserisci il nome del produttore:\n").lower()
        risultati = [film for film in oggetto_python if film["produttore"].lower() == produttore_cercato]
        if risultati:
            print(f"\nFilm prodotti da '{produttore_cercato}':")
            for film in risultati:
                print(f"{film['titolo']} - Anno: {film['data_produzione']}")
        else:
            print("\nNessun film trovato con quel produttore.")

    else:
        print("\nScelta non valida. Riprova.")
