from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name='list'),
    path('new-post/', views.posts_new, name='new-post'),
    path('post/<slug:slug>/', views.post_page, name='page'),

     
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                   document_root=settings.MEDIA_ROOT)