# Stock Trade - Admin Guide

## Table of Contents
1. [Admin Dashboard Overview](#admin-dashboard-overview)
2. [User Management](#user-management)
3. [Platform Analytics](#platform-analytics)
4. [Content Management](#content-management)
5. [System Configuration](#system-configuration)
6. [Monitoring & Maintenance](#monitoring--maintenance)
7. [Security](#security)

---

## Admin Dashboard Overview

### Accessing Admin Panel
1. Log in with admin credentials
2. Navigate to admin URL: `https://stock-trade.edu/admin`
3. You'll see the Admin Dashboard

### Key Metrics
- **Total Users**: Active, suspended, and total count
- **Total Trading Volume**: Daily/weekly/monthly volume
- **Platform Status**: Server health and performance
- **Active Sessions**: Currently logged-in users
- **System Alerts**: Important notifications

---

## User Management

### Viewing Users

1. Go to **Admin Panel > Users**
2. View list of all platform users
3. Filter by:
   - **Status**: Active, Suspended, Inactive
   - **Role**: Student, Teacher, Admin
   - **Date Joined**: Custom date range
   - **Activity Level**: High, Medium, Low

### User Details
Click on a user to view:
- Profile information
- Account statistics
- Trading history
- Login/activity log
- Linked accounts
- Suspension/warning history

### Managing User Accounts

#### Activating Users
1. Go to **Users > Pending**
2. Review user applications
3. Click **Approve** to activate account
4. User receives confirmation email

#### Suspending Users
1. Select user from list
2. Click **Actions > Suspend**
3. Choose duration: 24 hours, 7 days, permanent
4. Enter reason for suspension
5. User is notified via email

#### Resetting User Balances
1. Select user
2. Click **Actions > Reset Portfolio**
3. Confirm action
4. User's balance returns to $10,000
5. All trades are cleared

#### Deleting User Accounts
1. Select user
2. Click **Actions > Delete Account**
3. Confirm permanent deletion
4. All user data is archived
5. Account cannot be recovered

### Role Management
- **Student**: Standard user with trading access
- **Teacher**: Can view student portfolios and performance
- **Admin**: Full platform access

To change user role:
1. Select user
2. Click **Edit Role**
3. Choose new role
4. Click **Update**

---

## Platform Analytics

### Trading Analytics

#### Daily Statistics
- Total trades executed
- Trading volume (shares)
- Total trading value
- Average trade size
- Most traded stocks

#### User Performance
- Top performers (by % gain)
- Largest portfolios
- Most active traders
- Average student performance
- Performance distribution

#### Market Simulation
- Simulated market price movements
- Stock volatility
- Trading patterns
- Market correlation

### User Analytics

#### Engagement Metrics
- Daily active users (DAU)
- Monthly active users (MAU)
- User retention rate
- Session duration
- Login frequency

#### Learning Progress
- Course completion rates
- Video watch time
- Quiz scores
- Time spent learning
- Resource popularity

### Generating Reports

1. Go to **Analytics > Reports**
2. Choose report type:
   - Trading Report
   - User Report
   - Engagement Report
   - Revenue Report (if applicable)

3. Select date range
4. Configure filters
5. Click **Generate**
6. Download as PDF or CSV

---

## Content Management

### Managing Educational Resources

#### Adding Courses
1. Go to **Content > Courses**
2. Click **Add Course**
3. Fill in:
   - **Title**: Course name
   - **Description**: Overview
   - **Level**: Beginner, Intermediate, Advanced
   - **Duration**: Estimated time to complete
   - **Content**: Upload videos, PDFs, articles

4. Click **Publish**

#### Managing Articles
1. Go to **Content > Articles**
2. Click **New Article**
3. Write content using rich text editor
4. Add tags and categories
5. Set publication date
6. Click **Publish**

#### Managing Videos
1. Go to **Content > Videos**
2. Click **Upload Video**
3. Select video file or YouTube URL
4. Add title, description, thumbnail
5. Set visibility and access level
6. Click **Upload**

#### Scheduling Content
- Schedule release date for new content
- Set content expiration dates
- Archive old content
- Control visibility per user role

### Content Moderation
1. Monitor user-generated content
2. Review comments and discussions
3. Flag inappropriate content
4. Remove violations
5. Issue warnings to users

---

## System Configuration

### Platform Settings

#### General Settings
1. Go to **Settings > General**
2. Configure:
   - **Platform Name**: Display name
   - **Logo/Branding**: Upload images
   - **Website URL**: Public URL
   - **Support Email**: Contact email
   - **Timezone**: Default timezone

#### Trading Settings
1. Go to **Settings > Trading**
2. Configure:
   - **Initial Balance**: Starting virtual money ($)
   - **Commission Rate**: Trading fee (%)
   - **Market Open Time**: Opening hour (EST)
   - **Market Close Time**: Closing hour (EST)
   - **Trading Days**: Days of week
   - **Min Trade Size**: Minimum shares
   - **Max Trade Size**: Maximum shares

#### API Configuration
1. Go to **Settings > API Keys**
2. Add/update API keys for:
   - **Weather API**: OpenWeatherMap key
   - **Stock Data API**: Alpha Vantage/IEX Cloud key
   - **Email Service**: SMTP credentials
   - **Payment Gateway**: If applicable

#### Security Settings
1. Go to **Settings > Security**
2. Configure:
   - **Password Requirements**: Complexity rules
   - **Session Timeout**: Minutes of inactivity
   - **2FA Requirement**: Force 2-factor auth
   - **IP Whitelist**: Allowed IPs
   - **Rate Limiting**: Requests per minute

---

## Monitoring & Maintenance

### System Health

#### Server Monitoring
1. Go to **Monitoring > Health**
2. View:
   - **CPU Usage**: Server CPU
   - **Memory**: RAM utilization
   - **Disk Space**: Storage available
   - **Database**: Connection status
   - **Redis Cache**: Cache hit rate
   - **API Response Times**: Latency metrics

#### Error Logs
1. Go to **Monitoring > Logs**
2. Filter by:
   - **Level**: Error, Warning, Info, Debug
   - **Service**: Backend, Frontend, Database
   - **Time Range**: Custom dates

3. View full error details and stack traces

### Backups

#### Automated Backups
- Daily backups at 2:00 AM UTC
- 7-day retention policy
- Stored in secure cloud storage

#### Manual Backup
1. Go to **Maintenance > Backups**
2. Click **Create Backup Now**
3. Choose what to backup:
   - Database
   - User files
   - Configuration

4. Download or store backup

### Database Maintenance

#### Optimization
1. Go to **Maintenance > Database**
2. Click **Optimize Database**
3. Defragment indexes
4. Rebuild statistics
5. Clear cache

#### Migrations
- Monitor pending migrations
- Schedule migration windows
- Test migrations before applying
- Rollback capability

---

## Security

### User Security

#### Account Lockouts
- After 5 failed login attempts, account is locked
- Lock duration: 30 minutes
- Admin can unlock manually
- User receives notification

#### Password Requirements
- Minimum 8 characters
- Must include: uppercase, lowercase, numbers, symbols
- Cannot reuse last 5 passwords
- Change required every 90 days

#### 2-Factor Authentication
- Enable 2FA for all admin accounts
- Recommend 2FA for all users
- Support for authenticator apps and SMS

### Data Protection

#### Encryption
- All data in transit encrypted with SSL/TLS
- Passwords hashed with bcrypt
- Sensitive fields encrypted in database
- API keys never logged

#### Access Control
- Role-based access control (RBAC)
- Admin actions are logged
- Audit trail of all changes
- Principle of least privilege

#### Compliance
- GDPR compliant
- Data retention policies
- User data export capability
- Right to be forgotten

### Incident Response

#### Security Alerts
- Monitor for suspicious activity
- Automated alerts for:
  - Multiple login failures
  - Unusual trading patterns
  - API rate limit abuse
  - Database query anomalies

#### Breach Protocol
1. Identify and isolate affected systems
2. Notify affected users
3. Review logs and determine scope
4. Implement remediation
5. Document incident
6. Communicate resolution

---

## Support

### Getting Help
- Admin documentation: `/docs/ADMIN_GUIDE.md`
- API reference: `/docs/API.md`
- Technical support: admin-support@stock-trade.edu
- Emergency hotline: [phone number]

### Escalation
For critical issues:
1. Contact technical support team
2. Provide system logs and details
3. Follow incident response protocol

---

**Remember: With great power comes great responsibility. Always follow security best practices and platform policies.**