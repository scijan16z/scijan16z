import jinja2
import pdfkit
from typing import Dict, List, Union
import matplotlib.pyplot as plt
import seaborn as sns

class ReportGenerator:
    def __init__(self):
        self.template_loader = jinja2.FileSystemLoader('templates')
        self.template_env = jinja2.Environment(loader=self.template_loader)
        self.visualization_engine = VisualizationEngine()
        
    async def generate_report(self, analysis_results: Dict) -> bytes:
        template = self.template_env.get_template('analysis_report.html')
        visualizations = await self._generate_visualizations(analysis_results)
        html_content = template.render(
            results=analysis_results,
            visualizations=visualizations,
            metadata=self._generate_metadata()
        )
        return await self._convert_to_pdf(html_content) 