class Course:
    def __init__(self, title, description, instructor, duration, topics=None):
        self.title = title
        self.description = description
        self.instructor = instructor
        self.duration = duration
        self.topics = topics if topics is not None else []

    def __repr__(self):
        return f"<Course {self.title} by {self.instructor}>"

courses = [
    Course("Introduction to Python", "Learn the basics of Python programming.", "John Doe", "4 weeks",
           ["Variables and Data Types", "Control Structures", "Functions", "Object-Oriented Programming"]),
    Course("Web Development with Flask", "Build web applications using Flask.", "Jane Smith", "6 weeks",
           ["Flask Basics", "Routing and Templates", "Forms and Validation", "Database Integration", "Deployment"]),
    Course("Data Science Fundamentals", "An introduction to data science concepts and tools.", "Alice Johnson", "8 weeks",
           ["Statistics Basics", "Python for Data Science", "Data Visualization", "Machine Learning Introduction"]),
    Course("Go Programming Essentials", "Master Go programming language from basics to advanced concepts.", "Robert Chen", "5 weeks",
           ["Go Basics and Syntax", "Goroutines and Concurrency", "Channels and Synchronization", "Web Services with Go", "Testing and Deployment"]),
]