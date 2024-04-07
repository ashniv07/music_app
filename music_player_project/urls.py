from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from music_player import views

urlpatterns = [
    path('', views.index, name='home'),  # Home page
    path('admin/', admin.site.urls),
    path('music/', include('music_player.urls')),
    path('register/', views.register, name='register'),  # Register page
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
       path('about_us.html', views.about_us_view, name='about_us'),
        
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
