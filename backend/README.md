# Real Estate ADK Agent

## Getting Started
### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.x

### Configuration Setup
#### Using Local Environment Variables

1. Copy `.env.example` to create a new `.env` file in the backend directory
2. Update the `.env` file with your credentials and configuration:
3. Verify that all required environment variables are properly added

### Running the Agent
1. Create a virtual environment
   ```bash
   python -m venv venv
   ```
2.Activate the virtual environment (Windows – Command Prompt)
   ```bash
   venv\Scripts\activate
   ```
3. Install dependencies
   ```bash
      pip install -r requirements.txt
   ```
4. Run the Claims Agent
   ```bash
   python app.py
   ```

## Developer Guide - Local PostgreSQL Setup
This guide explains how to set up and manage PostgreSQL locally using Docker Compose for development purposes.

### Prerequisites
Before you begin, ensure you have the following installed on your development machine:

### Project Structure
The relevant files for database setup are:
```
backend/
├── docker-compose.yml    # Docker Compose configuration
└── README.md            # This documentation
```

### PostgreSQL Docker Configuration
### Running PostgreSQL
1. Start the PostgreSQL container:
   ```bash
   docker-compose up -d
   ```
2. Verify the container is running:
   ```bash
   docker-compose ps
   ```
3. Stop and remove containers (including volumes):
   ```bash
   docker-compose down -v
   ```
4. Restart containers:
   ```bash
   docker-compose up -d
   ```

### Connecting to PostgreSQL

To connect to the PostgreSQL container and access the psql command line:

```bash
docker exec -it real_estate_db psql -U postgres -d real_estate_db
```

To exit the psql prompt:
```bash
\q
```

### Database Initialization and Schema Setup

1. After manual data entries or modifications, run the following sequence fix commands:
   ```sql
   -- Fix sequence for users table
   SELECT setval(pg_get_serial_sequence('users', 'user_id'), 
          COALESCE((SELECT MAX(user_id) FROM users), 1), TRUE);

   **Important**: Always run these sequence fix commands after making manual data entries in the database to maintain data integrity and avoid synchronization issues.


## Project Structure

```
backend/
├── database/          # Database repositories and connection management
├── models/            # Data models and schemas
├── routes/            # API routes and endpoints
├── services/          # Business logic
├── tests/             # Test files and configurations
├── utils/             # Utility functions and middleware
├── app.py             # Main application entry point
└── docker-compose.yml # Docker configuration
```