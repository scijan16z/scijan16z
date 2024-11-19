import aiohttp
from typing import Dict, List, Union
import asyncio
from ratelimit import limits, sleep_and_retry

class SemanticScholarAPI:
    def __init__(self):
        self.base_url = "https://api.semanticscholar.org/v1"
        self.session = aiohttp.ClientSession()
        self.rate_limiter = RateLimiter(max_requests=100, time_window=60)
        
    @sleep_and_retry
    @limits(calls=100, period=60)
    async def fetch_paper_details(self, paper_id: str) -> Dict:
        endpoint = f"{self.base_url}/paper/{paper_id}"
        async with self.session.get(endpoint) as response:
            data = await response.json()
            return self._process_paper_data(data)
            
    async def fetch_citations(self, paper_id: str, limit: int = 100) -> List[Dict]:
        endpoint = f"{self.base_url}/paper/{paper_id}/citations"
        return await self._paginated_fetch(endpoint, limit) 