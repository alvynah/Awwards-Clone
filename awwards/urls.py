from django.urls import path,re_path
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('',views.welcome,name='welcome'),
    re_path(r'^review/(?P<project_id>\d+)', views.rate_project, name='rate'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)