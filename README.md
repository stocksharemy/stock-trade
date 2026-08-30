# Stock Trade - Educational Stock Trading Platform

An interactive, web-based educational platform designed to teach users the fundamentals of stock trading and financial literacy. The platform simulates a real-world stock market environment using virtual currency (paper trading).

## 📚 Features

### User Panel
- **Live Trading Practice** - Trade virtual stocks in a simulated market
- **Portfolio Management** - Track holdings, gains/losses, and performance metrics
- **Market Data Dashboard** - Real-time stock quotes and charting
- **Educational Resources** - Learn trading fundamentals and strategies
- **Performance Analytics** - Detailed reports on trading activity

### Admin Panel
- **User Management** - Track and manage student accounts
- **Content Management** - Update educational materials and resources
- **Platform Analytics** - Monitor platform usage and trading activity
- **Leaderboards** - Display top traders and rankings
- **System Configuration** - Configure trading parameters and settings

### Weather Dashboard
- **Real-time Weather Data** - Fetches current weather from public API
- **Location-based Forecasts** - View weather for any location
- **Market Impact Analysis** - Optional correlation between weather and market sentiment
- **Interactive Weather Widget** - Integrated into the main dashboard

## 🏗️ Project Structure

```
stock-trade/
├── frontend/                 # React/Vue frontend application
│   ├── src/
│   │   ├── components/       # Reusable UI components
│   │   ├── pages/            # Page components
│   │   ├── services/         # API service modules
│   │   ├── styles/           # CSS/SCSS files
│   │   └── utils/            # Utility functions
│   ├── public/               # Static assets
│   └── package.json
├── backend/                  # Node.js/Python backend
│   ├── routes/               # API endpoints
│   ├── controllers/          # Business logic
│   ├── models/               # Database models
│   ├── middleware/           # Authentication & validation
│   ├── config/               # Configuration files
│   └── requirements.txt      # Dependencies
├── database/                 # Database schemas
│   └── migrations/           # Database migrations
├── docs/                     # Documentation
├── .gitignore
├── docker-compose.yml        # Docker setup
└── README.md
```

## 🚀 Quick Start

### Prerequisites
- Node.js 16+ or Python 3.8+
- npm or pip
- Weather API Key (OpenWeatherMap, WeatherAPI, etc.)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/stocksharemy/stock-trade.git
   cd stock-trade
   ```

2. **Install dependencies**
   ```bash
   # Frontend
   cd frontend
   npm install
   
   # Backend
   cd ../backend
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   # Create .env file
   cp .env.example .env
   
   # Add your API keys:
   # - Weather API Key
   # - Stock Market API Key
   # - Database URL
   # - JWT Secret
   ```

4. **Start the application**
   ```bash
   # Frontend (port 3000)
   npm start
   
   # Backend (port 5000)
   python app.py
   ```

## 🌤️ Weather API Integration

The platform integrates with **OpenWeatherMap API** (or configurable alternative):

- **Endpoint**: `https://api.openweathermap.org/data/2.5/weather`
- **Features**: Current weather, 5-day forecast, weather alerts
- **Configuration**: Set `WEATHER_API_KEY` in `.env`

### Weather Dashboard Endpoints
- `GET /api/weather/:location` - Get current weather
- `GET /api/weather/:location/forecast` - Get forecast data
- `GET /api/weather/alerts/:location` - Get weather alerts

## 📊 Stock Market Simulation

- **Virtual Currency**: $10,000 starting balance
- **Real-time Data**: Market updates every second
- **Trading Hours**: Configurable market hours
- **Commission**: Realistic trading fees
- **Portfolio Tracking**: Real-time P&L calculations

## 🔐 Authentication

- JWT-based authentication
- Role-based access control (Student, Admin)
- Secure password hashing with bcrypt
- Session management

## 📚 Technology Stack

### Frontend
- React / Vue.js
- Redux / Vuex (State Management)
- Axios (HTTP Client)
- Chart.js / D3.js (Charting)
- Tailwind CSS / Material UI (Styling)

### Backend
- Node.js (Express.js) or Python (Flask/Django)
- PostgreSQL / MongoDB (Database)
- Redis (Caching)
- JWT (Authentication)

### External APIs
- OpenWeatherMap API (Weather Data)
- Alpha Vantage / IEX Cloud (Stock Data)

## 📖 Documentation

See the `/docs` folder for:
- [API Documentation](docs/API.md)
- [User Guide](docs/USER_GUIDE.md)
- [Admin Guide](docs/ADMIN_GUIDE.md)
- [Developer Setup](docs/DEVELOPER_SETUP.md)

## 🧪 Testing

```bash
# Run tests
npm test          # Frontend
pytest            # Backend

# Coverage reports
npm run coverage
pytest --cov
```

## 🐳 Docker Deployment

```bash
# Build and run with Docker
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

## 📝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Support

For questions or issues:
- Open a GitHub Issue
- Check existing documentation in `/docs`
- Contact: support@stock-trade.edu

## 🎯 Roadmap

- [ ] Mobile app (React Native/Flutter)
- [ ] Advanced charting tools
- [ ] AI-powered trading insights
- [ ] Social trading features
- [ ] Real market integration (with real money)
- [ ] Multi-language support
- [ ] Gamification elements

---

**Happy Trading! 📈**

*Educational Purpose Only - This platform is designed for learning. Always practice with virtual currency before using real money.*
