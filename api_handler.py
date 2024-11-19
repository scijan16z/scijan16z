import aiohttp
import asyncio
from typing import Dict, List, Union
from rate_limiter import RateLimiter
from error_handler import APIErrorHandler

class APIHandler:
    def __init__(self):
        self.rate_limiter = RateLimiter()
        self.error_handler = APIErrorHandler()
        self.endpoints = {
            'arxiv': 'http://export.arxiv.org/api/query',
            'pubmed': 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/',
            'crossref': 'https://api.crossref.org/works/',
            'semantic_scholar': 'https://api.semanticscholar.org/v1/paper/'
        }
        
    async def fetch_paper_metadata(self, doi: str) -> Dict:
        async with aiohttp.ClientSession() as session:
            tasks = [
                self._fetch_crossref(session, doi),
                self._fetch_semantic_scholar(session, doi),
                self._fetch_citations(session, doi)
            ]
            return await asyncio.gather(*tasks) 