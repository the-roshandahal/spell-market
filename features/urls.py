from django.urls import path
from. import views
from django.urls import re_path
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static


urlpatterns = [
	path('',views.home, name='home'),
	path('login/', views.login, name='login'),
	path('register/', views.register, name='register'), 
	path('success/<auth_token>', views.success, name='success'),
	path('logout/', views.logout, name='logout'),
    path('theme/', views.theme, name='theme'),
    path('contact/', views.contact, name='contact'),



	re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)