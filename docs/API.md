# Stock Trade - API Documentation

## Base URL
```
http://localhost:5000/api
```

## Authentication
All endpoints (except login/register) require a JWT token in the `Authorization` header:
```
Authorization: Bearer <your_jwt_token>
```

---

## User Endpoints

### 1. Register User
- **POST** `/auth/register`
- **Request Body**:
  ```json
  {
    "email": "user@example.com",
    "password": "secure_password",
    "name": "John Doe",
    "role": "student"
  }
  ```
- **Response**: User object + JWT token

### 2. Login
- **POST** `/auth/login`
- **Request Body**:
  ```json
  {
    "email": "user@example.com",
    "password": "secure_password"
  }
  ```
- **Response**: User object + JWT token

### 3. Get User Profile
- **GET** `/users/profile`
- **Response**: Current user details

### 4. Update User Profile
- **PUT** `/users/profile`
- **Request Body**:
  ```json
  {
    "name": "Jane Doe",
    "phone": "+1-234-567-8900"
  }
  ```
- **Response**: Updated user object

---

## Portfolio Endpoints

### 1. Get Portfolio
- **GET** `/portfolio`
- **Response**:
  ```json
  {
    "userId": "user_id",
    "balance": 10000,
    "holdings": [
      {
        "symbol": "AAPL",
        "quantity": 10,
        "avgPrice": 150.50,
        "currentPrice": 175.25,
        "totalValue": 1752.50,
        "gainLoss": 247.50
      }
    ],
    "totalValue": 11752.50,
    "todayGainLoss": 247.50,
    "todayGainLossPercent": 2.15
  }
  ```

### 2. Get Portfolio History
- **GET** `/portfolio/history?period=1M`
- **Query Parameters**: `period` (1D, 1W, 1M, 3M, 1Y)
- **Response**: Historical portfolio values and performance

---

## Trading Endpoints

### 1. Place Buy Order
- **POST** `/trades/buy`
- **Request Body**:
  ```json
  {
    "symbol": "AAPL",
    "quantity": 5,
    "price": 150.50
  }
  ```
- **Response**: Order confirmation

### 2. Place Sell Order
- **POST** `/trades/sell`
- **Request Body**:
  ```json
  {
    "symbol": "AAPL",
    "quantity": 5,
    "price": 175.25
  }
  ```
- **Response**: Order confirmation

### 3. Get Trade History
- **GET** `/trades/history?page=1&limit=20`
- **Response**: List of past trades

### 4. Cancel Order
- **DELETE** `/trades/:orderId`
- **Response**: Cancellation confirmation

---

## Stock Data Endpoints

### 1. Get Stock Quote
- **GET** `/stocks/:symbol`
- **Response**:
  ```json
  {
    "symbol": "AAPL",
    "name": "Apple Inc.",
    "price": 175.25,
    "change": 2.50,
    "changePercent": 1.45,
    "high": 176.50,
    "low": 173.80,
    "volume": 45000000,
    "marketCap": 2750000000000
  }
  ```

### 2. Search Stocks
- **GET** `/stocks/search?q=apple`
- **Response**: List of matching stocks

### 3. Get Stock Chart Data
- **GET** `/stocks/:symbol/chart?period=1M`
- **Query Parameters**: `period` (1D, 1W, 1M, 3M, 1Y)
- **Response**: Historical price data for charting

---

## Weather Endpoints

### 1. Get Current Weather
- **GET** `/weather/:location`
- **Response**:
  ```json
  {
    "location": "New York",
    "temperature": 72,
    "condition": "Partly Cloudy",
    "humidity": 65,
    "windSpeed": 8,
    "feelsLike": 70,
    "uvIndex": 6,
    "visibility": 10
  }
  ```

### 2. Get Weather Forecast
- **GET** `/weather/:location/forecast`
- **Response**: 5-day weather forecast

### 3. Get Weather Alerts
- **GET** `/weather/:location/alerts`
- **Response**: Active weather alerts for location

---

## Leaderboard Endpoints

### 1. Get Global Leaderboard
- **GET** `/leaderboards/global?period=1M&limit=100`
- **Query Parameters**: 
  - `period` (1D, 1W, 1M, ALL)
  - `limit` (default: 100)
- **Response**: Ranked list of top traders

### 2. Get User Rank
- **GET** `/leaderboards/rank/:userId`
- **Response**: User's rank and performance metrics

---

## Admin Endpoints

### 1. Get All Users
- **GET** `/admin/users`
- **Query Parameters**: `page`, `limit`, `role`, `status`
- **Response**: List of users (Admin only)

### 2. Update User Status
- **PUT** `/admin/users/:userId/status`
- **Request Body**: `{ "status": "active" | "suspended" | "deleted" }`
- **Response**: Updated user object (Admin only)

### 3. Get Platform Analytics
- **GET** `/admin/analytics`
- **Response**: Trading volume, user stats, platform metrics (Admin only)

### 4. Update Platform Settings
- **PUT** `/admin/settings`
- **Request Body**: Platform configuration
- **Response**: Updated settings (Admin only)

---

## Error Responses

All errors follow this format:
```json
{
  "status": 400,
  "message": "Error description",
  "code": "ERROR_CODE"
}
```

### Common Error Codes
- `INVALID_CREDENTIALS` - Login failed
- `INSUFFICIENT_BALANCE` - Not enough funds
- `STOCK_NOT_FOUND` - Invalid stock symbol
- `UNAUTHORIZED` - Missing or invalid token
- `FORBIDDEN` - Insufficient permissions
- `INTERNAL_ERROR` - Server error

---

## Rate Limiting
- 100 requests per minute per IP
- 1000 requests per hour per authenticated user
- Response header: `X-RateLimit-Remaining`