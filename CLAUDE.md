# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Flask-based web application that displays course information. The application uses a simple MVC-style architecture with Flask handling routing, view functions rendering templates, and a Course model managing course data.

## Development Environment

### Setup

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Unix/Mac
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Application

```bash
python src/app.py
```

The application will be available at `http://127.0.0.1:5000`

### Running Tests

```bash
# Run all tests
python -m unittest discover -s tests

# Run a specific test file
python -m unittest tests.test_app

# Run a specific test case
python -m unittest tests.test_app.AppTestCase.test_index
```

## Architecture

### Application Structure

The application follows a modular Flask design:

- **src/app.py**: Application entry point and Flask configuration. Routes are registered using `add_url_rule()` rather than decorators, which allows views to remain decoupled from Flask.
- **src/views.py**: View functions that handle HTTP requests and return rendered templates. Views are pure functions that don't depend on Flask decorators.
- **src/models.py**: Data models (currently in-memory Course objects stored in a list). No database backend - all course data is hardcoded.
- **src/templates/**: Jinja2 HTML templates with inheritance structure (layout.html as base)
- **src/static/css/**: CSS stylesheets for the application

### Key Design Patterns

1. **Separation of concerns**: Routes (app.py), view logic (views.py), and data (models.py) are separated into distinct modules.
2. **Template inheritance**: Templates use Jinja2's extends/block pattern with layout.html as the base template.
3. **Manual route registration**: Routes are registered with `add_url_rule()` instead of `@app.route()` decorators, allowing view functions to be imported and registered separately.

### Data Model

- Course data is stored in-memory as a list of Course objects in models.py
- No database or persistence layer exists
- To add new courses, modify the `courses` list in models.py

## Important Notes

- The views.py module imports only `render_template` from Flask, maintaining loose coupling
- Course IDs in URLs are currently just passed to templates but not used to look up actual Course objects
- The .env file contains Flask configuration (FLASK_APP and FLASK_ENV)
- Virtual environment (venv/) should not be committed to version control

## Add Unit tests

- Whenever you add any changes add unit tests and run and make sure the tests passes.
