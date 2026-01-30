from fastapi import APIRouter
from app.models.schemas import SRSInput, AnalysisResult
from app.services.srs_analyzer import SRSAnalyzer

router = APIRouter(prefix="/analyze", tags=["SRS Analysis"])


@router.post("/", response_model=AnalysisResult)
def analyze_srs(input: SRSInput):
    analyzer = SRSAnalyzer()
    return analyzer.analyze(input.requirements)
