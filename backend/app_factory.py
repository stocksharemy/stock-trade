from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
import logging
import os
from config import config

# Initialize extensions
db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()

def create_app(config_name='development'):
    """Application factory"""
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    
    # Setup logging
    setup_logging(app)
    
    # Register blueprints
    from routes.auth import auth_bp
    from routes.portfolio import portfolio_bp
    from routes.trades import trades_bp
    from routes.stocks import stocks_bp
    from routes.weather import weather_bp
    from routes.leaderboard import leaderboard_bp
    from routes.admin import admin_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(portfolio_bp, url_prefix='/api/portfolio')
    app.register_blueprint(trades_bp, url_prefix='/api/trades')
    app.register_blueprint(stocks_bp, url_prefix='/api/stocks')
    app.register_blueprint(weather_bp, url_prefix='/api/weather')
    app.register_blueprint(leaderboard_bp, url_prefix='/api/leaderboards')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    # Health check endpoint
    @app.route('/api/health', methods=['GET'])
    def health():
        return {'status': 'ok', 'message': 'Stock Trade API is running'}, 200
    
    return app

def setup_logging(app):
    """Setup application logging"""
    if not app.debug:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        
        file_handler = logging.FileHandler(app.config['LOG_FILE'])
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
        file_handler.setLevel(getattr(logging, app.config['LOG_LEVEL'].upper()))
        app.logger.addHandler(file_handler)
        app.logger.setLevel(getattr(logging, app.config['LOG_LEVEL'].upper()))
        app.logger.info('Stock Trade API startup')
