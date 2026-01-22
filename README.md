Student Course Registration System

This is a simple web-based Student Course Registration System built using Python and Flask. It allows students to register, log in, view available courses, and register for them.

---

🔧 Features

- Student registration and login  
- View list of available courses  
- Register for a course  
- RESTful API endpoints  

---

📁 Project Structure

`
student-course-registration/
│
├── app.py           # Flask backend
├── README.md        # Project documentation
└── requirements.txt # (Optional) Python dependencies
`
---

🚀 How to Run

1. Install Flask:

`bash
pip install flask
`
2.Run the app:
`
python app.py
`
 3.open your browser and go to:
http://127.0.0.1:5000

API Endpoints

| Method  | Endpoint |Description                   |
|--------|------------------|-------------------------------|
| POST   | /register        | Register a new student        |
| POST   | /login           | Student login                 |
| GET    | /courses         | View available courses        |
| POST   | /register-course | Register for a course         |

Tools Used

- Python  
- Flask  
- Postman or Hoppscotch (for testing)  

---

SDLC Phases

1. Requirement Analysis
- Define system goals and user needs  
- Identify functional and non-functional requirements  

2. System Design
- Plan endpoints, data structures, and architecture  
- Design RESTful API routes  

3. Implementation
- Code the backend using Flask  
- Create endpoints for registration, login, course listing, and course registration  

4. Testing
- Use Postman or Hoppscotch to test all endpoints  
- Validate input and output for each route  

5. Deployment
- Push the project to GitHub  
- Share the repository link for access and review  

6. Maintenance
- Add validations and error handling  
- Upgrade to persistent storage (e.g., SQLite or PostgreSQL)  
- Add authentication tokens (e.g., JWT)  

---

👨‍💻 Author

Juwon  
GitHub: https://github.com/Michael1122you-sys

## 📘 Software Development Life Cycle (SDLC)

Software Development Life Cycle (SDLC)

1. Planning
The goal of this project was to build a simple web-based API that allows students to register, view available courses, and enroll in them. The project was chosen to demonstrate a practical application of backend development using Python and Flask. Flask was selected for its simplicity, flexibility, and suitability for building lightweight RESTful APIs.

---

2. System Analysis
During the analysis phase, the core requirements of the system were identified:
- Students should be able to register with their details.
- Students should be able to view available courses.
- Students should be able to enroll in courses.
- The system should provide clear and consistent JSON responses for all API interactions.

---

3. System Design
The system was designed with the following components:
- Entities:
  - Student: Represents a user who can register and enroll in courses.
  - Course: Represents a course available for enrollment.
  - Registration: Represents the relationship between students and courses.
- API Endpoints:
  - GET /: Returns a welcome message.
  - POST /register: Registers a new student.
  - GET /courses: Lists all available courses.
  - POST /enroll: Enrolls a student in a selected course.

All route names and data fields were consistently named to match the design and implementation.

---

4. Implementation
The application was implemented using Python and the Flask framework. The main logic resides in the app.py file. The app uses in-memory data structures (dictionaries and lists) to simulate a database. Each endpoint is defined using Flask routes and returns JSON responses. The project structure is simple and easy to understand, making it ideal for educational purposes.

---

5. Testing
The application was tested locally by running the Flask server with:

```bash
python app.py
```

Testing was performed using:
- A web browser for GET requests (e.g., visiting http://127.0.0.1:5000/)
- API testing tools like Hoppscotch and Postman for POST requests with JSON payloads

Each endpoint was tested to ensure it returned the correct response and handled errors appropriately.

---

6. Deployment
The project was deployed locally and then pushed to a public GitHub repository for submission and sharing 

🔗 GitHub Repository: https://github.com/micheal1122you-sys/student-course-registration

The repository includes:
- app.py – Main application file
- README.md – Documentation and setup instructions
- (Optional) requirements.txt – List of dependencies

---

7. Maintenance
The project is structured to allow easy updates and future improvements. Potential enhancements include:
- Adding persistent storage using a database (e.g., SQLite or PostgreSQL)
- Implementing user authentication
- Expanding the API to include admin features, course creation, and student dashboards
- Deploying the app to a cloud platform like Render or Replit for public access
