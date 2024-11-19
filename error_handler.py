import traceback
from typing import Dict, List, Union
import logging
import sentry_sdk

class ErrorHandler:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.error_patterns = self._load_error_patterns()
        
    async def handle_error(self, error: Exception, context: Dict) -> Dict:
        error_id = self._generate_error_id()
        self._log_error(error_id, error, context)
        
        if self._is_critical(error):
            await self._notify_admin(error_id, error)
            
        return self._format_error_response(error_id, error) 