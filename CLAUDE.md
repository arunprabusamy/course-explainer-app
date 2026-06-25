# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Run the app (development)
python src/app.py

# Run all tests
python -m unittest discover -s tests

# Run a specific test
python -m unittest tests.test_app.AppTestCase.test_index

# Install dependencies
pip install -r requirements.txt
```

## Architecture

Simple Flask MVC app with three layers:

- **[src/app.py](src/app.py)** — Flask app factory; registers URL rules (`/` → `index`, `/course/<course_id>` → `course`). Routes are registered with `add_url_rule()` instead of decorators.

- **[src/views.py](src/views.py)** — View functions that render Jinja2 templates. Currently passes `course_id` to templates but does **not** pass `Course` model objects — this is a known gap (templates reference `course.title`, `course.description`, etc. but no model lookup occurs).

- **[src/models.py](src/models.py)** — `Course` class with fields `title`, `description`, `instructor`, `duration`. A hardcoded `courses` list holds 3 sample courses. Not yet consumed by views.

- **[src/templates/](src/templates/)** — Jinja2 templates. `layout.html` is the base shell (header, nav, footer, content block). `index.html` and `course.html` each re-declare `<html>`/`<head>` — there's a template inheritance inconsistency: `index.html` uses `{% include 'layout.html' %}` while `course.html` uses `{% extends 'layout.html' %}`. Neither extends properly, resulting in duplicated HTML structure.

- **[src/static/css/styles.css](src/static/css/styles.css)** — CSS with some duplicated/conflicting rules (`.container`, `body`, `header`, `h1`, `.footer` are defined twice with different values).

- **[tests/test_app.py](tests/test_app.py)** — Flask test client tests. Patches `sys.path` to import `app` from `src/`.

### Known issues in the codebase

1. **Model data not wired to views** — `views.py` imports no models and passes no course data to templates. `course.html` references `course.title`/`.description`/`.instructor`/`.duration`/`.topics`, but none of these are provided in the render context.
2. **Template inheritance broken** — Both `index.html` and `course.html` include their own `<html>`, `<head>`, and `<body>` tags despite using `layout.html`. `index.html` uses `{% include %}` instead of `{% extends %}`.
3. **CSS duplication** — Some selectors (`.container`, `header`, `body`, `.footer`) are defined twice with different values.

## Development Workflow

- Whenever you add any changes, add unit tests and run it and make sure the tests pass.
