from django.urls import path
from. import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('dashboard/', views.dashboard, name='dashboard'),
	path('template/', views.template, name='template'),

	path('category/', views.category, name='category'),
	path('add_template/', views.add_template, name='add_template'),

	path('add_category/', views.add_category, name='add_category'),
]


urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)