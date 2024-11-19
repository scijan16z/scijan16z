import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from typing import Dict, List, Union
import dask.dataframe as dd

class DataPreprocessor:
    def __init__(self):
        self.scalers = {}
        self.encoders = {}
        self.cleaners = {
            'text': TextCleaner(),
            'numerical': NumericalCleaner(),
            'categorical': CategoricalCleaner()
        }
        
    async def preprocess_paper_data(self, raw_data: Dict) -> Dict:
        numerical_features = self._process_numerical_data(raw_data['statistics'])
        text_features = await self._process_text_data(raw_data['content'])
        categorical_features = self._process_categorical_data(raw_data['metadata'])
        
        return self._combine_features(numerical_features, text_features, categorical_features) 