from transformers import AutoModelForCausalLM, AutoTokenizer
import anthropic, openai, google.palm
from typing import Dict, List, Union
import torch
import asyncio
from token_manager import TokenUsageManager
from model_router import ModelRouter

class LLMOrchestrator:
    def __init__(self, config: Dict):
        self.models = {
            'gpt4': self._init_gpt4(),
            'claude': self._init_claude(),
            'local_llama': self._init_llama(),
            'palm': self._init_palm()
        }
        self.router = ModelRouter(config['routing_strategy'])
        self.token_manager = TokenUsageManager()
        
    async def process_query(self, query: str, context: Dict, model_preference: str = None) -> Dict:
        selected_model = self.router.select_model(query, context, model_preference)
        response = await self._get_response(selected_model, query, context)
        return self._post_process_response(response, selected_model) 