import json
import os
from typing import Dict, Any, Optional
from metadata import Metadata

class TranslationManager:
    def __init__(self, translations_path: str, translations_file: str = None, active_lang: str = "en"):
        self.translations_path = translations_path
        self.translations_file = translations_file
        self.active_lang = active_lang
        self.translations = {}
        self.metadata = {}
        self.load_translations_from_folder()

    def get_translations(self):
        return self.translations

    def get_metadata(self):
        return self.metadata

    def set_active_language(self, active_lang: str = "en"):
        """Set active language, although won't check if it exists in translation files."""
        self.active_lang = active_lang

    def load_translations_from_folder(self):
        """Loads all JSON translation files from the specified directory."""
        if not os.path.isdir(self.translations_path):
            raise ValueError(f"Invalid translations directory: {self.translations_path}")

        for file in os.listdir(self.translations_path):
            if file.endswith(".json"):
                category = file.replace(".json", "")
                file_path = os.path.join(self.translations_path, file)

                with open(file_path, "r", encoding="utf-8") as f:
                    try:
                        data = json.load(f)
                        if category == "metadata":
                            self.metadata = {k: Metadata(v) for k, v in data.items()}
                        else:
                            self.translations[category] = data
                    except json.JSONDecodeError as e:
                        raise ValueError(f"Error decoding {file}: {e}")

    def load_translations_from_file(self):
        """Loads a specific JSON translation file from the specified file name."""
        if not os.path.isdir(self.translations_path):
            raise ValueError(f"Invalid translations directory: {self.translations_path}")

        for file in os.listdir(self.translations_path):
            if file.endswith(".json"):
                category = file.replace(".json", "")
                if category == self.translations_file:
                    file_path = os.path.join(self.translations_path, self.translations_file)

                    with open(file_path, "r", encoding="utf-8") as f:
                        try:
                            data = json.load(f)
                            self.translations[category] = data
                        except json.JSONDecodeError as e:
                            raise ValueError(f"Error decoding {file}: {e}")

    def translate(self, key: str, **kwargs) -> str:
        """Retrieves a translation for the given key and language, formatting it if needed."""
        try:
            for category in self.translations:
                for lang in self.translations[category]:
                    if lang == self.active_lang:
                        if key in self.translations[category][lang]:
                            return self.translations[category][lang][key].format(**kwargs)

            return f"[{key}]"  # Return key as fallback
        except Exception:
            return f"[{key}]"  # Return key as fallback

    def get_metadata_for_key(self, key: str) -> Optional[Metadata]:
        """Returns the metadata object for a given key, if available."""
        return self.metadata.get(key)

    def load_text_file(self, category: str, lang: Optional[str] = None) -> str:
        """Loads a text file containing a long translation."""
        lang = lang or self.active_lang
        file_name = f"{lang}_{category}.txt"
        file_path = os.path.normpath(os.path.join(self.translations_path, file_name))

        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()

        return f"[{category} missing]"  # Return fallback message
