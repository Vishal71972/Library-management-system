
# Library Management System

A simple Library Management System built using Flask, MySQL, and Bootstrap.  
This project allows Admin and Students to manage books in a library.

## Features

- Admin Login
- Student Login
- Add Books (Admin)
- View Books
- Delete Books
- Issue Book to Student
- Return Book


## Technologies Used

- Python
- Flask
- MySQL
- HTML
- Bootstrap
- Jinja2 Templates



## Project Structure
``` 

library_management_system/
│
├── app.py
│
├── templates/
│   ├── login.html
│   ├── admin_dashboard.html
│   ├── student_dashboard.html
│   ├── add_book.html
│   ├── issue_book.html
│   ├── return_book.html
│   └── view_books.html
│
├── static/
│   ├── css/
│   └── js/
│
└── database/
```

## Database Tables

### Admin

 | id| admin_id    | password              |
| :-------- | :------- | :------------------------- |
|           |             |             |                

### students

 | id| student_id    | name            |  password  |
| :-------- | :------- | :--------------- |  :-------------   |
|            |        |        |          |


### Books

 | id| book_name   | author  |    category     |   quantity  |
| :-------- | :------- | :-------- |:-------  |  :-----------------   |
|   

### Issue Books

 | id| student_id    | book_id           |   issue_date  |
| :-------- | :------- | :------------------------- |  :-------------   |        
|

## Installation

1. Clone the repository
2. Install Python dependencies
3. Start MySQL server
4. Create database `library_db`
5. Run the application

```bash
pip install flask
pip install mysql-connector-python
```
