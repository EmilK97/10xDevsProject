# BoardGameTracker

A simple web application to help board game enthusiasts track their collection and identify rarely used games.

## Table of Contents
- [Project Description](#project-description)
- [Tech Stack](#tech-stack)
- [Getting Started Locally](#getting-started-locally)
- [Available Scripts](#available-scripts)
- [Project Scope](#project-scope)
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

### CI/CD & Hosting
- GitHub Actions for CI/CD pipelines
- DigitalOcean for hosting via Docker image

## Getting Started Locally

### Prerequisites
- Python 3.x
- Git

### Installation Steps
1. Clone the repository
   ```
   git clone https://github.com/yourusername/boardgametracker.git
   cd boardgametracker
   ```

2. Create and activate a virtual environment
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```
   pip install -r requirements.txt
   ```

4. Run database migrations
   ```
   python manage.py migrate
   ```

5. Create a superuser (for admin access)
   ```
   python manage.py createsuperuser
   ```

6. Start the development server
   ```
   python manage.py runserver
   ```

7. Access the application at http://localhost:8000

## Available Scripts

- `python manage.py runserver` - Start the development server
- `python manage.py migrate` - Apply database migrations
- `python manage.py makemigrations` - Create new migrations based on model changes
- `python manage.py test` - Run tests
- `python manage.py createsuperuser` - Create an admin user

## Project Scope

### Included in MVP
- Simple registration and login (username and password only)
- Board game library with user profiles
- Game categorization (two-player/multiplayer)
- Automatic warning and alert flags for unused games
- Last gameplay date updates
- Filtering games with alerts or warnings
- Admin panel for user management
- Web interface

### Not Included in Current Version
- Game quality ratings (1-10 scale)
- Email notifications about game alerts
- Game set sharing between users
- Integrations with other online platforms
- Mobile applications
- Game deletion or editing functionality
- Customizable time thresholds for alerts
- Password reset capability
- Account deletion functionality

## Project Status

This project is currently in development. The MVP is being implemented according to the requirements specified in the PRD.

### Success Metrics
1. 90% of users can register without assistance
2. 95% of users can add a new game to their library without assistance
3. 100% of games are correctly flagged with warnings and alerts
4. 80% of users understand the meaning of color markings for games

## License

This project is distributed under the MIT License. See the LICENSE file for details. 