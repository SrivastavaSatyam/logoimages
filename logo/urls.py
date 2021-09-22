"""logo_image URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path



from images import views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('admin/', admin.site.urls),
    # path('add/', views.add,name="add"),
    path('',views.Display_All,name="index"),
    path('about/',views.about,name="about"),
    path('images/',views.View_images,name="View_images"),
    path('images/<str:slug>/',views.Display_Images,name="Display_Images"),
    path('users/',views.users,name="users"),
    path('users/register/',user_views.register,name="register"),
    path('users/login/',user_views.login,name="login"),
    path('users/logout/',user_views.logout,name="logout"),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



handler400='images.views.error_400'
handler403='images.views.error_403'
handler404='images.views.error_404'
# handler500='images.views.error_500'