from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib import messages
import json
import urllib.request

# Create your views here.


def index(request):
    PAGETOP = A0PAGETOP.objects.last()
    NAVBAR = A1NAVBAR.objects.first()
    NAV_LINKS = A1NAVBAR.objects.all()
    TOP_PICKS = A2TOPPICKS.objects.all()
    NEWSTODAY = A3NEWSTODAY.objects.last()
    ALLNEWSTODAY = A3NEWSTODAY.objects.all()
    HOTPICKS = A4HOTPICKS.objects.last()
    ALLHOTPICKS = A4HOTPICKS.objects.all()
    SUBSCRIBENEWS = A5SUBSCRIBENEWS.objects.last()
    OTHERNEWS = A6OTHERNEWS.objects.last()
    ALLOTHERNEWS = A6OTHERNEWS.objects.all()
    ECOANDWORLD = A7ECOANDWORLD.objects.all()
    LIFESTYLE = A8LIFESTYLE.objects.all()
    BOTTOMNAV = A9BOTTOMNAV.objects.all()
    OURORIGINAL = B1OURORIGINAL.objects.all()
    STOREADS = B2STOREADS.objects.all()
    WEBSITE_TAGS = B3WEBSITE_TAGS.objects.last()
    KEYWORDS_DES = B5KEYWORDS_DES.objects.last()

    return render(request, 'index.html', {
        'PAGETOP': PAGETOP,
        'NAVBAR': NAVBAR,
        'NAV_LINKS': NAV_LINKS,
        'TOP_PICKS': TOP_PICKS,
        'NEWSTODAY': NEWSTODAY,
        'HOTPICKS': HOTPICKS,
        'ALLHOTPICKS': ALLHOTPICKS,
        'SUBSCRIBENEWS': SUBSCRIBENEWS,
        'ALLNEWSTODAY': ALLNEWSTODAY,
        'OTHERNEWS': OTHERNEWS,
        'ALLOTHERNEWS': ALLOTHERNEWS,
        'ECOANDWORLD': ECOANDWORLD,
        'LIFESTYLE': LIFESTYLE,
        'BOTTOMNAV': BOTTOMNAV,
        'OURORIGINAL': OURORIGINAL,
        'STOREADS': STOREADS,
        'WEBSITE_TAGS': WEBSITE_TAGS,
        'KEYWORDS_DES': KEYWORDS_DES,
    })

def signin(request):
    PAGETOP = A0PAGETOP.objects.last()
    NAVBAR = A1NAVBAR.objects.first()
    NAV_LINKS = A1NAVBAR.objects.all()


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username:
            messages.error(request, 'Username cannot be empty')
            return redirect('signin') 
    
        if not password:
            messages.error(request, 'Password cannot be empty')
            return redirect('signin')

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return  redirect('/')
        
        else:
            messages.info(request, 'User not found')
            return redirect('signin')
        
    else:
        return render(request, 'signin.html',{
            'PAGETOP': PAGETOP,
            'NAVBAR': NAVBAR,
            'NAV_LINKS': NAV_LINKS,
        })

def signup(request):
    PAGETOP = A0PAGETOP.objects.last()
    NAVBAR = A1NAVBAR.objects.first()
    NAV_LINKS = A1NAVBAR.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')

        if not username:
            messages.error(request, 'Username cannot be empty')
            return redirect('signup') 

        if not email:
            messages.error(request, 'Email cannot be empty')
            return redirect('signup') 
              
        if not password:
            messages.error(request, 'Password cannot be empty')
            return redirect('signup')
        
        if not repassword:
            messages.error(request, 'Re-enter password')
            return redirect('signup')  
    

        if password == repassword:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('signup')
            
            elif User.objects.filter(username = username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('signup')
            
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('signin')
        
        else:
            messages.info(request, 'Password Not Matched')
            return redirect('signup')
        
    else:
        return render(request, 'signup.html',{
            'PAGETOP': PAGETOP,
            'NAVBAR': NAVBAR,
            'NAV_LINKS': NAV_LINKS,
        })
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def user_profile(request, username):
    user = get_object_or_404(User, username = username)

    PAGETOP = A0PAGETOP.objects.last()
    NAVBAR = A1NAVBAR.objects.first()
    NAV_LINKS = A1NAVBAR.objects.all()

    return render(request, 'user.html', {
        'user': user,
        'PAGETOP': PAGETOP,
        'NAVBAR': NAVBAR,
        'NAV_LINKS': NAV_LINKS,
    })

def change_user_info(request, username):  #change ============================================================
    user = get_object_or_404(User, username = username)

    PAGETOP = A0PAGETOP.objects.last()
    NAVBAR = A1NAVBAR.objects.first()
    NAV_LINKS = A1NAVBAR.objects.all()

    return render(request, 'change_user_info.html', {
        'user': user,
        'PAGETOP': PAGETOP,
        'NAVBAR': NAVBAR,
        'NAV_LINKS': NAV_LINKS,
    })

def hot_picks(request):
    PAGETOP = A0PAGETOP.objects.last()
    NAVBAR = A1NAVBAR.objects.first()
    NAV_LINKS = A1NAVBAR.objects.all()
    ALLNEWSTODAY = A3NEWSTODAY.objects.all()
    HOTPICKS = A4HOTPICKS.objects.all()
    ALLHOTPICKS = A4HOTPICKS.objects.all()
    SUBSCRIBENEWS = A5SUBSCRIBENEWS.objects.last()
    OTHERNEWS = A6OTHERNEWS.objects.last()
    ALLOTHERNEWS = A6OTHERNEWS.objects.all()
    ECOANDWORLD = A7ECOANDWORLD.objects.all()
    LIFESTYLE = A8LIFESTYLE.objects.all()
    BOTTOMNAV = A9BOTTOMNAV.objects.all()
    OURORIGINAL = B1OURORIGINAL.objects.all()
    STOREADS = B2STOREADS.objects.all()
    WEBSITE_TAGS = B3WEBSITE_TAGS.objects.last()
    HORIZONTABANNER = B4HORIZONTABANNER.objects.all()
    KEYWORDS_DES = B5KEYWORDS_DES.objects.last()

    return render(request, 'hot-picks.html',{
        'PAGETOP': PAGETOP,
        'NAVBAR': NAVBAR,
        'NAV_LINKS': NAV_LINKS,
        'HOTPICKS': HOTPICKS,
        'ALLHOTPICKS': ALLHOTPICKS,
        'SUBSCRIBENEWS': SUBSCRIBENEWS,
        'ALLNEWSTODAY': ALLNEWSTODAY,
        'OTHERNEWS': OTHERNEWS,
        'ALLOTHERNEWS': ALLOTHERNEWS,
        'ECOANDWORLD': ECOANDWORLD,
        'LIFESTYLE': LIFESTYLE,
        'BOTTOMNAV': BOTTOMNAV,
        'OURORIGINAL': OURORIGINAL,
        'STOREADS': STOREADS,
        'WEBSITE_TAGS': WEBSITE_TAGS,
        'HORIZONTABANNER': HORIZONTABANNER,
        'KEYWORDS_DES': KEYWORDS_DES,
    })

def top_picks(request):
    PAGETOP = A0PAGETOP.objects.last()
    NAVBAR = A1NAVBAR.objects.first()
    NAV_LINKS = A1NAVBAR.objects.all()
    TOP_PICKS = A2TOPPICKS.objects.all()
    ALLNEWSTODAY = A3NEWSTODAY.objects.all()
    ALLHOTPICKS = A4HOTPICKS.objects.all()
    HOTPICKS = A4HOTPICKS.objects.last()
    SUBSCRIBENEWS = A5SUBSCRIBENEWS.objects.last()
    OTHERNEWS = A6OTHERNEWS.objects.last()
    ALLOTHERNEWS = A6OTHERNEWS.objects.all()
    ECOANDWORLD = A7ECOANDWORLD.objects.all()
    LIFESTYLE = A8LIFESTYLE.objects.all()
    BOTTOMNAV = A9BOTTOMNAV.objects.all()
    OURORIGINAL = B1OURORIGINAL.objects.all()
    STOREADS = B2STOREADS.objects.all()
    WEBSITE_TAGS = B3WEBSITE_TAGS.objects.last()
    HORIZONTABANNER = B4HORIZONTABANNER.objects.all()
    KEYWORDS_DES = B5KEYWORDS_DES.objects.last()

    return render(request, 'top-picks.html',{
        'PAGETOP': PAGETOP,
        'NAVBAR': NAVBAR,
        'NAV_LINKS': NAV_LINKS,
        'TOP_PICKS': TOP_PICKS,
        'ALLHOTPICKS': ALLHOTPICKS,
        'HOTPICKS': HOTPICKS,
        'SUBSCRIBENEWS': SUBSCRIBENEWS,
        'ALLNEWSTODAY': ALLNEWSTODAY,
        'OTHERNEWS': OTHERNEWS,
        'ALLOTHERNEWS': ALLOTHERNEWS,
        'ECOANDWORLD': ECOANDWORLD,
        'LIFESTYLE': LIFESTYLE,
        'BOTTOMNAV': BOTTOMNAV,
        'OURORIGINAL': OURORIGINAL,
        'STOREADS': STOREADS,
        'WEBSITE_TAGS': WEBSITE_TAGS,
        'HORIZONTABANNER': HORIZONTABANNER,
        'KEYWORDS_DES': KEYWORDS_DES,
    })

def latest_news(request):
    PAGETOP = A0PAGETOP.objects.last()
    NAVBAR = A1NAVBAR.objects.first()
    NAV_LINKS = A1NAVBAR.objects.all()
    ALLNEWSTODAY = A3NEWSTODAY.objects.all()
    ALLHOTPICKS = A4HOTPICKS.objects.all()
    SUBSCRIBENEWS = A5SUBSCRIBENEWS.objects.last()
    OTHERNEWS = A6OTHERNEWS.objects.last()
    ALLOTHERNEWS = A6OTHERNEWS.objects.all()
    ECOANDWORLD = A7ECOANDWORLD.objects.all()
    LIFESTYLE = A8LIFESTYLE.objects.all()
    BOTTOMNAV = A9BOTTOMNAV.objects.all()
    OURORIGINAL = B1OURORIGINAL.objects.all()
    STOREADS = B2STOREADS.objects.all()
    WEBSITE_TAGS = B3WEBSITE_TAGS.objects.last()
    HORIZONTABANNER = B4HORIZONTABANNER.objects.all()
    KEYWORDS_DES = B5KEYWORDS_DES.objects.last()

    return render(request, 'latest-news.html',{
        'PAGETOP': PAGETOP,
        'NAVBAR': NAVBAR,
        'NAV_LINKS': NAV_LINKS,
        'ALLHOTPICKS': ALLHOTPICKS,
        'SUBSCRIBENEWS': SUBSCRIBENEWS,
        'ALLNEWSTODAY': ALLNEWSTODAY,
        'OTHERNEWS': OTHERNEWS,
        'ALLOTHERNEWS': ALLOTHERNEWS,
        'ECOANDWORLD': ECOANDWORLD,
        'LIFESTYLE': LIFESTYLE,
        'BOTTOMNAV': BOTTOMNAV,
        'OURORIGINAL': OURORIGINAL,
        'STOREADS': STOREADS,
        'WEBSITE_TAGS': WEBSITE_TAGS,
        'HORIZONTABANNER': HORIZONTABANNER,
        'KEYWORDS_DES': KEYWORDS_DES,
    })


def sports_and_entertainment(request):
    PAGETOP = A0PAGETOP.objects.last()
    NAVBAR = A1NAVBAR.objects.first()
    NAV_LINKS = A1NAVBAR.objects.all()
    ALLNEWSTODAY = A3NEWSTODAY.objects.all()
    ALLHOTPICKS = A4HOTPICKS.objects.all()
    HOTPICKS = A4HOTPICKS.objects.last()
    SUBSCRIBENEWS = A5SUBSCRIBENEWS.objects.last()
    OTHERNEWS = A6OTHERNEWS.objects.last()
    ALLOTHERNEWS = A6OTHERNEWS.objects.all()
    ECOANDWORLD = A7ECOANDWORLD.objects.all()
    LIFESTYLE = A8LIFESTYLE.objects.all()
    BOTTOMNAV = A9BOTTOMNAV.objects.all()
    OURORIGINAL = B1OURORIGINAL.objects.all()
    STOREADS = B2STOREADS.objects.all()
    WEBSITE_TAGS = B3WEBSITE_TAGS.objects.last()
    HORIZONTABANNER = B4HORIZONTABANNER.objects.all()
    KEYWORDS_DES = B5KEYWORDS_DES.objects.last()

    return render(request, 'sports_and_entertainment.html',{
        'PAGETOP': PAGETOP,
        'NAVBAR': NAVBAR,
        'NAV_LINKS': NAV_LINKS,
        'ALLHOTPICKS': ALLHOTPICKS,
        'HOTPICKS': HOTPICKS,
        'SUBSCRIBENEWS': SUBSCRIBENEWS,
        'ALLNEWSTODAY': ALLNEWSTODAY,
        'OTHERNEWS': OTHERNEWS,
        'ALLOTHERNEWS': ALLOTHERNEWS,
        'ECOANDWORLD': ECOANDWORLD,
        'LIFESTYLE': LIFESTYLE,
        'BOTTOMNAV': BOTTOMNAV,
        'OURORIGINAL': OURORIGINAL,
        'STOREADS': STOREADS,
        'WEBSITE_TAGS': WEBSITE_TAGS,
        'HORIZONTABANNER': HORIZONTABANNER,
        'KEYWORDS_DES': KEYWORDS_DES,
    })

def economics_and_travel(request):
    PAGETOP = A0PAGETOP.objects.last()
    NAVBAR = A1NAVBAR.objects.first()
    NAV_LINKS = A1NAVBAR.objects.all()
    ALLNEWSTODAY = A3NEWSTODAY.objects.all()
    ALLHOTPICKS = A4HOTPICKS.objects.all()
    HOTPICKS = A4HOTPICKS.objects.last()
    SUBSCRIBENEWS = A5SUBSCRIBENEWS.objects.last()
    OTHERNEWS = A6OTHERNEWS.objects.last()
    ALLOTHERNEWS = A6OTHERNEWS.objects.all()
    ECOANDWORLD = A7ECOANDWORLD.objects.all()
    LIFESTYLE = A8LIFESTYLE.objects.all()
    BOTTOMNAV = A9BOTTOMNAV.objects.all()
    OURORIGINAL = B1OURORIGINAL.objects.all()
    STOREADS = B2STOREADS.objects.all()
    WEBSITE_TAGS = B3WEBSITE_TAGS.objects.last()
    HORIZONTABANNER = B4HORIZONTABANNER.objects.all()
    KEYWORDS_DES = B5KEYWORDS_DES.objects.last()

    return render(request, 'economics_and_travel.html',{
        'PAGETOP': PAGETOP,
        'NAVBAR': NAVBAR,
        'NAV_LINKS': NAV_LINKS,
        'ALLHOTPICKS': ALLHOTPICKS,
        'HOTPICKS': HOTPICKS,
        'SUBSCRIBENEWS': SUBSCRIBENEWS,
        'ALLNEWSTODAY': ALLNEWSTODAY,
        'OTHERNEWS': OTHERNEWS,
        'ALLOTHERNEWS': ALLOTHERNEWS,
        'ECOANDWORLD': ECOANDWORLD,
        'LIFESTYLE': LIFESTYLE,
        'BOTTOMNAV': BOTTOMNAV,
        'OURORIGINAL': OURORIGINAL,
        'STOREADS': STOREADS,
        'WEBSITE_TAGS': WEBSITE_TAGS,
        'HORIZONTABANNER': HORIZONTABANNER,
        'KEYWORDS_DES': KEYWORDS_DES,
    })

def lifestyle(request):
    PAGETOP = A0PAGETOP.objects.last()
    NAVBAR = A1NAVBAR.objects.first()
    NAV_LINKS = A1NAVBAR.objects.all()
    ALLNEWSTODAY = A3NEWSTODAY.objects.all()
    ALLHOTPICKS = A4HOTPICKS.objects.all()
    HOTPICKS = A4HOTPICKS.objects.last()
    SUBSCRIBENEWS = A5SUBSCRIBENEWS.objects.last()
    OTHERNEWS = A6OTHERNEWS.objects.last()
    ALLOTHERNEWS = A6OTHERNEWS.objects.all()
    ECOANDWORLD = A7ECOANDWORLD.objects.all()
    LIFESTYLE = A8LIFESTYLE.objects.all()
    BOTTOMNAV = A9BOTTOMNAV.objects.all()
    OURORIGINAL = B1OURORIGINAL.objects.all()
    STOREADS = B2STOREADS.objects.all()
    WEBSITE_TAGS = B3WEBSITE_TAGS.objects.last()
    HORIZONTABANNER = B4HORIZONTABANNER.objects.all()
    KEYWORDS_DES = B5KEYWORDS_DES.objects.last()

    return render(request, 'lifestyle.html',{
        'PAGETOP': PAGETOP,
        'NAVBAR': NAVBAR,
        'NAV_LINKS': NAV_LINKS,
        'ALLHOTPICKS': ALLHOTPICKS,
        'HOTPICKS': HOTPICKS,
        'SUBSCRIBENEWS': SUBSCRIBENEWS,
        'ALLNEWSTODAY': ALLNEWSTODAY,
        'OTHERNEWS': OTHERNEWS,
        'ALLOTHERNEWS': ALLOTHERNEWS,
        'ECOANDWORLD': ECOANDWORLD,
        'LIFESTYLE': LIFESTYLE,
        'BOTTOMNAV': BOTTOMNAV,
        'OURORIGINAL': OURORIGINAL,
        'STOREADS': STOREADS,
        'WEBSITE_TAGS': WEBSITE_TAGS,
        'HORIZONTABANNER': HORIZONTABANNER,
        'KEYWORDS_DES': KEYWORDS_DES,
    })

def hot_Picks_detail(request, title):
    PAGETOP = A0PAGETOP.objects.last()
    NAVBAR = A1NAVBAR.objects.first()
    NAV_LINKS = A1NAVBAR.objects.all()
    ALLNEWSTODAY = A3NEWSTODAY.objects.all()
    ALLHOTPICKS = A4HOTPICKS.objects.all()
    HOTPICKS = A4HOTPICKS.objects.last()
    SUBSCRIBENEWS = A5SUBSCRIBENEWS.objects.last()
    OTHERNEWS = A6OTHERNEWS.objects.last()
    ALLOTHERNEWS = A6OTHERNEWS.objects.all()
    ECOANDWORLD = A7ECOANDWORLD.objects.all()
    LIFESTYLE = A8LIFESTYLE.objects.all()
    BOTTOMNAV = A9BOTTOMNAV.objects.all()
    OURORIGINAL = B1OURORIGINAL.objects.all()
    STOREADS = B2STOREADS.objects.all()
    WEBSITE_TAGS = B3WEBSITE_TAGS.objects.last()
    HORIZONTABANNER = B4HORIZONTABANNER.objects.all()
    HOTPICKS = get_object_or_404(A4HOTPICKS, Title=title)

    return render(request, 'hot-picks-detail.html',{
        'PAGETOP': PAGETOP,
        'NAVBAR': NAVBAR,
        'NAV_LINKS': NAV_LINKS,
        'ALLHOTPICKS': ALLHOTPICKS,
        'HOTPICKS': HOTPICKS,
        'SUBSCRIBENEWS': SUBSCRIBENEWS,
        'ALLNEWSTODAY': ALLNEWSTODAY,
        'OTHERNEWS': OTHERNEWS,
        'ALLOTHERNEWS': ALLOTHERNEWS,
        'ECOANDWORLD': ECOANDWORLD,
        'LIFESTYLE': LIFESTYLE,
        'BOTTOMNAV': BOTTOMNAV,
        'OURORIGINAL': OURORIGINAL,
        'STOREADS': STOREADS,
        'WEBSITE_TAGS': WEBSITE_TAGS,
        'HORIZONTABANNER': HORIZONTABANNER,
    })

def top_Picks_detail(request, title):
    PAGETOP = A0PAGETOP.objects.last()
    NAVBAR = A1NAVBAR.objects.first()
    NAV_LINKS = A1NAVBAR.objects.all()
    ALLNEWSTODAY = A3NEWSTODAY.objects.all()
    ALLHOTPICKS = A4HOTPICKS.objects.all()
    HOTPICKS = A4HOTPICKS.objects.last()
    SUBSCRIBENEWS = A5SUBSCRIBENEWS.objects.last()
    OTHERNEWS = A6OTHERNEWS.objects.last()
    ALLOTHERNEWS = A6OTHERNEWS.objects.all()
    ECOANDWORLD = A7ECOANDWORLD.objects.all()
    LIFESTYLE = A8LIFESTYLE.objects.all()
    BOTTOMNAV = A9BOTTOMNAV.objects.all()
    OURORIGINAL = B1OURORIGINAL.objects.all()
    STOREADS = B2STOREADS.objects.all()
    WEBSITE_TAGS = B3WEBSITE_TAGS.objects.last()
    HORIZONTABANNER = B4HORIZONTABANNER.objects.all()
    TOP_PICKS = get_object_or_404(A2TOPPICKS, Title=title)

    return render(request, 'top-picks-detail.html',{
        'PAGETOP': PAGETOP,
        'NAVBAR': NAVBAR,
        'NAV_LINKS': NAV_LINKS,
        'ALLHOTPICKS': ALLHOTPICKS,
        'HOTPICKS': HOTPICKS,
        'TOP_PICKS': TOP_PICKS,
        'SUBSCRIBENEWS': SUBSCRIBENEWS,
        'ALLNEWSTODAY': ALLNEWSTODAY,
        'OTHERNEWS': OTHERNEWS,
        'ALLOTHERNEWS': ALLOTHERNEWS,
        'ECOANDWORLD': ECOANDWORLD,
        'LIFESTYLE': LIFESTYLE,
        'BOTTOMNAV': BOTTOMNAV,
        'OURORIGINAL': OURORIGINAL,
        'STOREADS': STOREADS,
        'WEBSITE_TAGS': WEBSITE_TAGS,
        'HORIZONTABANNER': HORIZONTABANNER,
    })

def latest_news_detail(request, title):
    PAGETOP = A0PAGETOP.objects.last()
    NAVBAR = A1NAVBAR.objects.first()
    NAV_LINKS = A1NAVBAR.objects.all()
    ALLNEWSTODAY = A3NEWSTODAY.objects.all()
    ALLHOTPICKS = A4HOTPICKS.objects.all()
    HOTPICKS = A4HOTPICKS.objects.last()
    SUBSCRIBENEWS = A5SUBSCRIBENEWS.objects.last()
    OTHERNEWS = A6OTHERNEWS.objects.last()
    ALLOTHERNEWS = A6OTHERNEWS.objects.all()
    ECOANDWORLD = A7ECOANDWORLD.objects.all()
    LIFESTYLE = A8LIFESTYLE.objects.all()
    BOTTOMNAV = A9BOTTOMNAV.objects.all()
    OURORIGINAL = B1OURORIGINAL.objects.all()
    STOREADS = B2STOREADS.objects.all()
    WEBSITE_TAGS = B3WEBSITE_TAGS.objects.last()
    HORIZONTABANNER = B4HORIZONTABANNER.objects.all()
    ALL_NEWS_TODAY = get_object_or_404(A3NEWSTODAY, Title=title)

    return render(request, 'latest-news-detail.html',{
        'PAGETOP': PAGETOP,
        'NAVBAR': NAVBAR,
        'NAV_LINKS': NAV_LINKS,
        'ALLHOTPICKS': ALLHOTPICKS,
        'HOTPICKS': HOTPICKS,
        'SUBSCRIBENEWS': SUBSCRIBENEWS,
        'ALLNEWSTODAY': ALLNEWSTODAY,
        'OTHERNEWS': OTHERNEWS,
        'ALLOTHERNEWS': ALLOTHERNEWS,
        'ECOANDWORLD': ECOANDWORLD,
        'LIFESTYLE': LIFESTYLE,
        'BOTTOMNAV': BOTTOMNAV,
        'OURORIGINAL': OURORIGINAL,
        'STOREADS': STOREADS,
        'WEBSITE_TAGS': WEBSITE_TAGS,
        'HORIZONTABANNER': HORIZONTABANNER,
        'ALL_NEWS_TODAY': ALL_NEWS_TODAY,
    })

def sports_and_entertainment_detail(request, title):
    PAGETOP = A0PAGETOP.objects.last()
    NAVBAR = A1NAVBAR.objects.first()
    NAV_LINKS = A1NAVBAR.objects.all()
    ALLNEWSTODAY = A3NEWSTODAY.objects.all()
    ALLHOTPICKS = A4HOTPICKS.objects.all()
    HOTPICKS = A4HOTPICKS.objects.last()
    SUBSCRIBENEWS = A5SUBSCRIBENEWS.objects.last()
    OTHERNEWS = A6OTHERNEWS.objects.last()
    ALLOTHERNEWS = A6OTHERNEWS.objects.all()
    ECOANDWORLD = A7ECOANDWORLD.objects.all()
    LIFESTYLE = A8LIFESTYLE.objects.all()
    BOTTOMNAV = A9BOTTOMNAV.objects.all()
    OURORIGINAL = B1OURORIGINAL.objects.all()
    STOREADS = B2STOREADS.objects.all()
    WEBSITE_TAGS = B3WEBSITE_TAGS.objects.last()
    HORIZONTABANNER = B4HORIZONTABANNER.objects.all()
    ALL_OTHERNEWS = get_object_or_404(A6OTHERNEWS, Title=title)

    return render(request, 'sports_and_entertainment_detail.html',{
        'PAGETOP': PAGETOP,
        'NAVBAR': NAVBAR,
        'NAV_LINKS': NAV_LINKS,
        'ALLHOTPICKS': ALLHOTPICKS,
        'HOTPICKS': HOTPICKS,
        'SUBSCRIBENEWS': SUBSCRIBENEWS,
        'ALLNEWSTODAY': ALLNEWSTODAY,
        'OTHERNEWS': OTHERNEWS,
        'ALLOTHERNEWS': ALLOTHERNEWS,
        'ECOANDWORLD': ECOANDWORLD,
        'LIFESTYLE': LIFESTYLE,
        'BOTTOMNAV': BOTTOMNAV,
        'OURORIGINAL': OURORIGINAL,
        'STOREADS': STOREADS,
        'WEBSITE_TAGS': WEBSITE_TAGS,
        'HORIZONTABANNER': HORIZONTABANNER,
        'ALL_OTHERNEWS': ALL_OTHERNEWS,
    })

def economics_and_travel_detail(request, title):
    PAGETOP = A0PAGETOP.objects.last()
    NAVBAR = A1NAVBAR.objects.first()
    NAV_LINKS = A1NAVBAR.objects.all()
    ALLNEWSTODAY = A3NEWSTODAY.objects.all()
    ALLHOTPICKS = A4HOTPICKS.objects.all()
    HOTPICKS = A4HOTPICKS.objects.last()
    SUBSCRIBENEWS = A5SUBSCRIBENEWS.objects.last()
    OTHERNEWS = A6OTHERNEWS.objects.last()
    ALLOTHERNEWS = A6OTHERNEWS.objects.all()
    ECOANDWORLD = A7ECOANDWORLD.objects.all()
    LIFESTYLE = A8LIFESTYLE.objects.all()
    BOTTOMNAV = A9BOTTOMNAV.objects.all()
    OURORIGINAL = B1OURORIGINAL.objects.all()
    STOREADS = B2STOREADS.objects.all()
    WEBSITE_TAGS = B3WEBSITE_TAGS.objects.last()
    HORIZONTABANNER = B4HORIZONTABANNER.objects.all()
    ALL_ECOANDWORLD = get_object_or_404(A7ECOANDWORLD, Title=title)

    return render(request, 'economics_and_travel_detail.html',{
        'PAGETOP': PAGETOP,
        'NAVBAR': NAVBAR,
        'NAV_LINKS': NAV_LINKS,
        'ALLHOTPICKS': ALLHOTPICKS,
        'HOTPICKS': HOTPICKS,
        'SUBSCRIBENEWS': SUBSCRIBENEWS,
        'ALLNEWSTODAY': ALLNEWSTODAY,
        'OTHERNEWS': OTHERNEWS,
        'ALLOTHERNEWS': ALLOTHERNEWS,
        'ECOANDWORLD': ECOANDWORLD,
        'LIFESTYLE': LIFESTYLE,
        'BOTTOMNAV': BOTTOMNAV,
        'OURORIGINAL': OURORIGINAL,
        'STOREADS': STOREADS,
        'WEBSITE_TAGS': WEBSITE_TAGS,
        'HORIZONTABANNER': HORIZONTABANNER,
        'ALL_ECOANDWORLD': ALL_ECOANDWORLD,
    })

def lifestyle_detail(request, title):
    PAGETOP = A0PAGETOP.objects.last()
    NAVBAR = A1NAVBAR.objects.first()
    NAV_LINKS = A1NAVBAR.objects.all()
    ALLNEWSTODAY = A3NEWSTODAY.objects.all()
    ALLHOTPICKS = A4HOTPICKS.objects.all()
    HOTPICKS = A4HOTPICKS.objects.last()
    SUBSCRIBENEWS = A5SUBSCRIBENEWS.objects.last()
    OTHERNEWS = A6OTHERNEWS.objects.last()
    ALLOTHERNEWS = A6OTHERNEWS.objects.all()
    ECOANDWORLD = A7ECOANDWORLD.objects.all()
    LIFESTYLE = A8LIFESTYLE.objects.all()
    BOTTOMNAV = A9BOTTOMNAV.objects.all()
    OURORIGINAL = B1OURORIGINAL.objects.all()
    STOREADS = B2STOREADS.objects.all()
    WEBSITE_TAGS = B3WEBSITE_TAGS.objects.last()
    HORIZONTABANNER = B4HORIZONTABANNER.objects.all()
    ALL_LIFESTYLE = get_object_or_404(A8LIFESTYLE, Title=title)

    return render(request, 'lifestyle_detail.html',{
        'PAGETOP': PAGETOP,
        'NAVBAR': NAVBAR,
        'NAV_LINKS': NAV_LINKS,
        'ALLHOTPICKS': ALLHOTPICKS,
        'HOTPICKS': HOTPICKS,
        'SUBSCRIBENEWS': SUBSCRIBENEWS,
        'ALLNEWSTODAY': ALLNEWSTODAY,
        'OTHERNEWS': OTHERNEWS,
        'ALLOTHERNEWS': ALLOTHERNEWS,
        'ECOANDWORLD': ECOANDWORLD,
        'LIFESTYLE': LIFESTYLE,
        'BOTTOMNAV': BOTTOMNAV,
        'OURORIGINAL': OURORIGINAL,
        'STOREADS': STOREADS,
        'WEBSITE_TAGS': WEBSITE_TAGS,
        'HORIZONTABANNER': HORIZONTABANNER,
        'ALL_LIFESTYLE': ALL_LIFESTYLE,
    })
