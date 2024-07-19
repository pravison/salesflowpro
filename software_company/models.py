from django.db import models
from tinymce.models import HTMLField  

# Create your models here.
class CompanyInfor(models.Model):
    company_name = models.CharField(max_length=40)
    problem_statement = models.TextField(max_length=150)
    solution_statement = models.TextField(max_length=300)
    pitch = models.TextField(max_length=150)
    address = models.TextField()
    location = models.TextField()
    geoloction_pin = models.URLField(blank=True, null=True)
    county = models.TextField()
    country = models.TextField()
    phone = models.CharField(max_length=40)
    email = models.EmailField()
    featured = models.BooleanField(default=False)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.company_name
    
class AboutUs(models.Model):
    about_pitch = models.TextField()
    about_image = models.ImageField(blank=True, null=True)
    about_description = HTMLField()
    youtube_link = models.URLField(blank=True, null=True)
    featured = models.BooleanField(default=False)


    def __str__(self):
        return self.about_pitch
    
    @property
    def imageURL(self):
        try:
            url = self.about_image.url
        except:
            url = ''
        return url
    
class CallToAction(models.Model):
    message = models.TextField(max_length=150)
    reminder = models.TextField(max_length=100, blank=True, null=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.message
    
class Service(models.Model):
    service_name = models.CharField(max_length=100)
    icon_name = models.CharField(max_length=100)
    service_image = models.ImageField(blank=True, null=True)
    service_title = models.CharField(max_length=100)#delete this collumn
    service_overview = models.TextField(blank=True, null=True)
    service_description = models.TextField()
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.service_name
    
    @property
    def imageURL(self):
        try:
            url = self.service_image.url
        except:
            url = ''
        return url
    
class Benefit(models.Model):
    benefit_title = models.CharField(max_length=100)
    benefit_image = models.ImageField(blank=True, null=True)
    benefit_description = models.TextField()
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.benefit_title
    
    @property
    def imageURL(self):
        try:
            url = self.benefit_image.url
        except:
            url = ''
        return url
    
class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question

class Statistic(models.Model):
    statistic_name = models.CharField(max_length=100)
    statistic_icon = models.CharField(max_length=100, blank=True, null=True)
    statistic_number = models.IntegerField()
    featured = models.BooleanField(default= False)

    def __str__(self):
        return self.statistic_name

class Testimonial(models.Model):
    testimonial_name = models.CharField(max_length=100)
    testimonial_proffession = models.CharField(max_length=100)
    testimonial_image = models.ImageField(blank=True, null=True)
    testimonial_message = models.TextField()
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.testimonial_name
    
    @property
    def imageURL(self):
        try:
            url = self.testimonial_image.url
        except:
            url = ''
        return url

class Lead(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=17, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    subject= models.TextField(max_length= 150 , blank=True)
    message = models.TextField(max_length=1000)
    company_name =models.CharField(max_length=100,  blank=True, null=True)
    country =models.CharField(max_length=100,  blank=True, null=True)
    industry =models.CharField(max_length=100, blank=True, null=True)
    number_of_sales_reps =models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Pricing(models.Model):
    plan = models.CharField(max_length=170)
    price = models.IntegerField()
    new_price = models.IntegerField()
    feature1 = models.CharField(max_length=170, blank=True, null=True)
    feature2 = models.CharField(max_length=170, blank=True, null=True)
    feature3 = models.CharField(max_length=170, blank=True, null=True)
    feature4 = models.CharField(max_length=170, blank=True, null=True)
    feature5 = models.CharField(max_length=170, blank=True, null=True)
    feature6 = models.CharField(max_length=170, blank=True, null=True)
    recommended = models.BooleanField(default=False)
    limited_feature = models.BooleanField(default=False)

    def __str__(self):
        return self.plan

class PrivacyPolicy(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description
    
class TermsAndCondition(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description
    
class Staff(models.Model):
    name = models.CharField(max_length=199)
    staff_photo = models.ImageField(blank=True, null=True)
    role = models.CharField(max_length=199)
    description = models.TextField(max_length=500)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    tiktok = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


    @property
    def imageURL(self):
        try:
            url = self.staff_photo.url
        except:
            url = ''
        return url

class Compaarison(models.Model):
    name = models.CharField(max_length=199)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class WhyUs(models.Model):
    overview = models.TextField(max_length=500)
    image = models.ImageField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    first_point_icon = models.CharField(max_length =100)
    first_point_title = models.CharField(max_length =100)
    first_point_overview = models.TextField(max_length=400)
    second_point_icon = models.CharField(max_length =100)
    second_point_title = models.CharField(max_length =100)
    second_point_overview = models.TextField(max_length =400)
    third_point_icon = models.CharField(max_length =100)
    third_point_title = models.CharField(max_length =100)
    third_point_overview = models.TextField(max_length =400)

    def __str__(self):
        return self.first_point_title
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url