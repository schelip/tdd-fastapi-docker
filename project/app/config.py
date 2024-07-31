import logging
import os
from pydantic_settings import BaseSettings
from functools import lru_cache

log = logging.getLogger('univorn')

class Settings(BaseSettings):
  environment: str = os.getenv('ENVIRONMENT', 'dev')
  testing: bool = os.getenv('TESTING', 0)

@lru_cache
def get_settings() -> BaseSettings:
  log.info('Loading configuration...')
  return Settings()
