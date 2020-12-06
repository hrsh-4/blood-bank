<h1>Blood Bank</h1>

This application has 2 types of users 

- Hospital
	- register
	- login
	- add sample of blood available to the blood bank
	- can see requests of receiver for particular blood sample


- Receiver
  - register
  - login
  - can see all blood samples added to the blood bank by different hospitals 
  - can request a hospital for a particular blood sample

Any user can see blood samples but can only request for it when logged in

Instructions to run

1. Make sure you have Python installed.

2. Install Django

   <code> pip install django==2.2 </code>

3. Go to project directory and run the following commands:

    <code> python manage.py makemigrations </code>
    <br/>
    
    <code> python manage.py migrate </code>
    <br/>
    
    <code> python manage.py runserver </code>
    
 4. Go to http://localhost:8000/ in your browser
    
