from django.conf.urls import patterns, include, url
from kindnesspledge import views
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^kindnesspledge/', include('kindnesspledge.foo.urls')),
    url(r'^$', views.home),
    url(r'^logout/$', views.logout_view),
    url(r'^login/$', views.login_view),
    url(r'^about/$', views.about),
    url(r'^contact/$', views.contact),
    url(r'^campaigns/$', views.campaigns),
    url(r'^reset/$', views.reset),
    url(r'^campaign/(\w+)/$', views.campaign),
    url(r'^campaign/(\w+)/post-video/$', views.post_video),
    url(r'^campaign/(\w+)/post-image/$', views.post_image),
    url(r'^campaign/(\w+)/post-text/$', views.post_text),
    url(r'^campaign/(\w+)/post-suggestion/$', views.post_suggestion),
    url(r'^campaign/(\w+)/post-link/$', views.post_link),
    url(r'^campaign/(\w+)/video-post/(\w+)/$', views.video_post),
    url(r'^campaign/(\w+)/image-post/(\w+)/$', views.image_post),
    url(r'^campaign/(\w+)/text-post/(\w+)/$', views.text_post),
    url(r'^profile/(\w+)/$', views.profile),
    url(r'^profile/(\w+)/stories/$', views.profile_stories),
    url(r'^profile/(\w+)/videos/$', views.profile_videos),
    url(r'^profile/(\w+)/images/$', views.profile_images),
    url(r'^profile/(\w+)/campaigns-created/$', views.profile_created),
    url(r'^profile/(\w+)/campaigns-pledged/$', views.profile_pledged),
    url(r'^recent-stories/$', views.recent_stories),
    url(r'^recent-videos/$', views.recent_videos),
    url(r'^recent-images/$', views.recent_images),
    url(r'^likes/$', views.likes),
    url(r'^create-campaign/$', views.create_campaign),
    url(r'^submit-comment/$', views.submit_comment),
    url(r'^campaign-post/$', views.campaign_post),
    url(r'^quotes/$', views.quotes),
    url(r'^add-quote/$', views.add_quote),
    url(r'^accounts/', include('registration.urls')),
    url(r'^social/', include('socialregistration.urls',
                             namespace = 'socialregistration')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
        # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Uncomment the next line to enable the admin:
    #(r'^tinymce/', include('tinymce.urls')),
)

urlpatterns += staticfiles_urlpatterns()
