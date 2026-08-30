import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration"""
    SECRET_KEY = os.getenv('JWT_SECRET', 'dev-secret-key-change-in-production')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # JWT Configuration
    JWT_SECRET_KEY = os.getenv('JWT_SECRET', 'dev-secret-key-change-in-production')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=7)
    
    # API Keys
    WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
    STOCK_API_KEY = os.getenv('STOCK_API_KEY')
    
    # Redis Configuration
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')
    
    # Application Settings
    INITIAL_BALANCE = float(os.getenv('INITIAL_BALANCE', 10000))
    COMMISSION_RATE = float(os.getenv('COMMISSION_RATE', 0.001))
    MARKET_OPEN_HOUR = int(os.getenv('MARKET_OPEN_HOUR', 9))
    MARKET_CLOSE_HOUR = int(os.getenv('MARKET_CLOSE_HOUR', 16))
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'info')
    LOG_FILE = os.getenv('LOG_FILE', 'logs/app.log')

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'postgresql://stock_trader:secure_password@localhost:5432/stock_trade'
    )

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=300)

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
