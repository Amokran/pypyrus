import json
import translation_manager
import metadata

def load_translations(lang,json_file):
    """Cargar traducciones desde un archivo JSON."""
    with open(json_file, "r", encoding="utf-8") as f:
        translations = json.load(f)
    return translations.get(lang, translations["en"])

def run_example():

    # Legacy usage. Won't use.
    print("0. Loading translations from JSON file (legacy, won't use)")
    lang = "en"  # Supongamos que el usuario seleccionó español
    translations = None
    try:
        translations = load_translations(lang,"resources/sample/translations.json")
    except Exception as e:
        print(f"Error loading translations: {e}")
    
    if translations:
        print(translations["GREETINGS"])
        print(translations["SETTINGS"]) 
        print(translations["LOGIN_FAILED"]) 
    
    foo = input("Press intro to continue...")
    print(".......")
    print()

    # Current usage (sample path). Loads all data from any translation JSON  in sample path
    print("1. Loading translations from JSON file (current usage)")
    SAMPLE_TEXTS = None
    try:
        SAMPLE_TEXTS = translation_manager.TranslationManager( 
            translations_path="resources/sample",
            translations_file=None,
            active_lang="en"
            )
    except Exception as e:
        print(f"Error loading translations: {e}")

    if SAMPLE_TEXTS:       
        username = input("Enter your name >> ")
        print(SAMPLE_TEXTS.translate("SPECIAL_GREETINGS", name=username)) # Pass var name to be replaced inside SPECIAL_GREETINGS
        print(SAMPLE_TEXTS.translate("SETTINGS"))
    
    foo = input("Press intro to continue...")
    print(".......")
    print()
    
    print("2. Loading metadatas from JSON file (current usage)")
    SAMPLE_TEXTS_META = None
    try:
        SAMPLE_TEXTS_META = SAMPLE_TEXTS.get_metadata()
    except Exception as e:
        print(f"Error loading metadata: {e}")

    if SAMPLE_TEXTS_META:
        print("metadata for [GREETINGS]:")
        print(SAMPLE_TEXTS_META["GREETINGS"])
    
    foo = input("Press intro to continue...")
    print(".......")
    print()

    print("3. Loading ALl translations from JSON file and printing as they come (useful to see internal structure of the dictionary)")
    print(SAMPLE_TEXTS.get_translations())
    foo = input("Press intro to continue...")
    print(".......")
    print()


    print("4. Loading larger translations from TXT file (current usage)")
    SAMPLE_QUOTES = None
    try:
        SAMPLE_QUOTES = translation_manager.TranslationManager( 
            translations_path="resources/texts",
            translations_file=None,
            active_lang="en"
            )
    except Exception as e:
        print(f"Error loading translations: {e}")

    if SAMPLE_QUOTES:           
        print(SAMPLE_QUOTES.load_text_file("waltari")) # print quotes from en_waltari.txt
        print()
        
        SAMPLE_QUOTES.set_active_language("es")         # change language to Spanish
        
        print(SAMPLE_QUOTES.load_text_file("waltari"))  # print quotes from es_waltari.txt
        print()

if __name__ == "__main__":
    run_example()
