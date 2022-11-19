from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import *


def dashboard(request):
	return render(request,'admin/dashboard.html')

def template(request):
    return render(request, 'admin/template.html')

def add_template(request):

    if request.method == "POST":
        category = request.POST['category']
        template_name = request.POST['template_name']
        template_details = request.POST['template_details']
        template_features = request.POST['template_features']
        template_layout = request.POST['template_layout']
        template_price = request.POST['template_price']
        version = request.POST['version']
        framework = request.POST['framework']
        template_image = request.FILES['template_image']
        template_url = request.POST['template_url']
                
        Template.objects.create(category=category, template_name=template_name,template_details=template_details,template_features=template_features,
        template_layout=template_layout,template_price=template_price,version=version,framework=framework,
        template_image=template_image,template_url=template_url)
        
        return redirect('template')
    cat = Category.objects.all()
    context={
    'cat':cat
    }
    return render(request, 'admin/addtemplate.html',context)

def category(request):
    category = Category.objects.all()
    context={
        'category':category
    }
    return render(request, 'admin/category.html',context)

def add_category(request):
    if request.method == "POST":
        category = request.POST['category']
        order = request.POST['order']
        status = request.POST['status']
        category_image = request.FILES['category_image']
        if Category.objects.filter(category=category).exists():
            messages.info(request, 'the category is already taken')
            return redirect('add_category')
        Category.objects.create(category=category,order=order, status= status, category_image = category_image)
        return redirect('category')
    return render(request, 'admin/addcategory.html')


