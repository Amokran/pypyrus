from typing import Any, Dict, Optional

class Metadata:
    def __init__(self, data: Dict[str, Any]):
        self.type: str = data.get("type", "text")
        self.source: Optional[str] = data.get("source")
        self.tags: Dict[str, list] = data.get("tags", {})
        self.context_tags: Dict[str, list] = data.get("context-tags", {})

        self.book: Optional[Dict[str, Any]] = data.get("book")
        self.article: Optional[Dict[str, Any]] = data.get("article")

    def get_tags(self, lang: str) -> list:
        return self.tags.get(lang, [])

    def get_context_tags(self, lang: str) -> list:
        return self.context_tags.get(lang, [])

    def get_book_info(self, lang: Optional[str] = None) -> Dict[str, Any]:
        if not self.book:
            return {}
        info = {k: v for k, v in self.book.items() if k != "languages"}
        if lang and "languages" in self.book:
            info.update(self.book["languages"].get(lang, {}))
        return info

    def get_article_info(self, lang: Optional[str] = None) -> Dict[str, Any]:
        if not self.article:
            return {}
        info = {k: v for k, v in self.article.items() if k != "languages"}
        if lang and "languages" in self.article:
            info.update(self.article["languages"].get(lang, {}))
        return info

    def __repr__(self):
        return f"<Metadata type={self.type} source={self.source}>"