from flask import render_template, request
from models import courses
import re

def index():
    return render_template('index.html', courses=courses)

def course(course_id):
    # Convert course_id to integer and get the course from the list
    course_index = int(course_id) - 1
    if 0 <= course_index < len(courses):
        selected_course = courses[course_index]
        return render_template('course.html', course=selected_course)
    else:
        return "Course not found", 404

def contact():
    """Handle contact form display and submission"""
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        address = request.form.get('address', '').strip()

        # Server-side validation
        errors = {}

        if not name:
            errors['name'] = 'Please enter your name'

        if not email:
            errors['email'] = 'Please enter a valid email address'
        elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            errors['email'] = 'Please enter a valid email address'

        if not address:
            errors['address'] = 'Please enter your address (minimum 10 characters)'
        elif len(address) < 10:
            errors['address'] = 'Please enter your address (minimum 10 characters)'

        if errors:
            # Return form with errors
            return render_template('contact.html', errors=errors, name=name, email=email, address=address)

        # Process successful submission
        print(f"Contact form submission: Name: {name}, Email: {email}, Address: {address}")

        # Return success
        return render_template('contact.html', success=True)

    # GET request - render empty form
    return render_template('contact.html')