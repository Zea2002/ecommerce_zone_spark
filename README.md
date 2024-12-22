E-Commerce Online Platform
Project Overview
This project implements the backend of an e-commerce platform with robust features and a focus on scalability, security, and deployment readiness.
Key Features
1.	User Authentication and Registration API: Secure user registration and login functionality with JWT-based authentication.
2.	E-commerce Functionality: Comprehensive support for managing products, categories, and stock with full CRUD operations.
3.	Advanced Features: PostgreSQL database integration, deployment readiness, and additional tools like Whitenoise for static file management.
________________________________________
Requirements
•	Python: 3.12
•	Django: 5.1.3
•	PostgreSQL: Hosted on Railway.app
________________________________________
Features
User Authentication
•	Registration and login APIs with JWT authentication.
•	Secure password handling using Django’s built-in utilities.
E-commerce Functionality
•	Models for Product, Category, and Stock.
•	Full CRUD operations for managing e-commerce data.
Database Integration
•	PostgreSQL database connection via a database URL stored securely in the .env file.
Deployment
•	Frontend hosted on Vercel.
•	PostgreSQL hosted on Railway.app.
•	Whitenoise used for serving static files in production environments.
________________________________________
Setup Instructions
Step 1: Clone the Repository
git clone https://github.com/Zea2002/ecommerce_zone_spark
Step 2: Set Up a Virtual Environment
python3.12 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Step 3: Install Dependencies
pip install -r requirements.txt
Step 4: Configure Environment Variables
1.	Create a .env file in the project root.
2.	Add the following variables: 
3.	DEBUG=True
4.	DATABASE_URL=your-database-url
Replace your-database-url with your PostgreSQL URL from Railway.app.
Step 5: Apply Migrations
python manage.py makemigrations
python manage.py migrate
Step 6: Run the Development Server
python manage.py runserver
Access the application at: http://127.0.0.1:8000/
Step 7: Admin Panel
Create a superuser to access the admin panel:
python manage.py createsuperuser
Access the admin panel at: http://127.0.0.1:8000/admin/
________________________________________
API Endpoints
User Authentication
1.	Register a New User
o	Method: POST
o	URL: https://ecommerce-zone-spark-6zop.vercel.app/user/register/
2.	Log In and Retrieve a JWT Token
o	Method: POST
o	URL: https://ecommerce-zone-spark-6zop.vercel.app/user/login/
3.	Profile Management
o	View Profile 
	Method: GET
	URL: https://ecommerce-zone-spark-6zop.vercel.app/user/profile/
o	Update Profile 
	Method: PUT or PATCH
	URL: https://ecommerce-zone-spark-6zop.vercel.app/user/profile/
o	Retrieve Individual Profile 
	Method: GET
	URL: https://ecommerce-zone-spark-6zop.vercel.app/user/profile/<id>
o	4.all users:
o	Api - https://ecommerce-zone-spark-6zop.vercel.app/user/users/
o	For individual-  https://ecommerce-zone-spark-6zop.vercel.app/user/users/<id>
Product Management
1.	Create a Product 
o	Method: POST
o	URL: https://ecommerce-zone-spark-6zop.vercel.app/product/products/
2.	Retrieve All Products 
o	Method: GET
o	URL: https://ecommerce-zone-spark-6zop.vercel.app/product/products/
3.	Update a Product 
o	Method: PUT
o	URL: https://ecommerce-zone-spark-6zop.vercel.app/product/products/<id>
4.	Delete a Product 
o	Method: DELETE
o	URL: https://ecommerce-zone-spark-6zop.vercel.app/product/products/<id>
Category Management
1.	Base URL: https://ecommerce-zone-spark-6zop.vercel.app/product/categories/
Stock Management
1.	Base URL: https://ecommerce-zone-spark-6zop.vercel.app/product/stocks/
________________________________________
Deployment Instructions
1.	Install Whitenoise 
2.	pip install whitenoise
3.	Collect Static Files 
4.	python manage.py collectstatic
5.	Deploy to Hosting Platform 
o	Use .env for environment-specific settings.
o	Deploy on platforms like Vercel or Railway.app.
________________________________________
Testing API with Postman
Example: Register a User
•	Method: POST
•	URL: https://ecommerce-zone-spark-6zop.vercel.app/user/register/
•	Headers: 
•	{
•	  "Content-Type": "application/json"
•	}
•	Body: 
•	{
•	  "username": "example_user",
•	  "password": "secure_password",
•	  "email": "example@example.com"
•	}
Notes
•	Replace <JWT_TOKEN> with the token obtained from the login endpoint.
•	Ensure all authenticated requests include appropriate headers.
________________________________________
Contact
For any issues or inquiries, please contact: rahmanzea31@gmail.com.

