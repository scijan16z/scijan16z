from sklearn.metrics import precision_recall_fscore_support
import numpy as np
from typing import Dict, List, Union
from dataclasses import dataclass

@dataclass
class ValidationMetrics:
    precision: float
    recall: float
    f1_score: float
    confidence: float
    sample_size: int

class MetricsCalculator:
    def __init__(self):
        self.metrics_history = []
        self.threshold = 0.95
        
    def calculate_metrics(self, predictions: np.ndarray, ground_truth: np.ndarray) -> ValidationMetrics:
        precision, recall, f1, _ = precision_recall_fscore_support(
            ground_truth, predictions, average='weighted'
        )
        confidence = self._calculate_confidence_interval(predictions)
        return ValidationMetrics(precision, recall, f1, confidence, len(predictions)) 