import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from typing import Dict, List, Union
import wandb
from tqdm import tqdm

class ModelTrainer:
    def __init__(self, model: nn.Module, config: Dict):
        self.model = model
        self.optimizer = torch.optim.AdamW(model.parameters(), lr=config['learning_rate'])
        self.scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(self.optimizer, T_max=config['epochs'])
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        
    async def train_epoch(self, dataloader: DataLoader) -> Dict:
        self.model.train()
        total_loss = 0
        all_predictions = []
        
        for batch in tqdm(dataloader):
            loss, predictions = self._process_batch(batch)
            self._update_model(loss)
            total_loss += loss.item()
            all_predictions.extend(predictions)
            
        return {'loss': total_loss / len(dataloader), 'predictions': all_predictions} 