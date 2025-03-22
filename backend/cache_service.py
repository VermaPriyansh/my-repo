# backend/app/services/cache_service.py
from typing import Dict, Any, Optional
import time
import logging

logger = logging.getLogger("cache_service")

class CacheService:
    def __init__(self, max_size: int = 1000, ttl: int = 3600):
        """
        Initialize a simple in-memory cache
        
        Parameters:
        - max_size: Maximum number of items to store in cache
        - ttl: Time-to-live in seconds for cache items
        """
        self.cache = {}
        self.max_size = max_size
        self.ttl = ttl
        logger.info(f"Initialized cache with max_size={max_size}, ttl={ttl}s")
    
    def get(self, key: str) -> Optional[Dict[str, Any]]:
        """Get an item from the cache"""
        if key not in self.cache:
            return None
            
        item, timestamp = self.cache[key]
        
        # Check if the item has expired
        if time.time() - timestamp > self.ttl:
            del self.cache[key]
            return None
            
        return item
    
    def set(self, key: str, value: Dict[str, Any]) -> None:
        """Add an item to the cache"""
        # If cache is full, remove the oldest item
        if len(self.cache) >= self.max_size:
            oldest_key = min(self.cache.keys(), key=lambda k: self.cache[k][1])
            del self.cache[oldest_key]
            
        self.cache[key] = (value, time.time())
