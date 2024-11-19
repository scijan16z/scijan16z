from prometheus_client import Counter, Histogram, Gauge
import datadog
from typing import Dict, List, Union
import time

class MonitoringService:
    def __init__(self):
        self.metrics = {
            'papers_processed': Counter('papers_processed_total', 'Total papers processed'),
            'processing_time': Histogram('processing_time_seconds', 'Time spent processing papers'),
            'error_rate': Gauge('error_rate', 'Current error rate in processing')
        }
        
    async def track_processing(self, paper_id: str):
        start_time = time.time()
        try:
            yield
        finally:
            duration = time.time() - start_time
            self.metrics['processing_time'].observe(duration)
            self.metrics['papers_processed'].inc() 