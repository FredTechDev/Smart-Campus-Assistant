# Smart Campus Assistant

An AI-powered educational platform that predicts student performance, analyzes attendance patterns, recommends courses, and provides academic support through an intelligent chatbot.

## Features

- **Predict Student Performance** - ML models to forecast academic outcomes
- **Attendance Analytics** - Track and analyze student attendance patterns
- **Course Recommendation System** - Personalized course suggestions
- **AI Chatbot** - Intelligent chatbot for academic FAQs
- **Dashboard for Lecturers** - Comprehensive analytics and insights

## Tech Stack

- **Backend**: Python, FastAPI
- **Machine Learning**: Scikit-Learn, Pandas, NumPy
- **Frontend**: React, Redux, Axios
- **Database**: PostgreSQL
- **DevOps**: Docker, Docker Compose
- **Deployment**: AWS/GCP (TBD)

## Project Structure

```
Smart-Campus-Assistant/
├── backend/                 # FastAPI application
│   ├── app/
│   │   ├── main.py
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── students.py
│   │   │   ├── attendance.py
│   │   │   ├── courses.py
│   │   │   └── chatbot.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── db_models.py
│   │   │   └── schemas.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── ml_service.py
│   │   │   ├── attendance_service.py
│   │   │   ├── recommendation_service.py
│   │   │   └── chatbot_service.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   └── db/
│   │       ├── database.py
│   │       └── migrations/
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
├── ml/                      # ML pipeline and models
│   ├── notebooks/
│   │   ├── 01_exploratory_analysis.ipynb
│   │   ├── 02_data_preprocessing.ipynb
│   │   ├── 03_model_training.ipynb
│   │   └── 04_model_evaluation.ipynb
│   ├── src/
│   │   ├── data_loader.py
│   │   ├── preprocessor.py
│   │   ├── models.py
│   │   ├── trainer.py
│   │   └── evaluator.py
│   ├── data/
│   │   ├── raw/
│   │   └── processed/
│   ├── models/
│   │   └── (trained models)
│   └── requirements.txt
├── frontend/                # React dashboard
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Dashboard.jsx
│   │   │   ├── StudentPerformance.jsx
│   │   │   ├── AttendanceAnalytics.jsx
│   │   │   ├── CourseRecommendations.jsx
│   │   │   ├── Chatbot.jsx
│   │   │   └── Navigation.jsx
│   │   ├── pages/
│   │   ├── store/
│   │   │   └── (Redux store)
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── App.jsx
│   │   └── index.jsx
│   ├── package.json
│   ├── vite.config.js
│   └── Dockerfile
├── database/                # PostgreSQL
│   ├── init.sql
│   ├── migrations/
│   └── seeds/
├── docker-compose.yml
├── .gitignore
├── .env.example
└── DEVELOPMENT.md
```

## Getting Started

### Prerequisites
- Docker and Docker Compose
- Python 3.11+
- Node.js 18+
- PostgreSQL (or use Docker)

### Quick Start with Docker

```bash
# Clone the repository
git clone https://github.com/FredTechDev/Smart-Campus-Assistant.git
cd Smart-Campus-Assistant

# Create environment file
cp .env.example .env

# Start all services
docker-compose up -d

# Backend API: http://localhost:8000
# Frontend: http://localhost:3000
# API Docs: http://localhost:8000/docs
```

### Local Development

See [DEVELOPMENT.md](./DEVELOPMENT.md) for detailed local setup instructions.

## Development Roadmap

1. **Phase 1: Data Pipeline** (Weeks 1-2)
   - [ ] Collect and organize student data
   - [ ] Clean and preprocess data
   - [ ] Create data pipeline

2. **Phase 2: ML Models** (Weeks 3-4)
   - [ ] Train baseline models
   - [ ] Implement performance prediction
   - [ ] Build attendance analytics
   - [ ] Develop recommendation system

3. **Phase 3: Backend API** (Weeks 5-6)
   - [ ] Set up FastAPI application
   - [ ] Create database schema
   - [ ] Build API endpoints
   - [ ] Implement model serving

4. **Phase 4: Frontend Dashboard** (Weeks 7-8)
   - [ ] Design UI/UX
   - [ ] Build React components
   - [ ] Implement state management
   - [ ] Connect to API

5. **Phase 5: AI Chatbot** (Week 9)
   - [ ] Integrate LLM/chatbot API
   - [ ] Create chatbot service
   - [ ] Build chat interface

6. **Phase 6: Deployment** (Week 10)
   - [ ] Configure Docker containers
   - [ ] Set up CI/CD pipeline
   - [ ] Deploy to cloud
   - [ ] Performance monitoring

## API Endpoints (TBD)

### Students
- `GET /api/students` - List all students
- `GET /api/students/{id}` - Get student details
- `GET /api/students/{id}/performance` - Get performance prediction

### Attendance
- `GET /api/attendance/analytics` - Get attendance analytics
- `POST /api/attendance/record` - Record attendance

### Courses
- `GET /api/courses/recommendations` - Get course recommendations
- `GET /api/courses` - List available courses

### Chatbot
- `POST /api/chatbot/query` - Send message to chatbot

## Contributing

1. Create a feature branch
2. Make your changes
3. Submit a pull request

## License

MIT License

## Author

FredTechDev
