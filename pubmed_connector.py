import xml.etree.ElementTree as ET
import aiohttp
from typing import Dict, List, Union
from datetime import datetime, timedelta

class PubMedConnector:
    def __init__(self, api_key: str):
        self.base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
        self.api_key = api_key
        self.rate_limiter = AsyncRateLimiter(300, 60)  # 300 requests per minute
        
    async def fetch_paper_metadata(self, pmid: str) -> Dict:
        async with self.rate_limiter:
            url = f"{self.base_url}efetch.fcgi"
            params = {
                'db': 'pubmed',
                'id': pmid,
                'retmode': 'xml',
                'api_key': self.api_key
            }
            async with aiohttp.ClientSession() as session:
                async with session.get(url, params=params) as response:
                    xml_data = await response.text()
                    return self._parse_pubmed_xml(xml_data) 