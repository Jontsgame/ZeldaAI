import wikipedia

# Name der Ausgabedatei
OUTPUT_FILE = "raw_data.txt"
# Suchbegriff für den Wikipedia-Artikel
SEARCH_TERM = "The Legend of Zelda: Breath of the Wild"
# Sprache einstellen (Deutsch ist 'de', Englisch ist 'en')
wikipedia.set_lang("de") 

try:
    # 1. Artikel suchen und abrufen
    # Der erste Treffer der Suche wird genommen. Man könnte auch .page("Genauer Titel") verwenden.
    page = wikipedia.page(SEARCH_TERM, auto_suggest=False)
    
    # 2. Titel und Text extrahieren
    title = page.title
    content = page.content # Dies ist der reine Text des Artikels
    
    # 3. Speichern in der Datei "raw_data.txt"
    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        f.write(f"=== ARTIKEL TITEL: {title} ===\n\n")
        f.write(content)
        f.write("\n\n--- ENDE DES ARTIKELS ---\n\n")
    
    print(f"Artikel '{title}' wurde erfolgreich in '{OUTPUT_FILE}' gespeichert.")

except wikipedia.exceptions.PageError:
    print(f"Fehler: Der Artikel zum Suchbegriff '{SEARCH_TERM}' wurde nicht gefunden.")
except wikipedia.exceptions.DisambiguationError as e:
    print(f"Fehler: Der Suchbegriff ist mehrdeutig. Mögliche Optionen: {e.options}")
except Exception as e:
    print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")