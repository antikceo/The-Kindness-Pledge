from django.contrib import admin
from kindnesspledge import models

class PostsAdmin(admin.ModelAdmin):
    list_display = ('caption', 'creator', 'in_moderation', 'timestamp')
    #search_fields = ('creator',)
    list_filter = ('in_moderation',)

class Pledgees(admin.ModelAdmin):
    list_display = ('pledgee', 'campaign')

class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'timestamp', 'creator')
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)

class Quotes(admin.ModelAdmin):
    list_display = ('quote', 'creator', 'author', 'timestamp')
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)

admin.site.register(models.Campaigns, CampaignAdmin)
admin.site.register(models.Campaign_Pledges, Pledgees)
admin.site.register(models.Campaign_Posts)
admin.site.register(models.Campaign_Posts_Videos, PostsAdmin)
admin.site.register(models.Campaign_Posts_Images, PostsAdmin)
admin.site.register(models.Campaign_Suggestions)
admin.site.register(models.Campaign_Post_Comments)
admin.site.register(models.Campaign_Post_Video_Comments)
admin.site.register(models.Campaign_Post_Image_Comments)
admin.site.register(models.Campaign_Suggestion_Comments)
admin.site.register(models.Quotes, Quotes)
