# Lab 2 Adding Brand, Category and Product


  ## a. Introduction:
  
  In our first lab, we made a produvt module. Presently, we include a brand, product and category within the product module which encompasses a structure of the er graph as appeared underneath:
  ![Screenshot1](https://github.com/BabeenDangol/Ecommerce_BabinDangol/blob/main/lab_manual/images/ER-product_module.png?raw%3Dtrue)
  
   ## b.Objective: 
 
        1.To Add Product, Brand, Category and Color
        2.To perform CRUD operations on all three models.  
        3.To verify the frontend and backend in the browser. 
        4.To get more information about the admin.py, models.py as well as other files that django framework provides
        5.To get more information about adding models and how models.py works

  ## c. Procedure:

**1. Adding the model Brand in the models.py**

  We downloaded the software and environments required for the project. Those were:

    class Category(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField()
    class Meta:
    verbose_name_plural = "Categories"

**2. Adding the model Product in the models.py**

    class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    quantity = models.IntegerField()
    image_url = models.CharField(max_length=500)
    color_code = models.CharField(max_length=20)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    registered_on = models.DateTimeField()
    is_active = models.BooleanField()
      
      
 **3. Making changes to the db by performing migrations** 
 
    python manage.py makemigrations
    python manage.py migrate
              
  **4. Adding the following code to admin.py for enabling CRUD operations in the admin site**

    from .models import Brand, Category, Product
    admin.site.register(Brand)
    admin.site.register(Category)
    admin.site.register(Product)
  **5. Finally, running the project and performing CRUD operations on Brand, Category and Product**

    python manage.py runserver

    

  ## d. Output
  **1. Installation of python| pip**
  
  ![Screenshot 2022-05-19 200206](https://user-images.githubusercontent.com/104016877/169320792-2c6f79fe-bdcb-4f56-88a7-1e2d1819bb6d.jpg)
  
 **2. Creation of project folder**
  
  ![Screenshot (140)](https://user-images.githubusercontent.com/104016877/169320992-2c80e80c-dad7-4f71-88be-e6ae7e789b47.png)
  
  **3. Migration**
  ![Screenshot (142)](https://user-images.githubusercontent.com/104016877/169321145-4962e6da-7c1e-4cc4-ae5e-658b4b649f03.png)
  
 **4. Creating superuser**
  ![Screenshot (143)](https://user-images.githubusercontent.com/104016877/169321330-f2701a5e-d205-45d6-b4b8-92413e3106a8.png)
  
  **5. Running server**
  ![Screenshot (144)](https://user-images.githubusercontent.com/104016877/169321535-95662287-26d9-43ed-89c1-28ffb5c0d106.png)
  ![Screenshot (145)](https://user-images.githubusercontent.com/104016877/169321553-0f57b487-3d0c-49e2-ac2a-c57b5998c898.png)
  ![Screenshot (146)](https://user-images.githubusercontent.com/104016877/169321558-621ffa95-a9d6-495a-8917-e76e171bb59a.png)
  **6. Logging In**
  ![Screenshot (147)](https://user-images.githubusercontent.com/104016877/169321604-4ef824c0-fbb7-434a-b351-35968cc6c844.png)
  
  **7. Git initialization**
  ![Screenshot (148)](https://user-images.githubusercontent.com/104016877/169321822-bcbd8020-f83e-4af2-8cdd-89e10767bb0d.png)

  ## e. Conclusion:
  
  As a result, in the first lab, we built our own project using the Django framework. There is now a superuser. I started the server, verified that the database was up and running, and then tested both the frontend and backend. On the server, I performed a CRUD activity and installed the branding module.
