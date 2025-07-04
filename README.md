# pypyrus
A python module to help developers getting texts and translations from files.

## Current state of things
This is an early version, and possibly won't accept pull requests at this stage.
Anyway, if you're interested in contributing, please open an issue and we can discuss it.
At this stage, it should be used in a development environment only.

## Purpose
The purpose of this module is to help developers getting texts and translations from files.
I created this as a helper module for my own projects, since I was lacking a proper separation of code and texts.
Besides, I figured out that I could use it to help me with translations, so I decided to make it a separate module.

## Ethics and values
This module is designed to be used in a responsible way. You know what I mean.
In case you don't, it's easy: don't use this to harm the weak and the helpless. Even if it's people you don't like.
In any case, try to use it for good, and to help others.

## Installation
At the moment, the module is not available on PyPI, so you have to install it from the source.

## Requirements
Python 3.10 or higher.
Not really tested on lower versions, but it should work.

## Tests and examples
You can run tests using unittest by simply doing:
````bash:
python -m unittest discover
````
You can also run the example script `example_main.py` to see how to use the module.

## Texts and translations
The module is designed to work with texts and translations in JSON files.
The idea is for you to create a folder with the texts and translations, and then use the module to load them.
The rule is that the folder should only contain a file called `translations.json` with the texts in it, and a file called `metadata.json` with the metadata for each text.
Nonetheless, they might be managed separately, although they should share the same keys, so one might use the same key for both metadata and translations of each text.

The `translations.json` file should contain the texts in each of the languages you want to support.:
```json
{
    "en": {
        "GREETINGS": "Hello, World!",
        "SPECIAL_GREETINGS": "Hello {name}!",
        "SETTINGS": "Settings",
        "LOGIN_FAILED": "Login failed. Please try again."
        
    },
    "es": {
        "GREETINGS": "Hola, Mundo!",
        "SPECIAL_GREETINGS": "Hola {name}!",
        "SETTINGS": "Configuración",
        "LOGIN_FAILED": "Error al iniciar sesión. Por favor, inténtalo de nuevo."
    }
}
```
Those texts have support for variables, so you can use them in the texts (see usage below).
We'll see the metadata file later.

## Example of translation folder structure
Please notice that there are txt files in the folder, mean for larger texts (see usage below).
Also there are metadata files, which are not mandatory, but highly recommended (see usage below).

````plaintext:
translations/
├── ui-texts/
│   ├── translations.json
│   ├── metadata.json
│   ├── en_credits.txt
│   └── es_credits.txt
│
├── sample-texts/
│   ├── translations.json
│   ├── metadata.json
│   └── en_intro.txt
│
└── quotes/
    ├── en_waltari.txt
    └── es_waltari.txt
````
    
## Basic usage for getting texts and translations
This module is designed to be used in a very simple way.
Please note that can be used as a mere text manager, even if you don't need translations.
You could only have one lenguage key in the translations file, and use it as a text manager for a single language.
That will help you to keep your texts separated from your code, and will help you to manage them in a more efficient way.

````python
from pypyrus import translation_manager as TRM

    # load the translation manager into an object (could and probably should be a constant)
    # Since you should only have a single translations file in the folder, there's no need for specifying it in translation_file parameter. 
    # This is kind of a legacy feature, but I left it there for now.
    try:
        SAMPLE_TEXTS = TRM.TranslationManager( 
            translations_path="resources/sample", #the path where the translations are stored
            translations_file=None, # [optional] the name of the translations file (without the .json extension), but I advise to use the default one** 
            active_lang="en" # [optional] the language to be used by default. If not specified, it will use english (en) as default.
            )
    except Exception as e_translation_manager:
        print(f"Error loading translations: {e_translation_manager}")   

    # Now you can use the translation manager to get the texts and translations.
    print(SAMPLE_TEXTS.translate("SPECIAL_GREETINGS", name="Pepe")) # Pass var name to be replaced inside SPECIAL_GREETINGS
    print(SAMPLE_TEXTS.translate("SETTINGS"))
````    

## Metadata
The `metadata.json` file should live in the same folder as the translations file, and it is highly recommended to use the same keys as the translations file.
The metadata file is not mandatory, but it is recommended to use it, for scalability and maintainability purposes, should project and texts grow in size and complexity.
See an example:

````json:
{
    "GREETINGS": {
      "type": "generic text",
      "author": "@dev",
      "source": "manual",
      "added" : "2025-04-18",
      "tags": {
        "en": ["greetings", ""],
        "es": ["saludos", ""]
      },
      "context_tags": {
        "en": [""],
        "es": [""]
      }
    },
    "SPECIAL_GREETINGS": {
      "type": "generic text",
      "author": "@dev",
      "source": "manual",
      "added" : "2025-04-18",
      "tags": {
        "en": ["greetings", "special"],
        "es": ["saludos", "especial"]
      },
      "context_tags": {
        "en": [""],
        "es": [""]
      }
    }
  }
````

The metadata file is used to store information about the texts, such as the author, the source, the date added, and the tags.
You might think it is of little interest, but it is useful when using text quotes from other sources, such as books, articles, papers, etc.
It is also useful to keep track of the texts you have in your project, and to be able to search for them later.
Lets see a more advanced verion of the metadata file node:

````json:
{
  "TURING_PAPER": {
    "type": "academic_article",
    "author": "Alan Turing",
    "source": "Manual translation based on public domain",
    "tags": {
      "en": ["AI", "computation", "philosophy"],
      "es": ["IA", "cómputo", "filosofía"]
    },
    "context_tags": {
      "en": ["turing_test", "classic_papers"],
      "es": ["test_de_turing", "artículos_clásicos"]
    },
    "article": {
      "en": {
        "title": "Computing Machinery and Intelligence",
        "journal": "Mind",
        "volume": 59,
        "issue": 236,
        "year": 1950,
        "pages": "433–460",
        "doi": "10.1093/mind/LIX.236.433"
      },
      "es": {
        "title": "¿Pueden pensar las máquinas?",
        "journal": "Revista Iberoamericana de Inteligencia Artificial",
        "volume": 3,
        "issue": 9,
        "year": 2000,
        "pages": "7–21",
        "translator": "Juan Pérez"
      }
    }
  }
}
````
The metadata file is used to store information about the texts, such as the author, the source, the date added, and the tags.

## Metadata usage
We'll see an example of how to use the metadata file in the code.
Please note we come from the previous example, where we loaded the translation manager into an object called `SAMPLE_TEXTS`.

````python

    try:
        SAMPLE_META = SAMPLE_TEXTS.get_metadata()
    Except Exception as e_metadata:
        print(f"Error loading metadata: {e_metadata}")
    
    print("metadata:")
    print(SAMPLE_META["GREETINGS"])
````
The metadata file is loaded into a dictionary, where the keys are the same as the ones in the translations file.

## Larger texts usage (txt files)
The module is designed to work with larger texts in txt files.
For the moment, those larger text are not referenced by keys, other than the name of the file (in fact, the name of the file without the language prefix is the key).
See an example:

````python
from pypyrus import translation_manager as TRM

    SAMPLE_QUOTES = None
    try:
        SAMPLE_QUOTES = TRM.TranslationManager( 
            translations_path="resources/quotes",
            translations_file=None,
            active_lang="en"
            )
    except Exception as e_translation_manager:
        print(f"Error loading translations: {e_translation_manager}")        
    
    print(SAMPLE_QUOTES.load_text_file("waltari")) # Load text from en_waltari.txt
    SAMPLE_QUOTES.set_active_language("es")        # Change the active language to Spanish
    print(SAMPLE_QUOTES.load_text_file("waltari")) # Load text from es_waltari.txt
````

## Usage of AI models in the development of this module
I have partly used AI models to help me with the development of this module, but I have not used them to generate any texts or translations.
More specifically I have used ChatGPT (GPT-4-turbo), but not all the code is AI generated. Some parts are, others are my own.

# Final Greetings
Hopefully you can get some use of this module.
And if not, you know what they say:

> Millennium Hand and Shrimp!!! 


