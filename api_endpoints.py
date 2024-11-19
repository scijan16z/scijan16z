from fastapi import FastAPI, HTTPException, Depends
from typing import Dict, List, Union
from pydantic import BaseModel
import asyncio

app = FastAPI()

class PaperAnalysisRequest(BaseModel):
    paper_id: str
    analysis_type: List[str]
    confidence_threshold: float = 0.95

@app.post("/analyze/paper")
async def analyze_paper(request: PaperAnalysisRequest):
    try:
        analysis_result = await paper_analyzer.analyze(
            paper_id=request.paper_id,
            analysis_types=request.analysis_type,
            threshold=request.confidence_threshold
        )
        return {"status": "success", "results": analysis_result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/paper/{paper_id}/status")
async def get_analysis_status(paper_id: str):
    status = await analysis_tracker.get_status(paper_id)
    return {"paper_id": paper_id, "status": status} 