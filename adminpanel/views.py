from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required
import json
from django.core.serializers.json import DjangoJSONEncoder
def dashboard(request):
    if request.user.is_authenticated:
        templates_ct=Template.objects.count()
        context = {
            'templates_ct': templates_ct
        }
        return render(request, 'admin/dashboard.html',context)
    else:
        messages.info(request, 'You are not logged in. Please log in to continue')
        return redirect('login')

@login_required
def template(request):
    template = Template.objects.all()
    return render(request, 'admin/template.html', {'template': template})


def add_template(request):

    if request.method == "POST":
        cat_id = request.POST['category']
        sub_cat_id = request.POST['sub_category']
        child_cat_id = request.POST['child_category']
        template_name = request.POST['template_name']
        template_details = request.POST['template_details']
        template_features = request.POST['template_features']
        template_layout = request.POST['template_layout']
        template_price = request.POST['template_price']
        version = request.POST['version']
        framework = request.POST['framework']
        template_image = request.FILES['template_image']
        template_url = request.POST['template_url']
        is_featured = request.POST['is_featured']

        category = Category.objects.get(id=cat_id)
        sub_category = SubCategory.objects.get(id=sub_cat_id)
        child_category = ChildCategory.objects.get(id=child_cat_id)

        Template.objects.create(category=category, sub_category=sub_category,child_category=child_category,template_name=template_name, template_details=template_details, template_features=template_features,
                                template_layout=template_layout, template_price=template_price, version=version, framework=framework,
                                template_image=template_image, template_url=template_url, is_featured=is_featured)

        return redirect('template')
    cat = Category.objects.all()
    sub_cat = SubCategory.objects.all()
    child_cat = ChildCategory.objects.all()
    context = {
        'cat': cat,
        'sub_cat': sub_cat,
        'child_cat': child_cat
    }
    return render(request, 'admin/add_template.html', context)


def category(request):
    category = Category.objects.all().order_by('order')
    context = {
        'category': category
    }
    return render(request, 'admin/category.html', context)


def add_category(request):
    if request.method == "POST":
        category = request.POST['category']
        order = request.POST['order']
        status = request.POST['status']
        category_image = request.FILES['category_image']
        if Category.objects.filter(category=category).exists():
            messages.info(request, 'the category is already taken')
            return redirect('add_category')
        Category.objects.create(
            category=category, order=order, status=status, category_image=category_image)
        return redirect('category')
    return render(request, 'admin/add_category.html')


def sub_category(request):
    sub_category = SubCategory.objects.all().order_by('order')
    context = {
        'sub_category': sub_category
    }
    return render(request, 'admin/sub_category.html', context)


def add_sub_category(request):
    if request.method == "POST":
        cat_id = request.POST['category']
        sub_category = request.POST['sub_category']
        order = request.POST['order']
        status = request.POST['status']

        if SubCategory.objects.filter(sub_category=sub_category).exists():
            messages.info(request, 'the category is already taken')
            return redirect('add_sub_category')

        category = Category.objects.get(id=cat_id)
        SubCategory.objects.create(
            category=category, order=order, status=status, sub_category=sub_category)
        return redirect('sub_category')
    cat = Category.objects.all()
    context = {
        'cat': cat
    }
    return render(request, 'admin/add_sub_category.html', context)


def child_category(request):
    child_category = ChildCategory.objects.all().order_by('order')
    context = {
        'child_category': child_category
    }
    return render(request, 'admin/child_category.html', context)


def add_child_category(request):
    if request.method == "POST":
        sub_cat_id = request.POST['category']
        child_category = request.POST['child_category']
        order = request.POST['order']
        status = request.POST['status']

        if ChildCategory.objects.filter(child_category=child_category).exists():
            messages.info(request, 'the category is already taken')
            return redirect('add_sub_category')

        sub_category = SubCategory.objects.get(id=sub_cat_id)
        ChildCategory.objects.create(
            sub_category=sub_category, order=order, status=status, child_category=child_category)
        return redirect('child_category')

    cat = Category.objects.all()
    sub_cat = SubCategory.objects.all()
    context ={
        "cat": cat,
        "sub_cat": sub_cat
    }
  
    return render(request, 'admin/add_child_category.html', context)


def load_sub_category(request):
    cat=request.GET.get("cat")
    sub_cat = SubCategory.objects.filter(category=cat)
    return render(request, 'admin/load_sub_category.html', {'sub_cat': sub_cat})


def load_child_category(request):
    sub_cat=request.GET.get("sub_cat")
    child_cat = ChildCategory.objects.filter(sub_category=sub_cat)
    return render(request, 'admin/load_child_category.html', {'child_cat': child_cat})


def edit_template(request,id):
    if request.method == 'POST':
        cat_id = request.POST['category']
        sub_cat_id = request.POST['sub_category']
        child_cat_id = request.POST['child_category']
        template_name = request.POST['template_name']
        template_details = request.POST['template_details']
        template_features = request.POST['template_features']
        template_layout = request.POST['template_layout']
        template_price = request.POST['template_price']
        version = request.POST['version']
        framework = request.POST['framework']
        if ( request.FILES and request.FILES['template_image']):
            template_image = request.FILES['template_image']
        else:
            template_image=None
        template_url = request.POST['template_url']

        category = Category.objects.get(id=cat_id)
        sub_category = SubCategory.objects.get(id=sub_cat_id)
        child_category = ChildCategory.objects.get(id=child_cat_id)

        template_data = Template.objects.filter(id=id)[0]

        template_data.category=category
        template_data.sub_category=sub_category
        template_data.child_category=child_category
        template_data.sub_category=sub_category
        template_data.child_category=child_category
        template_data.template_name=template_name
        template_data.template_details=template_details
        template_data.template_features=template_features
        template_data.template_layout=template_layout
        template_data.template_price=template_price
        template_data.version=version
        template_data.framework=framework
        template_data.template_url=template_url
        if(template_image):
            template_data.template_image=template_image
        

        template_data.save()
        return redirect('template')

    else:
        cat = Category.objects.all()
        sub_cat = SubCategory.objects.all()
        child_cat = ChildCategory.objects.all()
        template_data = Template.objects.filter(id=id)[0]

        context = {
            'cat': cat,
            'sub_cat': sub_cat,
            'child_cat': child_cat,
            'template_data':template_data
        }
        return render(request,'admin/edit_template.html',context)

def change_status(request, id):
    status = Template.objects.get(id=id)
    print(status.is_featured)
    if (status.is_featured == True):
        status_update = Template.objects.filter(id=id)[0]
        status_update.is_featured = 'False'
        status_update.save()
        return redirect(template)
    else:
        status_update = Template.objects.filter(id=id)[0]
        status_update.is_featured = 'True'
        status_update.save()
        return redirect(template)
