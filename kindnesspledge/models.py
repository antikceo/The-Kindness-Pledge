from django.db import models
#from django import forms
#from tinymce.widgets import TinyMCE
from tinymce import models as tinymce_models
from django.contrib.auth.models import User
from django.forms import ModelForm

class Campaigns(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='Campaign-Photos')
    description = models.TextField()
    creator = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)
    #pledge_count = models.IntegerField()
    #num_signed = models.IntegerField() 


class Campaign_Pledges(models.Model):
    pledgee = models.ForeignKey(User)
    campaign = models.ForeignKey(Campaigns)

#video posts on a specific campaign's page                                                                                                                                          
class Campaign_Posts(models.Model):
    campaign = models.ForeignKey(Campaigns)
    creator = models.ForeignKey(User)
    title = models.CharField(max_length=30)
    link = models.URLField(blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    in_moderation = models.BooleanField() #automatically sets to true after a post has been reported as spam                                                                        
    spam_report = models.BooleanField() #sets to true after post is reported as spam                                                                                                
    #num_likes = models.IntegerField()

class Campaign_Posts_Images(models.Model):
    campaign = models.ForeignKey(Campaigns)
    creator = models.ForeignKey(User)
    title = models.CharField(max_length=30)
    content = models.ImageField(upload_to='Campaign-Post-Images')
    caption = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    in_moderation = models.BooleanField() #automatically sets to true after a post has been reported as spam       
    spam_report = models.BooleanField() #sets to true after post is reported as spam         
    #num_likes = models.IntegerField()

#video posts on a specific campaign's page
class Campaign_Posts_Videos(models.Model):
    campaign = models.ForeignKey(Campaigns)
    creator = models.ForeignKey(User)
    title = models.CharField(max_length=30)
    content = models.URLField()
    caption = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    in_moderation = models.BooleanField() #automatically sets to true after a post has been reported as spam 
    spam_report = models.BooleanField() #sets to true after post is reported as spam
    #num_likes = models.IntegerField()


class Post_Likes(models.Model):
    campaign_post = models.ForeignKey(Campaign_Posts)
    creator = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)

class Video_Likes(models.Model):
    campaign_post = models.ForeignKey(Campaign_Posts_Videos)
    creator = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)

class Image_Likes(models.Model):
    campaign_post = models.ForeignKey(Campaign_Posts_Images)
    creator = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)

#user suggestions for a specific campaign's page                                                                                                
class Campaign_Suggestions(models.Model):
    campaign = models.ForeignKey(Campaigns)
    creator = models.ForeignKey(User)
    suggestion = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    in_moderation = models.BooleanField() #automatically sets to true after a post has been reported as spam
    spam_report = models.BooleanField()  #sets to true after post is reported as spam 
    #num_likes = models.IntegerField()

class Campaign_Links(models.Model):
    campaign = models.ForeignKey(Campaigns)
    creator = models.ForeignKey(User)
    link = models.URLField()
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    in_moderation = models.BooleanField() #automatically sets to true after a post has been reported as spam                                                                        
    spam_report = models.BooleanField()  #sets to true after post is reported as spam        

#comments on a post
class Campaign_Post_Comments(models.Model):
    campaign_post = models.ForeignKey(Campaign_Posts)
    creator = models.ForeignKey(User)
    comment = models.TextField() 
    timestamp = models.DateTimeField(auto_now_add=True)
    in_moderation = models.BooleanField() #automatically sets to true after a post has been reported as spam 
    spam_report = models.BooleanField()   #sets to true after post is reported as spam 

#comments on a post                                                                                                                                   
class Campaign_Post_Image_Comments(models.Model):
    campaign_post = models.ForeignKey(Campaign_Posts_Images)
    creator = models.ForeignKey(User)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    in_moderation = models.BooleanField() #automatically sets to true after a post has been reported as spam                                                                       
    spam_report = models.BooleanField()   #sets to true after post is reported as spam  

#comments on a post                                                                                                                                                                
class Campaign_Post_Video_Comments(models.Model):
    campaign_post = models.ForeignKey(Campaign_Posts_Videos)
    creator = models.ForeignKey(User)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    in_moderation = models.BooleanField() #automatically sets to true after a post has been reported as spam                                                                        
    spam_report = models.BooleanField()   #sets to true after post is reported as spam  

#comments on a post                                                                                                                                                                 
class Campaign_Suggestion_Comments(models.Model):
    campaign_suggestion = models.ForeignKey(Campaign_Suggestions)
    creator = models.ForeignKey(User)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    in_moderation = models.BooleanField() #automatically sets to true after a post has been reported as spam                                                                        
    spam_report = models.BooleanField()  #sets to true after post is reported as spam 

#quotes added
class Quotes(models.Model):
    quote = models.TextField()
    creator = models.ForeignKey(User)
    optional_source = models.CharField(max_length=100, blank=True)
    #date_created = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True) 
    in_moderation = models.BooleanField() #defaults to false until it has been approved
    #num_likes = models.IntegerField()
    author = models.CharField(max_length=100)
