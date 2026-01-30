from app.services.nlp_processor import NLPProcessor
from app.services.ai_rewriter import AIRewriter
from app.services.scoring_engine import ScoringEngine
from app.services.quality_rules import SRSQualityRules
from app.models.schemas import (
    AnalysisResult,
    RequirementAnalysis,
    RewrittenRequirement,
    TraceabilityInfo,
    RTMEntry,
    RequirementInput
)


class SRSAnalyzer:

    def analyze(self, requirements: list[RequirementInput]) -> AnalysisResult:
        nlp = NLPProcessor()
        ai = AIRewriter()
        scorer = ScoringEngine()
        rules = SRSQualityRules()

        per_req_results = []
        rewritten_reqs = []
        traceability = []
        rtm = []

        total_issues = 0

        for req in requirements:
            processed = nlp.preprocess(req.text)
            ambiguities = rules.check_ambiguity(processed)
            score = scorer.compute_score(len(ambiguities))
            total_issues += len(ambiguities)

            per_req_results.append(
                RequirementAnalysis(
                    requirement_id=req.id,
                    quality_score=score,
                    ambiguities=ambiguities
                )
            )

            if ambiguities:
                rewritten_reqs.append(
                    RewrittenRequirement(
                        original_id=req.id,
                        original_text=req.text,
                        rewritten_text = ai.rewrite(processed, ambiguities)

                    )
                )

            traceability.append(
                TraceabilityInfo(
                    requirement_id=req.id,
                    rules_triggered=["Ambiguity"] if ambiguities else [],
                    phase="Phase-3: Program Synthesis"
                )
            )

            rtm.append(
                RTMEntry(
                    requirement_id=req.id,
                    requirement_text=req.text,
                    detected_issues=ambiguities,
                    related_rules=["Ambiguity"] if ambiguities else [],
                    phase="Phase-3: Program Synthesis"
                )
            )

        overall_score = scorer.compute_score(total_issues)

        return AnalysisResult(
            overall_quality_score=overall_score,
            per_requirement_analysis=per_req_results,
            rewritten_requirements=rewritten_reqs,
            traceability=traceability,
            rtm=rtm
        )
