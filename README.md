# BoardGameTracker

A simple web application designed to help users track their board game collection and identify rarely used games.

## Table of Contents
- [Project Description](#project-description)
- [Tech Stack](#tech-stack)
- [Getting Started Locally](#getting-started-locally)
- [Available Scripts](#available-scripts)
- [Project Structure](#project-structure)
- [Data Models](#data-models)
- [Important Information](#important-information)
- [Project Status](#project-status)
- [License](#license)

## Project Description

BoardGameTracker is a web application designed to help users track their board game collection and identify rarely used games. The app allows users to maintain their own board game library, track last gameplay dates, and automatically flag games that haven't been used for a long time.

### Main Features
- Simple registration and login system
- Board game library management
- Automatic flagging of rarely used games (warnings after 1 year, alerts after 3 years)
- Last gameplay date updates with a simple "Played Today" button
- Collection filtering and browsing
- Admin panel for user and game management

This application is non-commercial and was created as a demonstration project for a course.

## Tech Stack

### Frontend
- HTML, CSS, and vanilla JavaScript
- Simple, modern design with white background and light blue interactive elements
- No complex frameworks - focusing on simplicity and ease of implementation

### Backend
- Python with Django framework
- SQLite database (built-in with Django)
- Django's authentication system for user management
- Django Admin panel for administrative functions

## Getting Started Locally

### Prerequisites
- Python 3.10.11
- Django 4.x
- SQLite (default database)

### Installation Steps
1. Clone the repository:
```bash
git clone <repository-url>
cd boardGameTracker
```

2. (Optional) Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate  # Windows
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database:
```bash
# Generate migration files based on models
python manage.py makemigrations boardGameApp

# Apply migrations to the database
python manage.py migrate
```

5. Create an admin account:
```bash
python manage.py createsuperuser
```

6. Start the development server:
```bash
python manage.py runserver
```

7. Access the application at http://localhost:8000

## Project Structure

- `boardGameTracker/` - main Django project directory
  - `boardGameApp/` - board game management application
    - `models.py` - data models (BoardGame, UserProfile)
    - `views.py` - view logic
    - `templates/` - HTML templates
    - `static/` - static files (CSS, JavaScript)

## Data Models

The application contains two main models:

1. `UserProfile` - extension of Django's standard User model
2. `BoardGame` - board game model with fields:
   - name
   - owner (relationship with User)
   - game type (two-player/multiplayer)
   - last played date
   - status (normal/warning/alarm) - automatically calculated

## Important Information

### Database Migrations

After any changes to the models (`models.py`), you need to generate and apply new migrations:

```bash
python manage.py makemigrations boardGameApp  # generates new migrations
python manage.py migrate  # applies migrations to the database
```

Migrations are crucial for:
- Creating the initial database structure
- Updating the structure after model changes
- Maintaining data consistency

### Admin Panel Access

The admin panel is available at `/admin/` after logging in with superuser credentials.

## Project Status

This project is currently in development. The MVP is being implemented according to the requirements specified in the PRD.

### Success Metrics
1. 90% of users can register without assistance
2. 95% of users can add a new game to their library without assistance
3. 100% of games are correctly flagged with warnings and alerts
4. 80% of users understand the meaning of color markings for games

## License

This project is distributed under the MIT License. See the LICENSE file for details. 