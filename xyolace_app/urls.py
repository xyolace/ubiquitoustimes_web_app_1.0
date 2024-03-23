from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index, name = 'home'),

    path('signin', views.signin, name = 'signin'),
    path('signup', views.signup, name = 'signup'),
    path('logout', views.logout, name = 'logout'),
    path('user/<str:username>', views.user_profile, name = 'user'),
    path('user/change-user-information/<str:username>', views.change_user_info, name = 'change_user_info'), #change

    path('top-picks/', views.top_picks,  name = 'top-picks'),
    path('top-picks/detail/<str:title>/', views.top_Picks_detail, name='Top-Picks-detail'),

    path('hot-picks/', views.hot_picks,  name = 'hot-picks'),
    path('hot-picks/detail/<str:title>/', views.hot_Picks_detail, name='Hot-Picks-detail'),

    path('Latest-News/', views.latest_news,  name = 'Latest-News'),
    path('Latest-News/detail/<str:title>/', views.latest_news_detail, name='Latest-News-detail'),

    path('Sports-and-entertainment/', views.sports_and_entertainment,  name = 'Sports-and-entertainment'),
    path('Sports-and-entertainment/detail/<str:title>/', views.sports_and_entertainment_detail, name='sports-and-entertainment-detail'),

    path('Economics-and-travel/', views.economics_and_travel,  name = 'Economics-and-travel'),
    path('Economics-and-travel/detail/<str:title>/', views.economics_and_travel_detail, name='Economics-and-travel-detail'),

    path('LifeStyle/', views.lifestyle,  name = 'LifeStyle'),
    path('LifeStyle/detail/<str:title>/', views.lifestyle_detail, name='LifeStyle-detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)