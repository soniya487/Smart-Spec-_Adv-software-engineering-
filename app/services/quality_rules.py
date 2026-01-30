class SRSQualityRules:

    VAGUE_TERMS = [
        "fast",
        "user-friendly",
        "efficient",
        "easy",
        "secure",
        "reliable"
    ]

    def check_ambiguity(self, text: str):
        issues = []
        lower_text = text.lower()

        for term in self.VAGUE_TERMS:
            if term in lower_text:
                issues.append(term)

        return issues
