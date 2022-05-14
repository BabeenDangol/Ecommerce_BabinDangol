a. Objective: -To install Python, its framework, and database tools. 
              -To develop a project using the Django framework.  
              -To verify the frontend and backend in the browser. 
              -To add other users and perform CRUD operations.
              -To create product module named Brands.

b. Introduction:E-commerce refers to a business that conducts its operations over the Internet. Python is a programming language that may be used to create websites and applications, automate processes, and analyze data. Python is a programming language with many uses. To summarize, Python may be used to create a wide range of applications and is not limited to a single problem. Django is a Python web framework that allows for quick development with a simple, functional design. SQLite is a C language package that implements a full-featured SQL database engine that is tiny, quick, self-contained, and dependable. GitHub is a code hosting and collaboration platform.

c. Procedure:First we initialize django project: 
              django-admin startproject ecommerce_lab1 
              Then, we initialize the database: python3 manage.py migrate To create a super user:
              To run the project: python manage.py runserver
              To add a module: python manage.py startapp product_module
              Then, we go to settings.py and add the module to 'Installed Apps' section: INSTALLED_APPS = [ ..., 'product_module' ]
              Now, we add code for Brand in models.py: class Brand(models.Model): name = models.CharField(max_length=200) is_active = models.BooleanField()
              Then, we ensure that the database table for added model is created properly: python manage.py makemigrations python manage.py migrate
              Now, we add the following code to admin.py: from .models import Brand admin.site.register(Brand)
d. Conclusion: As a result, in the first lab, we used the Django framework to create our own project. A superuser has been formed. I started the server, made sure the database was running, and tested the frontend and backend. I ran a CRUD operation on the server and installed the branding module.
