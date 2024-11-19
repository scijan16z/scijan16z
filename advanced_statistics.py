import statsmodels.api as sm
from scipy import stats
import numpy as np
from typing import Dict, List, Union
from dataclasses import dataclass

class AdvancedStatistics:
    def __init__(self):
        self.tests = {
            'meta_analysis': self._perform_meta_analysis,
            'bayesian_inference': self._perform_bayesian_analysis,
            'power_analysis': self._perform_power_analysis,
            'effect_size': self._calculate_effect_sizes
        }
        
    def analyze_study_power(self, data: Dict) -> Dict:
        effect_size = self._calculate_cohens_d(data['experimental'], data['control'])
        power = stats.power.TTestPower().solve_power(
            effect_size=effect_size,
            nobs=len(data['experimental']),
            alpha=0.05
        )
        return {
            'effect_size': effect_size,
            'power': power,
            'sample_size_recommendation': self._recommend_sample_size(effect_size)
        } 