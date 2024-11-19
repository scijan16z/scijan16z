from sqlalchemy import create_engine, Column, Integer, String, JSON, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import asyncpg
import motor.motor_asyncio
from typing import Dict, List, Union

class DatabaseManager:
    def __init__(self, config: Dict):
        self.mongo_client = motor.motor_asyncio.AsyncIOMotorClient(config['mongo_uri'])
        self.postgres_pool = asyncpg.create_pool(config['postgres_uri'])
        self.redis_client = aioredis.from_url(config['redis_uri'])
        
    async def store_paper_analysis(self, paper_id: str, analysis_results: Dict):
        async with self.postgres_pool.acquire() as conn:
            await conn.execute("""
                INSERT INTO paper_analyses (paper_id, results, confidence_score)
                VALUES ($1, $2, $3)
                ON CONFLICT (paper_id) DO UPDATE SET results = $2, confidence_score = $3
            """, paper_id, analysis_results, analysis_results['confidence'])
