from bs4 import BeautifulSoup
import requests
import PyPDF2

class PaperProcessor:
    def __init__(self):
        self.statistical_validator = StatisticalValidator()
        self.figure_extractor = FigureExtractor()
        self.table_extractor = TableExtractor()
        
    async def process_paper(self, url: str) -> Dict:
        raw_content = await self._fetch_content(url)
        figures = await self.figure_extractor.extract(raw_content)
        tables = await self.table_extractor.extract(raw_content)
        stats = await self.statistical_validator.validate(raw_content)
        return self._compile_results(raw_content, figures, tables, stats)