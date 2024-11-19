import spacy
import nltk
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from typing import Dict, List, Union
import torch.nn.functional as F

class ScientificNLP:
    def __init__(self):
        self.nlp = spacy.load("en_core_sci_scibert")
        self.tokenizer = AutoTokenizer.from_pretrained("allenai/scibert_scivocab_uncased")
        self.citation_extractor = CitationParser()
        self.method_extractor = MethodologyExtractor()
        
    async def analyze_text(self, text: str) -> Dict:
        doc = self.nlp(text)
        return {
            'citations': await self.citation_extractor.extract(doc),
            'methodology': await self.method_extractor.analyze(doc),
            'statistical_claims': self._extract_statistical_claims(doc),
            'key_findings': self._extract_key_findings(doc),
            'entity_relationships': self._build_entity_graph(doc)
        } 