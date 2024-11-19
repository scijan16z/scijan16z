import cv2
import numpy as np
from PIL import Image
import pytesseract
from typing import Dict, List, Union

class FigureExtractor:
    def __init__(self):
        self.image_processor = ImageProcessor()
        self.text_extractor = pytesseract.image_to_string
        self.graph_analyzer = GraphAnalyzer()
        
    async def extract_figures(self, pdf_path: str) -> List[Dict]:
        images = await self._extract_images_from_pdf(pdf_path)
        results = []
        for img in images:
            processed_img = self.image_processor.preprocess(img)
            text = self.text_extractor(processed_img)
            graph_data = await self.graph_analyzer.analyze(processed_img)
            results.append({
                'text': text,
                'graph_data': graph_data,
                'type': self._classify_figure_type(processed_img)
            })
        return results 