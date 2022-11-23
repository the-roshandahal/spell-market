from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('template/', views.template, name='template'),


    path('add_template/', views.add_template, name='add_template'),
    path('category/', views.category, name='category'),
    path('add_category/', views.add_category, name='add_category'),

    path('sub_category/', views.sub_category, name='sub_category'),
    path('add_sub_category/', views.add_sub_category, name='add_sub_category'),

    path('child_category/', views.child_category, name='child_category'),
    path('add_child_category/', views.add_child_category,name='add_child_category'),

    path('edit_template/<int:id>', views.edit_template, name='edit_template'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
