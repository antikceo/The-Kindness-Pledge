from django import forms
from django.forms import ModelForm
from kindnesspledge import models
from django.contrib.auth.models import User


class PledgeForm(ModelForm):
   class Meta:
      model = models.Campaign_Pledges
      exclude = ('pledgee', 'campaign')

class QuotesForm(ModelForm):
   class Meta:
      model = models.Quotes
      exclude = ('creator', )

class VideoLikesForm(ModelForm):
   class Meta:
      model = models.Video_Likes
      exclude = ('creator', 'campaign_post')

class ImageLikesForm(ModelForm):
   class Meta:
      model = models.Video_Likes
      exclude = ('creator', 'campaign_post')

class PostLikesForm(ModelForm):
   class Meta:
      model = models.Video_Likes
      exclude = ('creator', 'campaign_post')

class CampaignsForm(ModelForm):
   class Meta:
      model = models.Campaigns
      exclude = ('creator',)

class VideoCommentsForm(ModelForm):
   class Meta:
      model = models.Campaign_Post_Video_Comments
      exclude = ('creator', 'campaign_post')


class PhotoCommentsForm(ModelForm):
   class Meta:
      model = models.Campaign_Post_Image_Comments
      exclude = ('creator', 'campaign_post')

class StoryCommentsForm(ModelForm):
   class Meta:
      model = models.Campaign_Post_Comments
      exclude = ('creator', 'campaign_post')


class VideoForm(ModelForm):
   class Meta:
      model = models.Campaign_Posts_Videos
      exclude = ('creator', 'campaign')


class ImageForm(ModelForm):
   class Meta:
      model = models.Campaign_Posts_Images
      exclude = ('creator', 'campaign')

class TextForm(ModelForm):
   class Meta:
      model = models.Campaign_Posts
      exclude = ('creator', 'campaign')


class SuggestionForm(ModelForm):
   class Meta:
      model = models.Campaign_Suggestions
      exclude = ('creator', 'campaign')

class LinkForm(ModelForm):
   class Meta:
      model = models.Campaign_Links
      exclude = ('creator', 'campaign')
