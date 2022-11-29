from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    templates_ct = Template.objects.count()
    context = {"templates_ct": templates_ct}
    return render(request, "admin/dashboard.html", context)


@login_required
def category(request):
    category = Category.objects.all().order_by("order")
    context = {"category": category}
    return render(request, "admin/category.html", context)


@login_required
def add_category(request):
    if request.method == "POST":
        category = request.POST["category"]
        order = request.POST["order"]
        status = request.POST["status"]
        category_image = request.FILES["category_image"]
        if Category.objects.filter(category=category).exists():
            messages.info(request, "the category is already taken")
            return redirect("add_category")
        Category.objects.create(
            category=category, order=order, status=status, category_image=category_image
        )
        messages.info(request, "Category added successfully.")
        return redirect("category")
    return render(request, "admin/add_category.html")

def edit_category(request,id):
    if request.method == "POST":
        cat_category = request.POST["category"]
        order = request.POST["order"]
        if request.FILES and request.FILES["category_image"]:
            category_image = request.FILES["category_image"]
        else:
            category_image = None
        new_category = Category.objects.get(id=id)
        new_category.category = cat_category
        new_category.order = order
        if category_image:
            new_category.category_image = category_image
        new_category.save()
        messages.info(request, "Category edited successfully.")
        return redirect(category)
    else:
        cat_data = Category.objects.get(id=id)
        context = {
            "cat_data":cat_data
        }        
    return render(request, "admin/edit_category.html",context)

@login_required
def delete_category(request, id):
    del_category = Category.objects.get(id=id)
    del_category.delete()
    messages.info(request, "Deleted")
    return redirect(category)


@login_required
def change_cat_status(request, id):
    cat_status = Category.objects.get(id=id)
    if cat_status.status == "active":
        status_update = Category.objects.filter(id=id)[0]
        status_update.status = "inactive"
        status_update.save()
        messages.info(request, "Status Changed")
        return redirect(category)
    else:
        status_update = Category.objects.filter(id=id)[0]
        status_update.status = "active"
        status_update.save()
        messages.info(request, "Status Changed")
        return redirect(category)


@login_required
def sub_category(request):
    sub_category = SubCategory.objects.all().order_by("order")
    context = {"sub_category": sub_category}
    return render(request, "admin/sub_category.html", context)

@login_required
def add_sub_category(request):
    if request.method == "POST":
        cat_id = request.POST["category"]
        sub_category = request.POST["sub_category"]
        order = request.POST["order"]
        status = request.POST["status"]

        if SubCategory.objects.filter(sub_category=sub_category).exists():
            messages.info(request, "the category is already taken")
            return redirect("add_sub_category")

        category = Category.objects.get(id=cat_id)
        SubCategory.objects.create(
            category=category, order=order, status=status, sub_category=sub_category
        )
        messages.info(request, "Sub category added successfully.")

        return redirect("sub_category")
    cat = Category.objects.all()
    context = {"cat": cat}
    return render(request, "admin/add_sub_category.html", context)

def edit_sub_category(request,id):
    if request.method == "POST":
        cat_id = request.POST["category"]
        sub_sub_category = request.POST["sub_category"]
        order = request.POST["order"]

        category = Category.objects.get(id=cat_id)
        new_sub_category = SubCategory.objects.get(id=id)

        new_sub_category.category = category
        new_sub_category.sub_category = sub_sub_category
        new_sub_category.order = order
        new_sub_category.save()

        return redirect("sub_category")
    else:
        cat = Category.objects.all()
        sub_cat_data = SubCategory.objects.get(id=id)
        context = {
            "cat":cat,
            "sub_cat_data":sub_cat_data
        }        
    return render(request, "admin/edit_sub_category.html",context)

@login_required
def delete_sub_category(request, id):
    del_sub_category = SubCategory.objects.get(id=id)
    del_sub_category.delete()
    messages.info(request, "Deleted")
    return redirect(sub_category)


@login_required
def change_sub_cat_status(request, id):
    sub_cat_status = SubCategory.objects.get(id=id)
    if sub_cat_status.status == "active":
        status_update = SubCategory.objects.filter(id=id)[0]
        status_update.status = "inactive"
        status_update.save()
        messages.info(request, "Status Changed")
        return redirect(sub_category)
    else:
        status_update = SubCategory.objects.filter(id=id)[0]
        status_update.status = "active"
        status_update.save()
        messages.info(request, "Status Changed")
        return redirect(sub_category)


def child_category(request):
    child_category = ChildCategory.objects.all().order_by("order")
    context = {"child_category": child_category}
    return render(request, "admin/child_category.html", context)


@login_required
def add_child_category(request):
    if request.method == "POST":
        sub_cat_id = request.POST["category"]
        child_category = request.POST["child_category"]
        order = request.POST["order"]
        status = request.POST["status"]

        if ChildCategory.objects.filter(child_category=child_category).exists():
            messages.info(request, "the category is already taken")
            return redirect("add_sub_category")

        sub_category = SubCategory.objects.get(id=sub_cat_id)
        ChildCategory.objects.create(
            sub_category=sub_category,
            order=order,
            status=status,
            child_category=child_category,
        )
        messages.info(request, "Child category added successfully.")
        return redirect("child_category")

    cat = Category.objects.all()
    sub_cat = SubCategory.objects.all()
    context = {"cat": cat, "sub_cat": sub_cat}

    return render(request, "admin/add_child_category.html", context)


def edit_child_category(request,id):
    if request.method == "POST":
        sub_cat_id = request.POST["category"]
        child_child_category = request.POST["child_category"]
        order = request.POST["order"]

        sub_category = SubCategory.objects.get(id=sub_cat_id)
        new_child_category = ChildCategory.objects.get(id=id)

        new_child_category.sub_category = sub_category
        new_child_category.order= order
        new_child_category.child_category=child_child_category
        new_child_category.save()
        
        messages.info(request, "Child category edited successfully.")
        return redirect(child_category)
    else:
        cat = Category.objects.all()
        sub_cat = SubCategory.objects.all()
        child_cat_data = ChildCategory.objects.get(id=id)
        
        context = {
            "cat":cat,
            "sub_cat":sub_cat,
            "child_cat_data":child_cat_data,
        } 
        return render(request, "admin/edit_child_category.html",context)

@login_required
def delete_child_category(request, id):
    del_child_category = ChildCategory.objects.get(id=id)
    del_child_category.delete()
    messages.info(request, "Deleted")
    return redirect(child_category)


@login_required
def change_child_cat_status(request, id):
    child_cat_status = ChildCategory.objects.get(id=id)
    if child_cat_status.status == "active":
        status_update = ChildCategory.objects.filter(id=id)[0]
        status_update.status = "inactive"
        status_update.save()
        messages.info(request, "Status Changed")
        return redirect(child_category)
    else:
        status_update = ChildCategory.objects.filter(id=id)[0]
        status_update.status = "active"
        status_update.save()
        messages.info(request, "Status Changed")
        return redirect(child_category)

@login_required
def template(request):
    template = Template.objects.all()
    return render(request, "admin/template.html", {"template": template})


@login_required
def add_template(request):
    if request.method == "POST":
        cat_id = request.POST["category"]
        sub_cat_id = request.POST["sub_category"]
        child_cat_id = request.POST["child_category"]
        template_name = request.POST["template_name"]
        template_details = request.POST["template_details"]
        template_features = request.POST["template_features"]
        template_layout = request.POST["template_layout"]
        template_price = request.POST["template_price"]
        version = request.POST["version"]
        framework = request.POST["framework"]
        template_image = request.FILES["template_image"]
        template_url = request.POST["template_url"]
        is_featured = request.POST["is_featured"]

        category = Category.objects.get(id=cat_id)
        sub_category = SubCategory.objects.get(id=sub_cat_id)
        child_category = ChildCategory.objects.get(id=child_cat_id)

        Template.objects.create(
            category=category,
            sub_category=sub_category,
            child_category=child_category,
            template_name=template_name,
            template_details=template_details,
            template_features=template_features,
            template_layout=template_layout,
            template_price=template_price,
            version=version,
            framework=framework,
            template_image=template_image,
            template_url=template_url,
            is_featured=is_featured,
        )

        return redirect("template")
    cat = Category.objects.all()
    sub_cat = SubCategory.objects.all()
    child_cat = ChildCategory.objects.all()
    context = {"cat": cat, "sub_cat": sub_cat, "child_cat": child_cat}
    return render(request, "admin/add_template.html", context)








@login_required
def edit_template(request, id):
    if request.method == "POST":
        cat_id = request.POST["category"]
        sub_cat_id = request.POST["sub_category"]
        child_cat_id = request.POST["child_category"]
        template_name = request.POST["template_name"]
        template_details = request.POST["template_details"]
        template_features = request.POST["template_features"]
        template_layout = request.POST["template_layout"]
        template_price = request.POST["template_price"]
        version = request.POST["version"]
        framework = request.POST["framework"]
        if request.FILES and request.FILES["template_image"]:
            template_image = request.FILES["template_image"]
        else:
            template_image = None
        template_url = request.POST["template_url"]

        category = Category.objects.get(id=cat_id)
        sub_category = SubCategory.objects.get(id=sub_cat_id)
        child_category = ChildCategory.objects.get(id=child_cat_id)

        template_data = Template.objects.filter(id=id)[0]

        template_data.category = category
        template_data.sub_category = sub_category
        template_data.child_category = child_category
        template_data.sub_category = sub_category
        template_data.child_category = child_category
        template_data.template_name = template_name
        template_data.template_details = template_details
        template_data.template_features = template_features
        template_data.template_layout = template_layout
        template_data.template_price = template_price
        template_data.version = version
        template_data.framework = framework
        template_data.template_url = template_url
        if template_image:
            template_data.template_image = template_image

        template_data.save()
        messages.info(request, "Template edited successfully.")

        return redirect("template")

    else:
        cat = Category.objects.all()
        sub_cat = SubCategory.objects.all()
        child_cat = ChildCategory.objects.all()
        template_data = Template.objects.filter(id=id)[0]

        context = {
            "cat": cat,
            "sub_cat": sub_cat,
            "child_cat": child_cat,
            "template_data": template_data,
        }
        return render(request, "admin/edit_template.html", context)
    
@login_required
def load_sub_category(request):
    cat = request.GET.get("cat")
    sub_cat = SubCategory.objects.filter(category=cat)
    return render(request, "admin/load_sub_category.html", {"sub_cat": sub_cat})


@login_required
def load_child_category(request):
    sub_cat = request.GET.get("sub_cat")
    child_cat = ChildCategory.objects.filter(sub_category=sub_cat)
    return render(request, "admin/load_child_category.html", {"child_cat": child_cat})

@login_required
def change_status(request, id):
    status = Template.objects.get(id=id)
    if status.is_featured == True:
        status_update = Template.objects.filter(id=id)[0]
        status_update.is_featured = "False"
        status_update.save()
        messages.info(request, "Status Changed")
        return redirect(template)
    else:
        status_update = Template.objects.filter(id=id)[0]
        status_update.is_featured = "True"
        status_update.save()
        messages.info(request, "Status Changed")
        return redirect(template)


@login_required(login_url='login')
def delete_template(request, id):
    del_template = Template.objects.get(id=id)
    del_template.delete()
    messages.info(request, "Deleted")
    return redirect(template)


# def post_blog(request):
#     if request.method == "POST":
#         title = request.POST["title"]
#         blog = request.POST["blog"]
#         image = request.FILE["image"]
#         Blog.objects.create(title=title,blog=blog,image=image)
#         messages.info(request, "Blog added")
#         return redirect(post_blog)
#     return render (redirect,'post_blog.html')


def blog(request):
    blog_data = Blog.objects.all()
    context = {
        'blog_data':blog_data,
    }
    return render(request,'blogs.html',context)



def blog_single(request, id):
    blog_data = Blog.objects.get(id=id)
    context = {
        'blog_data':blog_data
    }
    return render (request, 'blog_single.html',context)