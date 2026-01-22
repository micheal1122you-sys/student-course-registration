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
