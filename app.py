from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data stores
students = []
courses = [
    {"id": 1, "name": "Mathematics"},
    {"id": 2, "name": "Physics"},
    {"id": 3, "name": "Computer Science"}
]
registrations = []

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Student Course Registration API"})

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data.get('email') or not data.get('password'):
        return jsonify({"error": "Email and password are required"}), 400
    students.append(data)
    return jsonify({"message": "Student registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    for student in students:
        if student['email'] == data['email'] and student['password'] == data['password']:
            return jsonify({"message": "Login successful"})
    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/courses', methods=['GET'])
def get_courses():
    return jsonify(courses)

@app.route('/register-course', methods=['POST'])
def register_course():
    data = request.get_json()
    if not data.get('email') or not data.get('course_id'):
        return jsonify({"error": "Email and course_id are required"}), 400
    registrations.append(data)
    return jsonify({"message": "Course registration successful"})

if __name__ == '__main__':
    app.run(debug=True)
