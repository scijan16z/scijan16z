import bibtexparser
from typing import Dict, List, Union
import difflib
import re

class CitationValidator:
    def __init__(self):
        self.reference_db = ReferenceDatabase()
        self.similarity_threshold = 0.85
        
    async def validate_citations(self, paper_citations: List[Dict]) -> Dict:
        validation_results = []
        for citation in paper_citations:
            matched_reference = await self.reference_db.find_best_match(citation)
            similarity_score = self._calculate_similarity(citation, matched_reference)
            validation_results.append({
                'citation': citation,
                'matched_reference': matched_reference,
                'similarity_score': similarity_score,
                'is_valid': similarity_score >= self.similarity_threshold,
                'suggested_corrections': self._generate_corrections(citation, matched_reference)
            })
        return self._compile_validation_report(validation_results) 