class ScoringEngine:

    def compute_score(self, issue_count: int) -> int:
        base_score = 100
        penalty = issue_count * 20
        return max(base_score - penalty, 0)
