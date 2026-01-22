# Project Overview

This is a simple web application built with Python and Flask. It displays a list of courses and their details. The application follows a simple Model-View-Controller (MVC) like pattern where:
- `src/app.py` is the main entry point of the application.
- `src/views.py` contains the view functions for handling requests.
- `src/models.py` defines the data models for managing course data.
- `src/templates` contains the HTML templates for rendering the pages.

The main technologies used are Python and Flask.

# Building and Running

## Installation

1. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the application

To run the application, execute the following command:
```
python src/app.py
```
The application will be available at `http://127.0.0.1:5000`.

## Testing

To run the tests, use:
```
python -m unittest discover -s tests
```

# Development Conventions

- The application follows the standard Flask project structure.
- The view functions are separated from the main application file.
- The data models are defined in a separate file.
- The HTML templates are stored in the `templates` directory.
