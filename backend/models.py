from app_factory import db
from datetime import datetime

class User(db.Model):
    """User model"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), default='student', nullable=False)  # student, teacher, admin
    status = db.Column(db.String(20), default='active', nullable=False)  # active, suspended, inactive
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    portfolio = db.relationship('Portfolio', backref='user', uselist=False, cascade='all, delete-orphan')
    trades = db.relationship('Trade', backref='user', cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'role': self.role,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class Portfolio(db.Model):
    """Portfolio model"""
    __tablename__ = 'portfolios'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)
    balance = db.Column(db.Float, default=10000.0, nullable=False)
    total_invested = db.Column(db.Float, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    holdings = db.relationship('Holding', backref='portfolio', cascade='all, delete-orphan')
    
    def to_dict(self):
        total_value = self.balance + sum(h.total_value for h in self.holdings)
        gain_loss = total_value - (self.total_invested + self.balance)
        
        return {
            'id': self.id,
            'balance': self.balance,
            'holdings': [h.to_dict() for h in self.holdings],
            'total_value': total_value,
            'total_gain_loss': gain_loss,
            'total_gain_loss_percent': (gain_loss / (self.total_invested or total_value)) * 100 if (self.total_invested or total_value) > 0 else 0
        }

class Holding(db.Model):
    """Stock holding model"""
    __tablename__ = 'holdings'
    
    id = db.Column(db.Integer, primary_key=True)
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolios.id'), nullable=False)
    symbol = db.Column(db.String(10), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    average_price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self, current_price=None):
        current_price = current_price or self.average_price
        total_value = self.quantity * current_price
        gain_loss = total_value - (self.quantity * self.average_price)
        
        return {
            'symbol': self.symbol,
            'quantity': self.quantity,
            'average_price': self.average_price,
            'current_price': current_price,
            'total_value': total_value,
            'gain_loss': gain_loss,
            'gain_loss_percent': (gain_loss / (self.quantity * self.average_price)) * 100 if (self.quantity * self.average_price) > 0 else 0
        }

class Trade(db.Model):
    """Trade/Order model"""
    __tablename__ = 'trades'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    symbol = db.Column(db.String(10), nullable=False)
    trade_type = db.Column(db.String(10), nullable=False)  # buy, sell
    quantity = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    commission = db.Column(db.Float, nullable=False)
    total_value = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='completed', nullable=False)  # pending, completed, cancelled
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'symbol': self.symbol,
            'type': self.trade_type,
            'quantity': self.quantity,
            'price': self.price,
            'commission': self.commission,
            'total_value': self.total_value,
            'status': self.status,
            'created_at': self.created_at.isoformat()
        }
