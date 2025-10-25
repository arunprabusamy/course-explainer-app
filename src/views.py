from flask import render_template
from models import courses

def index():
    return render_template('index.html')

def course(course_id):
    # Convert course_id to integer and get the course from the list
    course_index = int(course_id) - 1
    if 0 <= course_index < len(courses):
        selected_course = courses[course_index]
        return render_template('course.html', course=selected_course)
    else:
        return "Course not found", 404