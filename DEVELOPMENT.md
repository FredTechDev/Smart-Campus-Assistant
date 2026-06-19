# Development Guide

## Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/FredTechDev/Smart-Campus-Assistant.git
cd Smart-Campus-Assistant
```

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp ../.env.example .env

# Run migrations
alembic upgrade head

# Start the server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

API will be available at: http://localhost:8000
API Docs: http://localhost:8000/docs

### 3. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

Frontend will be available at: http://localhost:5173

### 4. Database Setup

#### Using Docker:

```bash
docker run --name postgres-smart-campus \
  -e POSTGRES_USER=user \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=smart_campus \
  -p 5432:5432 \
  -d postgres:15
```

#### Or use Docker Compose:

```bash
docker-compose up -d db
```

### 5. ML Setup

```bash
cd ml

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run notebooks in order
jupyter notebook
```

## Docker Compose Setup

Start all services at once:

```bash
docker-compose up -d
```

This starts:
- PostgreSQL database (port 5432)
- FastAPI backend (port 8000)
- React frontend (port 3000)

View logs:

```bash
docker-compose logs -f [service-name]
```

Stop services:

```bash
docker-compose down
```

## Database Migrations

Create a new migration:

```bash
cd backend
alembic revision --autogenerate -m "Description of changes"
alembic upgrade head
```

## Testing

### Backend Tests

```bash
cd backend
pytest tests/ -v
```

### Frontend Tests

```bash
cd frontend
npm run test
```

## Code Style

### Python

```bash
# Format with black
black backend/

# Lint with flake8
flake8 backend/

# Type check with mypy
mypy backend/
```

### JavaScript

```bash
cd frontend
npm run lint
npm run format
```

## Project Structure Details

### Backend (`/backend`)
- `app/main.py` - FastAPI application entry point
- `app/api/` - Route handlers
- `app/models/` - Pydantic schemas and SQLAlchemy models
- `app/services/` - Business logic
- `app/core/` - Configuration and security
- `app/db/` - Database setup and migrations

### Frontend (`/frontend`)
- `src/components/` - Reusable React components
- `src/pages/` - Page components
- `src/store/` - Redux store configuration
- `src/services/` - API client and utilities

### ML (`/ml`)
- `notebooks/` - Jupyter notebooks for experimentation
- `src/` - Reusable Python modules
- `data/` - Raw and processed data
- `models/` - Serialized trained models

## Useful Commands

### Backend

```bash
# Format code
black backend/

# Run tests
pytest backend/tests/ -v --cov

# Start with hot reload
uvicorn app.main:app --reload
```

### Frontend

```bash
# Development server
npm run dev

# Build for production
npm run build

# Run tests
npm run test
```

### Database

```bash
# Connect to PostgreSQL
psql -U user -d smart_campus -h localhost
```

## Troubleshooting

### Port Already in Use

```bash
# Find and kill process on port 8000
lsof -ti:8000 | xargs kill -9
```

### Database Connection Issues

Ensure the DATABASE_URL in `.env` is correct:

```
postgresql://user:password@localhost:5432/smart_campus
```

### Module Not Found

Make sure virtual environment is activated and dependencies are installed:

```bash
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Next Steps

1. Set up local environment
2. Start with data collection and preprocessing (`/ml`)
3. Build ML models and pipelines
4. Create FastAPI endpoints
5. Develop React components
6. Connect frontend to backend
7. Deploy using Docker
