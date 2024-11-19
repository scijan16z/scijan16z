import numpy as np
import scipy.stats as stats
from typing import Dict, List, Union
from dataclasses import dataclass
from p_value_validator import PValueValidator
from effect_size_calculator import EffectSizeCalculator

@dataclass
class StatisticalTest:
    name: str
    parameters: Dict
    assumptions: List[str]
    results: Dict

class StatisticalAnalyzer:
    def __init__(self):
        self.p_validator = PValueValidator()
        self.effect_calculator = EffectSizeCalculator()
        self.supported_tests = {
            't_test': self._perform_t_test,
            'chi_square': self._perform_chi_square,
            'anova': self._perform_anova,
            'regression': self._perform_regression
        }
        
    def analyze_results(self, paper_data: Dict) -> Dict:
        reported_stats = self._extract_statistical_claims(paper_data)
        recalculated = self._recalculate_statistics(paper_data)
        discrepancies = self._find_discrepancies(reported_stats, recalculated)
        return self._generate_analysis_report(discrepancies) 