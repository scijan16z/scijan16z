import yaml
import json
from pathlib import Path
from typing import Dict, List, Union
import os

class ConfigManager:
    def __init__(self):
        self.config = self._load_base_config()
        self.model_configs = self._load_model_configs()
        self.api_configs = self._load_api_configs()
        self.validation_rules = self._load_validation_rules()
        
    def _load_base_config(self) -> Dict:
        with open('config.yaml', 'r') as f:
            return yaml.safe_load(f)
            
    def get_model_config(self, model_name: str) -> Dict:
        return self.model_configs.get(model_name, {}) 