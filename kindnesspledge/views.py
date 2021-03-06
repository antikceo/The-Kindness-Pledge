from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.template import RequestContext
from tinymce.widgets import TinyMCE
from kindnesspledge import models
from kindnesspledge import forms
from django.utils import simplejson as json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


quote = models.Quotes.objects.get(in_moderation__exact=True)
recent_videos = models.Campaign_Posts_Videos.objects.order_by('-timestamp')[:5]
recent_images = models.Campaign_Posts_Images.objects.order_by('-timestamp')[:5]
recent_stories = models.Campaign_Posts.objects.order_by('-timestamp')[:5]


def profile_pledged(request, user):
    user_this =  auth.models.User.objects.get(username__exact=user)
    pledged = models.Campaign_Pledges.objects.filter(pledgee=user_this)
    paginator = Paginator(pledged, 15)
    count = paginator.num_pages
    them = []
    for num in range(0,count):
        them.append('bogus')
    page = request.GET.get('page')
    try:
        campaigns = paginator.page(page)
    except PageNotAnInteger:
        campaigns = paginator.page(1)
    except EmptyPage:
        campaigns = paginator.page(paginator.num_pages)
    if not request.user.is_authenticated():
        is_logged = False
        return render_to_response('frontend/campaigns-pledged.html', {'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories,'user':user,'is_logged': is_logged, 'campaigns': campaigns, 'them': them})
    else:
        is_logged = True
        username = request.user.username
        return render_to_response('frontend/campaigns-pledged.html', {'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories,'user':user,'is_logged': is_logged, 'username': username, 'campaigns': campaigns, 'them': them})


def profile_created(request, user):
    user_this =  auth.models.User.objects.get(username__exact=user)
    created = models.Campaigns.objects.filter(creator=user_this)
    paginator = Paginator(created, 15)
    count = paginator.num_pages
    them = []
    for num in range(0,count):
        them.append('bogus')
    page = request.GET.get('page')
    try:
        campaigns = paginator.page(page)
    except PageNotAnInteger:
        campaigns = paginator.page(1)
    except EmptyPage:
        campaigns = paginator.page(paginator.num_pages)
    if not request.user.is_authenticated():
        is_logged = False
        return render_to_response('frontend/campaigns-created.html', {'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories,'user':user,'is_logged': is_logged, 'campaigns': campaigns, 'them': them})
    else:
        is_logged = True
        username = request.user.username
        return render_to_response('frontend/campaigns-created.html', {'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories,'user':user,'is_logged': is_logged, 'username': username, 'campaigns': campaigns, 'them': them})


def profile_stories(request, user):
    user_this =  auth.models.User.objects.get(username__exact=user)
    user_stories_raw = models.Campaign_Posts.objects.filter(creator=user_this).order_by('-timestamp')
    paginator = Paginator(user_stories_raw, 12)
    count = paginator.num_pages
    them = []
    for num in range(0,count):
        them.append('bogus')
    page = request.GET.get('page')
    try:
        user_vids = paginator.page(page)
    except PageNotAnInteger:
        user_vids = paginator.page(1)
    except EmptyPage:
        user_vids = paginator.page(paginator.num_pages)

    if not request.user.is_authenticated():
        is_logged = False
        return render_to_response('frontend/profile-stories.html', {'them': them, 'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories, 'user_vids': user_vids, 'user':user, 'is_logged': is_logged}, context_instance = RequestContext(request))
    else:
        is_logged = True
        username = request.user.username
        return render_to_response('frontend/profile-stories.html', {'them': them, 'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'username': username, 'recent_stories': recent_stories, 'user_vids': user_vids, 'user':user, 'is_logged': is_logged}, context_instance = RequestContext(request))

def profile_videos(request, user):
    user_this =  auth.models.User.objects.get(username__exact=user)
    user_vids_raw = models.Campaign_Posts_Videos.objects.filter(creator=user_this).order_by('-timestamp')
    paginator = Paginator(user_vids_raw, 12) 
    count = paginator.num_pages
    them = []
    for num in range(0,count):
        them.append('bogus')
    page = request.GET.get('page')
    try:
        user_vids = paginator.page(page)
    except PageNotAnInteger:
        user_vids = paginator.page(1)
    except EmptyPage:
        user_vids = paginator.page(paginator.num_pages)
    if not request.user.is_authenticated():
        is_logged = False
        return render_to_response('frontend/profile-videos.html', {'them': them, 'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories, 'user_vids': user_vids, 'user':user, 'is_logged': is_logged}, context_instance = RequestContext(request))
    else:
        is_logged = True
        username = request.user.username
        return render_to_response('frontend/profile-videos.html', {'them': them, 'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories,'username':username, 'user_vids': user_vids, 'user':user, 'is_logged': is_logged}, context_instance = RequestContext(request))

def profile_images(request, user):
    user_this =  auth.models.User.objects.get(username__exact=user)
    user_images_raw = models.Campaign_Posts_Images.objects.filter(creator=user_this).order_by('-timestamp')
    paginator = Paginator(user_images_raw, 12)
    count = paginator.num_pages
    them = []
    for num in range(0,count):
        them.append('bogus')
    page = request.GET.get('page')
    try:
        user_images = paginator.page(page)
    except PageNotAnInteger:
        user_images = paginator.page(1)
    except EmptyPage:
        user_images = paginator.page(paginator.num_pages)
    if not request.user.is_authenticated():
        is_logged = False
        return render_to_response('frontend/profile-images.html', {'them': them, 'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories, 'user_vids': user_images, 'user':user, 'is_logged': is_logged}, context_instance = RequestContext(request))
    else:
        is_logged = True
        username = request.user.username
        return render_to_response('frontend/profile-images.html', {'them': them, 'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'username':username, 'recent_stories': recent_stories, 'user': user,'user_vids': user_images, 'is_logged': is_logged}, context_instance = RequestContext(request))

def recent_stories(request):
    user_stories_raw = models.Campaign_Posts.objects.order_by('-timestamp')
    paginator = Paginator(user_stories_raw, 12)
    count = paginator.num_pages
    them = []
    for num in range(0,count):
        them.append('bogus')
    page = request.GET.get('page')
    try:
        user_vids = paginator.page(page)
    except PageNotAnInteger:
        user_vids = paginator.page(1)
    except EmptyPage:
        user_vids = paginator.page(paginator.num_pages)
    if not request.user.is_authenticated():
        is_logged = False
        return render_to_response('frontend/recent-stories.html', {'them': them, 'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories, 'user_vids': user_vids, 'is_logged': is_logged}, context_instance = RequestContext(request))
    else:
        is_logged = True
        username = request.user.username
        return render_to_response('frontend/recent-stories.html', {'them': them, 'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'username': username,'recent_stories': recent_stories, 'user_vids': user_vids, 'is_logged': is_logged}, context_instance = RequestContext(request))

def recent_videos(request):
    user_vids_raw = models.Campaign_Posts_Videos.objects.order_by('-timestamp')
    paginator = Paginator(user_vids_raw, 12)
    count = paginator.num_pages
    them = []
    for num in range(0,count):
        them.append('bogus')
    page = request.GET.get('page')
    try:
        user_vids = paginator.page(page)
    except PageNotAnInteger:
        user_vids = paginator.page(1)
    except EmptyPage:
        user_vids = paginator.page(paginator.num_pages)
    if not request.user.is_authenticated():
        is_logged = False
        return render_to_response('frontend/recent-videos.html', {'them': them, 'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories, 'user_vids': user_vids, 'is_logged': is_logged}, context_instance = RequestContext(request))
    else:
        is_logged = True
        username = request.user.username
        return render_to_response('frontend/recent-videos.html', {'them': them, 'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'username': username,'recent_stories': recent_stories, 'user_vids': user_vids, 'is_logged': is_logged}, context_instance = RequestContext(request))

def recent_images(request):
    user_images_raw = models.Campaign_Posts_Images.objects.order_by('-timestamp')
    paginator = Paginator(user_images_raw, 12)
    count = paginator.num_pages
    them = []
    for num in range(0,count):
        them.append('bogus')
    page = request.GET.get('page')
    try:
        user_images = paginator.page(page)
    except PageNotAnInteger:
        user_images = paginator.page(1)
    except EmptyPage:
        user_images = paginator.page(paginator.num_pages)
    if not request.user.is_authenticated():
        is_logged = False
        return render_to_response('frontend/recent-images.html', {'them': them, 'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories, 'user_vids': user_images, 'is_logged': is_logged}, context_instance = RequestContext(request))
    else: 
        is_logged = True
        username = request.user.username
        return render_to_response('frontend/recent-images.html', {'them': them, 'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories, 'username': username, 'user_vids': user_images, 'is_logged': is_logged}, context_instance = RequestContext(request))

def post_link(request, this_id):
    errors = []
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login")
    else:
        is_logged = True
        username = request.user.username
        if request.method == 'POST':
            user_this =  auth.models.User.objects.get(username__exact=username)
            campaign = models.Campaigns.objects.get(id__exact=this_id)
            user = models.Campaign_Links(creator=user_this, campaign=campaign)
            form = forms.LinkForm(request.POST, instance=user)
            if form.is_valid():
                cmodel = form.save()
                cmodel.save()
                url  = '/campaign/' + this_id
                return HttpResponseRedirect(url)
            else:
                errors.append('Please fill out all fields in the form!')
        else:
            form = forms.LinkForm()
        return render_to_response('frontend/post-link.html', {'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories, 'is_logged': is_logged, 'username': username, 'form': form, 'errors': errors}, context_instance = RequestContext(request))

def video_post(request, campaign_id, video_id):
    campaign_post = models.Campaign_Posts_Videos.objects.get(id__exact=video_id)
    if not request.user.is_authenticated():
        is_logged = False
        return render_to_response('frontend/video-post.html', {'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories,'campaign_id': campaign_id, 'is_logged': is_logged, 'campaign_post': campaign_post}, context_instance = RequestContext(request))
    else:
        is_logged = True
        username = request.user.username
        return render_to_response('frontend/video-post.html', {'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories,'campaign_id': campaign_id, 'is_logged': is_logged , 'campaign_post': campaign_post, 'username': username}, context_instance = RequestContext(request))

def image_post(request, campaign_id, image_id):
    campaign_post = models.Campaign_Posts_Images.objects.get(id__exact=image_id)
    if not request.user.is_authenticated():
        is_logged = False
        return render_to_response('frontend/image-post.html', {'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories,'campaign_id': campaign_id, 'is_logged': is_logged, 'campaign_post': campaign_post}, context_instance = RequestContext(request))
    else:
        is_logged = True
        username = request.user.username
        return render_to_response('frontend/image-post.html', {'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories,'campaign_id': campaign_id, 'is_logged': is_logged , 'campaign_post': campaign_post, 'username': username}, context_instance = RequestContext(request))

def text_post(request, campaign_id, post_id):
    campaign_post = models.Campaign_Posts.objects.get(id__exact=post_id)
    if not request.user.is_authenticated():
        is_logged = False
        return render_to_response('frontend/text-post.html', {'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories,'campaign_id': campaign_id, 'is_logged': is_logged, 'campaign_post': campaign_post}, context_instance = RequestContext(request))
    else:
        is_logged = True
        username = request.user.username
        return render_to_response('frontend/text-post.html', {'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories,'campaign_id': campaign_id, 'is_logged': is_logged , 'campaign_post': campaign_post, 'username': username}, context_instance = RequestContext(request))

def likes(request):
    if not request.user.is_authenticated():
        return HttpResponse("you must be logged in to do this!")
    else:
        is_logged = True
        username = request.user.username
        if request.method == 'POST' and 'post_id' in request.POST:
            post_id = request.POST.get('post_id')
            user_this =  auth.models.User.objects.get(username__exact=username)
            campaign_post = models.Campaign_Posts.objects.get(id__exact=post_id)
        elif request.method == 'POST' and 'video_id' in request.POST:
            video_id = request.POST.get('video_id')
            user_this =  auth.models.User.objects.get(username__exact=username)
            campaign_post = models.Campaign_Posts_Videos.objects.get(id__exact=video_id)
            user = models.Video_Likes(creator=user_this, campaign_post=campaign_post)
            form = forms.VideoLikesForm(request.POST, instance=user)
            if form.is_valid():
                cmodel = form.save()
                cmodel.save()
                return HttpResponse("Like recorded!")
        elif request.method == 'POST' and 'image_id' in request.POST:
            image_id = request.POST.get('image_id')
            user_this =  auth.models.User.objects.get(username__exact=username)
            campaign_post = models.Campaign_Posts_Images.objects.get(id__exact=image_id)
        else:
            return HttpResponse("something went wrong")
        

def post_video(request, this_id):
    errors = []
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login")
    else:
        is_logged = True
        username = request.user.username
        if request.method == 'POST':
            user_this =  auth.models.User.objects.get(username__exact=username)
            campaign = models.Campaigns.objects.get(id__exact=this_id)
            user = models.Campaign_Posts_Videos(creator=user_this, campaign=campaign)
            form = forms.VideoForm(request.POST, instance=user)
            if form.is_valid():
                cmodel = form.save()
                cmodel.save()
                url  = '/campaign/' + this_id
                return HttpResponseRedirect(url)
            else:
                errors.append('Please fill out all fields in the form!')
        else:
            form = forms.VideoForm()
        return render_to_response('frontend/post-video.html', {'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories,'is_logged': is_logged, 'username': username, 'form': form, 'errors': errors}, context_instance = RequestContext(request))


def post_image(request, this_id):
    errors = []
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login")
    else:
        is_logged = True
        username = request.user.username
        if request.method == 'POST':
            user_this =  auth.models.User.objects.get(username__exact=username)
            campaign = models.Campaigns.objects.get(id__exact=this_id)
            user = models.Campaign_Posts_Images(creator=user_this, campaign=campaign)
            form = forms.ImageForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                cmodel = form.save()
                cmodel.save()
                url  = '/campaign/' + this_id
                return HttpResponseRedirect(url)
            else:
                errors.append('Please fill out all fields in the form!')
        else:
            form = forms.ImageForm()
        return render_to_response('frontend/post-image.html', {'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories,'is_logged': is_logged, 'username': username, 'form': form, 'errors': errors}, context_instance = RequestContext(request))
    
def post_text(request, this_id):
    errors = []
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login")
    else:
        is_logged = True
        username = request.user.username
        if request.method == 'POST':
            user_this =  auth.models.User.objects.get(username__exact=username)
            campaign = models.Campaigns.objects.get(id__exact=this_id)
            user = models.Campaign_Posts(creator=user_this, campaign=campaign)
            form = forms.TextForm(request.POST, instance=user)
            if form.is_valid():
                cmodel = form.save()
                cmodel.save()
                url  = '/campaign/' + this_id
                return HttpResponseRedirect(url)
            else:
                errors.append('Please fill out all fields in the form!')
        else:
            form = forms.TextForm()
        return render_to_response('frontend/post-text.html', {'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories,'is_logged': is_logged, 'username': username, 'form': form, 'errors': errors}, context_instance = RequestContext(request))

def post_suggestion(request, this_id):
    errors = []
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login")
    else:
        is_logged = True
        username = request.user.username
        if request.method == 'POST':
            user_this =  auth.models.User.objects.get(username__exact=username)
            campaign = models.Campaigns.objects.get(id__exact=this_id)
            user = models.Campaign_Suggestions(creator=user_this, campaign=campaign)
            form = forms.SuggestionForm(request.POST, instance=user)
            if form.is_valid():
                cmodel = form.save()
                cmodel.save()
                url  = '/campaign/' + this_id
                return HttpResponseRedirect(url)
            else:
                errors.append('Please fill out all fields in the form!')
        else:
            form = forms.SuggestionForm()
        return render_to_response('frontend/post-suggest.html', {'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories,'is_logged': is_logged, 'username': username, 'form': form, 'errors': errors}, context_instance = RequestContext(request))

def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
            # Redirect to a success page.
        return HttpResponseRedirect("/")
        #return HttpResponseRedirect(username) 
    else:
        # Show an error page
        return HttpResponseRedirect("/accounts/login")

def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def home(request):
    campaigns = models.Campaigns.objects.all().order_by('-timestamp')[:8] 
    if not request.user.is_authenticated():
        is_logged = False
        #username = request.user.username
        return render_to_response('frontend/home.html', {'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories, 'campaigns': campaigns, 'is_logged': is_logged})
    else:
        is_logged = True
        username = request.user.username
        #in future change this to redirect to profile
        url = '/profile/' + username
        return HttpResponseRedirect(url)
        #return render_to_response('frontend/home.html', {'campaigns': campaigns, 'is_logged': is_logged, 'username': username})

def profile(request,username):
    user = auth.models.User.objects.get(username__exact=username)
    #is_logged = True
    pledged =  models.Campaign_Pledges.objects.filter(pledgee=user)[:5]
    images =  models.Campaign_Posts_Images.objects.filter(creator=user).order_by('-timestamp')[:5]
    videos =  models.Campaign_Posts_Videos.objects.filter(creator=user).order_by('-timestamp')[:5]
    stories  =  models.Campaign_Posts.objects.filter(creator=user).order_by('-timestamp')[:5]
    campaigns = models.Campaigns.objects.filter(creator=user).order_by('-timestamp')[:5]
    
    if not request.user.is_authenticated():
        is_logged = False
        return render_to_response('frontend/profile.html', {'pledged':pledged,'videos':videos,'images':images,'stories':stories,'campaigns':campaigns,'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories, 'user':user, 'is_logged': is_logged})
    else:
        is_logged = True
        user_this = request.user.username
        if user_this == username:
            is_owner = True
            
            return render_to_response('frontend/profile.html', {'pledged':pledged,'videos':videos,'images':images,'stories':stories,'campaigns':campaigns,'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories, 'is_logged': is_logged,'username':username,'user':user, 'is_owner':is_owner})
        else:
            is_owner = False
            username = user_this
            return render_to_response('frontend/profile.html', {'pledged':pledged,'videos':videos,'images':images,'stories':stories,'campaigns':campaigns,'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories, 'is_logged': is_logged,'username':username,'user':user, 'is_owner':is_owner})

def about(request):
    if not request.user.is_authenticated():
        is_logged = False
        return render_to_response('frontend/about.html', {'is_logged': is_logged})
    else:
        is_logged = True
        username = request.user.username
        return render_to_response('frontend/about.html', {'is_logged': is_logged, 'username': username})

def contact(request):
    errors = []
    messages = []
    if not request.user.is_authenticated():
        is_logged = False
        if request.method == 'GET':
            if not request.GET.get('name') or not request.GET.get('email') or not request.GET.get('message'):
                errors.append('Please fill out all the fields!')
            else:
                name = request.GET.get('name')
                email = request.GET.get('email')
                message = request.GET.get('message') + ' ' + email
                message_full = 'Message from ' + name
                if (send_mail(message_full, message, email,['admin@thekindnesspledge.org'], fail_silently=False)):
                    messages.append('Your message was sent successfully, you will recieve a response as soon as possible.')
                else:
                    errors.append('Oops something went wrong, please check to ensure that you filled out the email field correctly')
        return render_to_response('frontend/contact.html', {'is_logged': is_logged, 'errors':errors, 'messages':messages}, context_instance = RequestContext(request))
    else:
        is_logged = True
        username = request.user.username
        return render_to_response('frontend/contact.html', {'is_logged': is_logged, 'username': username, 'errors':errors, 'messages':messages}, context_instance = RequestContext(request))

def campaigns(request):
    campaigns_all = models.Campaigns.objects.all().order_by('-timestamp')
    paginator = Paginator(campaigns_all, 18) 
    count = paginator.num_pages
    them = []
    for num in range(0,count):
        them.append('bogus')
    page = request.GET.get('page')
    try:
        campaigns = paginator.page(page)
    except PageNotAnInteger:
        campaigns = paginator.page(1)
    except EmptyPage:
        campaigns = paginator.page(paginator.num_pages)

    if not request.user.is_authenticated():
        is_logged = False
        return render_to_response('frontend/campaigns.html', {'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories,'is_logged': is_logged, 'campaigns': campaigns, 'them': them})
    else:
        is_logged = True
        username = request.user.username
        return render_to_response('frontend/campaigns.html', {'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories,'is_logged': is_logged, 'username': username, 'campaigns': campaigns, 'them': them})

def reset(request):
    if not request.user.is_authenticated():
        is_logged = False
        return render_to_response('frontend/reset.html', {'is_logged': is_logged})
    else:
        is_logged = True
        username = request.user.username
        return render_to_response('frontend/reset.html', {'is_logged': is_logged, 'username': username})


def submit_comment(request):
    if request.is_ajax():
        message = "This is ajax"
    else:
        message = "Not ajax"
    return HttpResponse(message)    

def campaign(request, this_id):

    campaign = models.Campaigns.objects.get(id__exact=this_id)
    images_raw = models.Campaign_Posts_Images.objects.filter(campaign=campaign).order_by('-timestamp')
    paginator2 = Paginator(images_raw, 50) # Show 25 per page       
    count2 = paginator2.num_pages
    them2 = []
    for num in range(0,count2):
        them2.append('bogus')
    if 'image' in request.GET:
        page2 = request.GET.get('page')
    else:
        page2 = []
    try:
        images = paginator2.page(page2)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.                    
        images = paginator2.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.                                                                                                        
        images = paginator2.page(paginator2.num_pages)

    videos_raw = models.Campaign_Posts_Videos.objects.filter(campaign=campaign).order_by('-timestamp')
    paginator1 = Paginator(videos_raw, 50) # Show 25 per page
    count1 = paginator1.num_pages
    them1 = []
    for num in range(0,count1):
        them1.append('bogus')
    if 'video' in request.GET:
        page1 = request.GET.get('page')
    else:
        page1 = []
    try:
        videos = paginator1.page(page1)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        videos = paginator1.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.                                                                                                        
        videos = paginator1.page(paginator1.num_pages)

    stories_raw = models.Campaign_Posts.objects.filter(campaign=campaign).order_by('-timestamp')
    paginator3 = Paginator(stories_raw, 50) # Show 25 per page
    count3 = paginator3.num_pages
    them3 = []
    for num in range(0,count3):
        them3.append('bogus')
    if 'story' in request.GET:
        page3 = request.GET.get('page')
    else:
        page3 = []
    try:
        stories = paginator3.page(page3)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.                                                                                              
        stories = paginator3.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.                                
        stories = paginator3.page(paginator3.num_pages)

    suggestions_raw = models.Campaign_Suggestions.objects.filter(campaign=campaign).order_by('-timestamp')
    paginator4 = Paginator(suggestions_raw, 50) # Show 50 per page                                                                           
    count4 = paginator4.num_pages
    them4 = []
    for num in range(0,count4):
        them4.append('bogus')
    if 'suggestion' in request.GET:
        page4 = request.GET.get('page')
    else:
        page4 = []
    try:
        suggestions = paginator4.page(page4)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.                                                                   
        suggestions = paginator4.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.                                                    
        suggestions = paginator4.page(paginator4.num_pages)

    links = models.Campaign_Links.objects.filter(campaign=campaign)
    comments_vids = models.Campaign_Post_Video_Comments.objects.all()
    comments_photos = models.Campaign_Post_Image_Comments.objects.all()
    comments_stories = models.Campaign_Post_Comments.objects.all()
    errors = []
    pledge_count = models.Campaign_Pledges.objects.filter(campaign=campaign).count()
    
    if not request.user.is_authenticated():
        is_logged = False
        form = forms.PledgeForm()
        if request.method == 'POST':
            if 'pledge_form' in request.POST:
                errors.append('You must be logged in to pledge a campaign!')
        return render_to_response('frontend/campaign.html', {'pledge_count':pledge_count, 'form':form, 'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories,'them1': them1,'them2': them2, 'them3': them3,'them4': them4,'is_logged': is_logged, 'links': links, 'campaign': campaign, 'images': images, 'videos': videos, 'stories': stories, 'comments_vids': comments_vids, 'errors':errors}, context_instance = RequestContext(request))
    else:
        is_logged = True
        username = request.user.username
        form = forms.VideoCommentsForm()
        is_pledged = models.Campaign_Pledges.objects.filter(pledgee=request.user).filter(campaign=campaign)
        #is_pledged = False
        if request.method == 'POST':
            #checks submit button to ascertain what kind of post
            if 'pledge_form' in request.POST:
                user_this =  auth.models.User.objects.get(username__exact=username)
                user = models.Campaign_Pledges(pledgee=user_this, campaign=campaign)
                form = forms.PledgeForm(request.POST, instance=user)
                if form.is_valid():
                    cmodel = form.save()
                    cmodel.save()
                    errors.append('You just pledged this campaign!')
            if 'video_post' in request.POST:
                user_this =  auth.models.User.objects.get(username__exact=username)
                post_id = request.POST.get('campaign_post')
                this_post = models.Campaign_Posts_Videos.objects.get(id__exact=post_id)
                user = models.Campaign_Post_Video_Comments(creator=user_this, campaign_post=this_post)
                form = forms.VideoCommentsForm(request.POST, instance=user)
                if form.is_valid():
                    errors.append('Valid input!')
                    cmodel = form.save()
                    cmodel.save()
                    if request.is_ajax():
                        return HttpResponse("Reaction posted successfully! It will show up in the comment box above on your next page refresh.")
                else:
                    if request.is_ajax():
                        return HttpResponse("Invalid Input")
                    errors.append('Invalid input!')
            else:
                form = forms.VideoCommentsForm()
            if 'image_post' in request.POST:
                user_this =  auth.models.User.objects.get(username__exact=username)
                post_id = request.POST.get('campaign_post')
                this_post = models.Campaign_Posts_Images.objects.get(id__exact=post_id)
                user = models.Campaign_Post_Image_Comments(creator=user_this, campaign_post=this_post)
                form = forms.PhotoCommentsForm(request.POST, instance=user)
                if form.is_valid():
                    errors.append('Valid Image comment input!')
                    cmodel = form.save()
                    cmodel.save()
                    if request.is_ajax():
                        return HttpResponse("Reaction posted successfully! It will show up in the comment box above on your next page refresh.")
                else:
                    if request.is_ajax():
                        return HttpResponse("Invalid Input")
                    errors.append('Invalid input!')
            else:
                form = forms.PhotoCommentsForm()
            if 'story_post' in request.POST:
                user_this =  auth.models.User.objects.get(username__exact=username)
                post_id = request.POST.get('campaign_post')
                this_post = models.Campaign_Posts.objects.get(id__exact=post_id)
                user = models.Campaign_Post_Comments(creator=user_this, campaign_post=this_post)
                form = forms.StoryCommentsForm(request.POST, instance=user)
                if form.is_valid():
                    errors.append('Valid input!')
                    cmodel = form.save()
                    cmodel.save()
                    if request.is_ajax():
                        return HttpResponse("Reaction posted successfully! It will show up in the comment box above on your next page refresh.")
                else:
                    if request.is_ajax():
                        return HttpResponse("Invalid Input")
                    errors.append('Invalid input!')
            else:
                form = forms.VideoCommentsForm()
        else:
            form = forms.PledgeForm()
        return render_to_response('frontend/campaign.html', {'pledge_count':pledge_count, 'is_pledged':is_pledged, 'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories,'is_logged': is_logged, 'username': username, 'links': links,'campaign': campaign, 'images': images, 'videos': videos, 'stories': stories, 'suggestions': suggestions, 'comments_vids': comments_vids, 'comments_photos': comments_photos, 'comments_stories': comments_stories, 'errors': errors, 'form': form}, context_instance = RequestContext(request))

def create_campaign(request):
    errors = []
    if not request.user.is_authenticated():
        is_logged = False
        errors.append('You need to log in to perform this action. This is essential to maintaining the quality of posts on this site.')
        return HttpResponseRedirect("/accounts/login")
    else:
        is_logged = True
        username = request.user.username
        if request.method == 'POST':
            user_this =  auth.models.User.objects.get(username__exact=username) 
            userid = auth.models.User.objects.get(username__exact=username).id
            user = models.Campaigns(creator=user_this)
            form = forms.CampaignsForm(request.POST, request.FILES, instance=user)            
            if form.is_valid():
                cmodel = form.save()
                cmodel.save()
                return HttpResponseRedirect('/')
                #url = '/profile/' + username
            else:
                errors.append('Please fill out all fields in the form!')
        else:
            form = forms.CampaignsForm()
        return render_to_response('frontend/create-campaign.html', {'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories,'is_logged': is_logged, 'username': username, 'form': form, 'errors': errors}, context_instance = RequestContext(request))

def success(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('name', ''):
            errors.append('\'Campaign Name\' field is compulsory.')
        if not request.POST.get('image', ''):
            errors.append('\'Campaign Image\' field is compulsory.')
        if not request.POST.get('description', ''):
            errors.append('\'Campaign Description\' field is compulsory.')
        if not errors:
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                handle_uploaded_file(request.FILES['file'])
    return render_to_response('create-campaign.html', {'errors': errors})

def handle_uploaded_file(f):
    storename = f.name
    with open('Campaign-Photos/', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def campaign_post(request):
    if not request.user.is_authenticated():
        is_logged = False
        return render_to_response('frontend/campaign-post.html', {'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories,'is_logged': is_logged})
    else:
        is_logged = True
        username = request.user.username
        return render_to_response('frontend/campaign-post.html', {'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories,'is_logged': is_logged, 'username': username})

def post_success():
    if 'name' in request.POST and 'image' in request.POST and 'description' in request.POST:        
        message =  "Successfully created your campaign, we will send you a message when your campaign is approved"
        is_logged = True
        return render_to_response('frontend/campaign-post.html', {'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories,'is_logged': is_logged, 'username': username})
    
def quotes(request):
    quotes = models.Quotes.objects.order_by('-timestamp')
    if not request.user.is_authenticated():
        is_logged = False
        return render_to_response('frontend/quotes.html', {'is_logged': is_logged, 'quotes': quotes})
    else:
        is_logged = True
        username = request.user.username
        return render_to_response('frontend/quotes.html', {'is_logged': is_logged, 'quotes': quotes, 'username': username})

def add_quote(request):
    errors = []
    if not request.user.is_authenticated():
        is_logged = False
        return HttpResponseRedirect('/accounts/login')
    else:
        is_logged = True
        username = request.user.username
        if request.method == 'POST':
            user_this =  auth.models.User.objects.get(username__exact=username)
            user = models.Quotes(creator=user_this)
            form = forms.QuotesForm(request.POST, instance=user)
            if form.is_valid():
                errors.append('Valid Image comment input!')
                cmodel = form.save()
                cmodel.save()
                return HttpResponseRedirect('/quotes')
            else:
                errors.append('Invalid input!')
        else:
            form = forms.QuotesForm()
        return render_to_response('frontend/add-quote.html', {'form': form,'quote': quote, 'recent_videos':recent_videos, 'recent_images':recent_images, 'recent_stories': recent_stories,'is_logged': is_logged, 'username': username}, context_instance = RequestContext(request))
