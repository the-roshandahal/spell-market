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
    
    path('load_sub_category/', views.load_sub_category, name='load_sub_category'),
    path('load_child_category/', views.load_child_category, name='load_child_category'),

    path('edit_template/<int:id>', views.edit_template, name='edit_template'),
    path('delete_template/<int:id>',views.delete_template,name='delete_template'),

    path('change_status/<int:id>', views.change_status, name='change_status'),

    path('delete_category/<int:id>',views.delete_category,name='delete_category'),
    path('change_cat_status/<int:id>', views.change_cat_status, name='change_cat_status'),
     path('edit_category/<int:id>', views.edit_category, name='edit_category'),
    
    path('delete_sub_category/<int:id>',views.delete_sub_category,name='delete_sub_category'),
    path('change_sub_cat_status/<int:id>', views.change_sub_cat_status, name='change_sub_cat_status'),
    path('edit_sub_category/<int:id>', views.edit_sub_category, name='edit_sub_category'),

    path('delete_child_category/<int:id>',views.delete_child_category,name='delete_child_category'),
    path('change_child_cat_status/<int:id>', views.change_child_cat_status, name='change_child_cat_status'),
    path('edit_child_category/<int:id>', views.edit_child_category, name='edit_child_category'),
    
    

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
