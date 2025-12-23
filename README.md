📂 **Item_Selling_Project**

A secure and scalable Item Selling REST API built using Flask and SQLAlchemy, featuring JWT-based authentication & authorization. This project demonstrates backend development best practices, RESTful API design, and database integration.


🚀 **Features**

1.User Registration & Login

2.JWT-based Authentication & Authorization

3.Role-based access control (Admin / User)

4.CRUD operations for items

5.Secure password hashing

6.Database integration using SQLAlchemy ORM

7.RESTful API architecture

8.Error handling & validation

9.Version control using Git



📁**Project Structure**

item_selling_project/
│
├── app.py
├── models.py
├── routes/
│   ├── auth.py
│   ├── items.py
│
├── database.db
├── requirements.txt
├── config.py
├── README.md
└── venv/



🔐 **Authentication & Authorization**

1.JWT (JSON Web Tokens) are used for securing API endpoints

2.Access tokens are required for protected routes

3.Role-based access:

  3.1 : Admin: Can add, update, and delete items

  3.2 :  User: Can view and purchase items


🔒 **Security Practices**

1.Passwords stored using hashing

2.JWT tokens for stateless authentication

3.Protected routes using decorators

4.Input validation & error handling

📌** Version Control**

1.Git used for source control

2.Meaningful commit messages

3.Feature-based commits

🎯 **Future Enhancements**

1.Item purchase & order management

2.Pagination & filtering

3.Refresh tokens

4.Docker deployment

5.Frontend integration (React / HTML-CSS-JS)

6.Payment gateway integration
