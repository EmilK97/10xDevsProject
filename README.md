# 10xDevsProjekt

A modern web application for efficient project management and team collaboration.

## Table of Contents
- [Project Description](#project-description)
- [Tech Stack](#tech-stack)
- [Getting Started Locally](#getting-started-locally)
- [Available Scripts](#available-scripts)
- [Project Scope](#project-scope)
- [Project Status](#project-status)
- [License](#license)

## Project Description

10xDevsProjekt is a comprehensive project management tool designed to streamline development workflows and enhance team collaboration. The application provides a centralized platform for managing projects, tracking tasks, and facilitating team communication.

### Key Features
- User authentication and authorization
- Project creation and management
- Task tracking and assignment
- Team collaboration tools
- Real-time updates
- Project analytics and reporting

## Tech Stack

### Backend
- Python 3.x
- FastAPI
- SQLAlchemy
- Pydantic
- PostgreSQL
- Alembic (Database migrations)

### Frontend
- React
- TypeScript
- Modern UI components
- Responsive design

### Development Tools
- Git for version control
- Docker (optional)
- VS Code recommended

## Getting Started Locally

### Prerequisites
- Python 3.x
- Node.js and npm
- PostgreSQL
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/10xDevsProjekt.git
cd 10xDevsProjekt
```

2. Set up the backend:
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration
```

3. Set up the frontend:
```bash
cd frontend
npm install
```

4. Database setup:
```bash
# Create PostgreSQL database
createdb 10xdevsprojekt

# Run migrations
alembic upgrade head
```

5. Run the application:
```bash
# Start backend server
uvicorn app.main:app --reload

# In a new terminal, start frontend
cd frontend
npm start
```

## Available Scripts

### Backend
```bash
# Run tests
pytest

# Run migrations
alembic upgrade head

# Generate migrations
alembic revision --autogenerate -m "description"
```

### Frontend
```bash
# Start development server
npm start

# Build for production
npm run build

# Run tests
npm test
```

## Project Scope

### Core Features
- User authentication and profile management
- Project creation and configuration
- Task management and tracking
- Team collaboration tools
- Project analytics and reporting

### Future Plans
- Real-time notifications
- Advanced analytics dashboard
- Integration with third-party tools
- Mobile application

## Project Status

The project is currently in active development. We are working on implementing core features and improving the user experience.

### Current Focus
- Core functionality implementation
- Performance optimization
- User interface improvements
- Documentation

### Known Issues
- Some features are still in development
- Performance optimization needed for large datasets
- Mobile responsiveness improvements planned

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 