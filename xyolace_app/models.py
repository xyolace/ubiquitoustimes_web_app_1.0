from django.db import models
from datetime import datetime
from django.utils.text import slugify

# Create your models here.

class A0PAGETOP(models.Model):
    Title = models.CharField(max_length = 30)
    Image = models.ImageField(upload_to = 'Page Logo', default= None)
    
    def __str__(self):
        return self.Title

class A1NAVBAR(models.Model):
    Title = models.CharField(max_length = 30, null = True, default = None, blank = True)
    Tag_line = models.CharField(max_length = 50, null = True, default = None, blank = True)
    Nav_links = models.CharField(max_length = 30)
    Link_href = models.URLField()

    def __str__(self):
        return self.Nav_links
    
class A2TOPPICKS(models.Model):
    Field = models.CharField(max_length = 30)
    Title = models.CharField(max_length = 50)
    Text = models.TextField()
    Image = models.ImageField(upload_to= 'Top Picks', null = True, blank = True)
    Time = models.DateTimeField(default = datetime.now, blank = True)
    Source = models.CharField(max_length = 50, blank = True)
    Source_link = models.URLField(blank = True, null = True)
    KEYWORD = models.CharField(max_length = 150)
    Description = models.TextField()

    def __str__(self):
        return self.Title
    
class A3NEWSTODAY(models.Model):
    Title = models.TextField()
    Text = models.TextField()
    Source = models.CharField(max_length = 50, blank = True)
    Source_link = models.URLField(blank = True, null = True)
    Image = models.ImageField(upload_to= 'New Post')
    Time = models.DateTimeField(default = datetime.now, blank = True)
    KEYWORD = models.CharField(max_length = 150)
    Description = models.TextField()

    def __str__(self):
        return self.Title
    
class A4HOTPICKS(models.Model):
    Title = models.TextField()
    Text = models.TextField()
    Image = models.ImageField(upload_to= 'Hot Picks')
    Source = models.CharField(max_length = 50, blank = True)
    Source_link = models.URLField(blank = True, null = True)
    Time = models.DateTimeField(default = datetime.now, blank = True)
    KEYWORD = models.CharField(max_length = 150)
    Description = models.TextField()

    def __str__(self):
        return self.Title
    
class A5SUBSCRIBENEWS(models.Model):
    Title = models.CharField(max_length = 50)
    Subtitle = models.CharField(max_length = 60, null= True)
    Image = models.ImageField(upload_to = 'Subscribe News', null= True)
    Text = models.TextField()
    Button = models.CharField(max_length = 40)

    def __str__(self):
        return self.Title
    
class A6OTHERNEWS(models.Model):
    Title = models.TextField()
    Image = models.ImageField(upload_to= 'Other News')
    Text = models.TextField()
    Source = models.CharField(max_length = 50, blank = True)
    Source_link = models.URLField(blank = True, null = True)
    Describe = models.TextField()
    Time = models.DateTimeField(default = datetime.now, blank = True)
    KEYWORD = models.CharField(max_length = 150)
    Description = models.TextField()


    def __str__(self):
        return self.Title
    
class A7ECOANDWORLD(models.Model):
    Title = models.TextField()
    Text = models.TextField()
    Image = models.ImageField(upload_to= 'Latest News')
    Source = models.CharField(max_length = 40, null = True)
    Source_link = models.URLField(blank = True, null = True)
    Time = models.DateField(default = datetime.now, blank = True)
    KEYWORD = models.CharField(max_length = 150)
    Description = models.TextField()

    def __str__(self):
        return self.Title

class A8LIFESTYLE(models.Model):
    Title = models.TextField()
    Text = models.TextField()
    Image = models.ImageField(upload_to= 'Latest News')
    Source = models.CharField(max_length = 40, null = True)
    Source_link = models.URLField(blank = True, null = True)
    Time = models.DateField(default = datetime.now, blank = True)
    KEYWORD = models.CharField(max_length = 150)
    Description = models.TextField()

    def __str__(self):
        return self.Title
    
class A9BOTTOMNAV(models.Model):
    Title = models.CharField(max_length = 30, null = True)
    Link = models.URLField(default = None)

    def __str__(self):
        return self.Title
    
class B1OURORIGINAL(models.Model):
    Image = models.ImageField(upload_to= 'Original Gallery')

class B2STOREADS(models.Model):
    Title = models.CharField(max_length = 30)
    Image = models.ImageField(upload_to= 'Ads')
    Button = models.CharField(max_length = 20, null = True)
    Link = models.URLField()

    def __str__(self):
        return self.Title
    
class B3WEBSITE_TAGS(models.Model):
    Follow_us_top = models.CharField(max_length = 50)
    Hot_Picks = models.CharField(max_length = 50)
    Top_Picks = models.CharField(max_length = 50)
    Latest_news = models.CharField(max_length = 50)
    Other = models.CharField(max_length = 50)
    Ecoandworld = models.CharField(max_length = 50)
    LIFESTYLE = models.CharField(max_length = 50)
    Stay_connected = models.CharField(max_length = 50)
    Address_head = models.CharField(max_length = 50)
    Address_location_head = models.CharField(max_length = 50)
    Address_location = models.CharField(max_length = 50)
    Address_email_head = models.CharField(max_length = 50)
    Address_email = models.CharField(max_length = 50)
    Address_Phone_head = models.CharField(max_length = 50, blank = True, default = None)
    Address_Phone = models.CharField(max_length = 50, blank = True, default = None)
    Twitter_link = models.URLField()
    Youtube_link = models.URLField()
    Instagram_link = models.URLField()
    Recent_head = models.CharField(max_length = 50)
    Categories_head = models.CharField(max_length = 50)
    Ourgallery_head = models.CharField(max_length = 50)
    Site_name = models.CharField(max_length = 50)
    Site_after_name = models.CharField(max_length = 50)
    Disclaimer_head = models.CharField(max_length = 50)
    Disclaimer_link = models.CharField(max_length = 50)
    Email_bar_inside = models.CharField(max_length = 50)

class B4HORIZONTABANNER(models.Model):
    Image = models.ImageField(upload_to= 'Horizontal Ads')

class B5KEYWORDS_DES(models.Model):
    MAINPAGEKEYWORD = models.CharField(max_length = 150)
    MAINPAGEDESCRIPTION = models.TextField()

    HOTPAGEKEYWORD = models.CharField(max_length = 150)
    HOTPAGEDESCRIPTION = models.TextField()

    TOPPAGEKEYWORD = models.CharField(max_length = 150)
    TOPPAGEDESCRIPTION = models.TextField()

    LATESTPAGEKEYWORD = models.CharField(max_length = 150)
    LATESTPAGEDESCRIPTION = models.TextField()

    SPORTSPAGEKEYWORD = models.CharField(max_length = 150)
    SPORTSPAGEDESCRIPTION = models.TextField()

    ECONOMICSPAGEKEYWORD = models.CharField(max_length = 150)
    ECONOMICSPAGEDESCRIPTION = models.TextField()

    LIFESTYLEPAGEKEYWORD = models.CharField(max_length = 150)
    LIFESTYLEPAGEDESCRIPTION = models.TextField()