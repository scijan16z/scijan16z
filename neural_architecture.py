import torch
import torch.nn as nn
from transformers import AutoModel
from typing import Dict, List, Union

class ScientificPaperAnalyzer(nn.Module):
    def __init__(self, config: Dict):
        super().__init__()
        self.bert = AutoModel.from_pretrained("allenai/scibert_scivocab_uncased")
        
        self.methodology_analyzer = nn.Sequential(
            nn.Linear(768, 512),
            nn.LayerNorm(512),
            nn.GELU(),
            nn.Dropout(0.1),
            nn.Linear(512, 128)
        )
        
        self.statistical_analyzer = nn.Sequential(
            nn.Linear(768, 512),
            nn.LayerNorm(512),
            nn.GELU(),
            nn.Dropout(0.1),
            nn.Linear(512, 64)
        )
        
        self.reproducibility_scorer = nn.Sequential(
            nn.Linear(192, 96),
            nn.LayerNorm(96),
            nn.GELU(),
            nn.Linear(96, 1),
            nn.Sigmoid()
        ) 