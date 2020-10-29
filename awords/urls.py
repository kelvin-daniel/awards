from . import views
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import views as authViews 
from .views import Signup

#url urlpatterns
urlpatterns=[
   path('',views.index, name='index'),
   path('accounts/register/', Signup, name='signup'),
   path('accounts/login/', authViews.LoginView.as_view(template_name='registration/login.html'), name='login'),
   path('logout/', authViews.LogoutView.as_view(), {'next_page' : 'index'}, name='logout'),
   path('project/post/',views.post,name='post'),
   path('user/profile/',views.profile,name='profile'),
   re_path('project/(\d+)/',views.project_detail,name='details'),
   path('search/projects/results/',views.search,name="search"),
   path('api/projects/',views.ProjectList.as_view()),
   path('api/profile/',views.ProfileList.as_view()),
   path('token/', obtain_auth_token),
   path('developer/api/',views.apiView,name='api'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)