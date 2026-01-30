class AIRewriter:

    def rewrite(self, text: str, ambiguous_terms: list[str]) -> str:
        terms = ", ".join([f"'{t}'" for t in ambiguous_terms])

        return (
            f"The requirement contains ambiguous terms ({terms}). "
            f"Replace them with measurable and verifiable performance or usability criteria "
            f"to improve requirement quality."
        )


