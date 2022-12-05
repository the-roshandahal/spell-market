from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import *
from adminpanel.models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.utils import timezone

# Create your views here.
def home(request):
    category = Category.objects.filter(status="active").order_by("order")[:4]
    fet_temp = Template.objects.filter(is_featured=1)

    partner = Partner.objects.all()
    testimonial = Testimonial.objects.all()
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 2)
    page = request.GET.get("page")
    blogs = paginator.get_page(page)
    if request.user.is_authenticated:
        cart_num = Cart.objects.filter(user=request.user).count()
        context = {
            "category": category,
            "fet_temp": fet_temp,
            "partner": partner,
            "testimonial": testimonial,
            "blogs": blogs,
            "cart_num": cart_num,
        }
        return render(request, "index.html", context)
    else:
        context = {
            "category": category,
            "fet_temp": fet_temp,
            "partner": partner,
            "testimonial": testimonial,
            "blogs": blogs,
        }
        return render(request, "index.html", context)


def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]

        password1 = request.POST["password1"]
        password = request.POST["password"]
        email = request.POST["email"]
        username = request.POST["username"]

        if password1 != password:
            messages.info(request, "passwords are different")
            return redirect("register")
        if User.objects.filter(username=username).exists():
            messages.info(request, "username taken")
            return redirect("register")
        if User.objects.filter(email=email).exists():
            messages.info(request, "email taken")
            return redirect("register")

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )

        auth_token = str(uuid.uuid4())
        profile_obj = Token.objects.create(user=user, auth_token=auth_token)
        profile_obj.save()

        subject = "Welcome to Spell Market. Please verify your account"
        message = f"Hi {user.username}, thank you for becoming a member. Please click the link below to verify yourself http://127.0.0.1:8000/success/{auth_token}"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [
            user.email,
        ]
        try:
            send_mail(subject, message, email_from, recipient_list)
            messages.info(request, "Please check your inbox to verify yourself.")
        except:
            messages.info(request, "Couldnot send mail")
            return redirect("home")
        return redirect("home")
    else:
        return render(request, "register.html")


def success(request, auth_token):
    try:
        profile_obj = Token.objects.filter(auth_token=auth_token).first()
        if profile_obj:
            if profile_obj.is_verified:
                messages.info(request, "Email address is already verified")
                return redirect("login")
            else:
                profile_obj.is_verified = True
                profile_obj.save()
                messages.info(request, "Congratulation your email has been verified")
                return redirect("login")
        else:
            messages.info(request, "Couldnot verify.")
            return redirect("home")

    except Exception as e:
        print(e)
        return redirect("home")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        user_obj = User.objects.filter(username=username).first()

        profile_obj = Token.objects.filter(user=user_obj).first()
        if user is None:
            messages.info(request, "Invalid credentials")
            return redirect("login")

        if user is not None and user.is_superuser:
            auth.login(request, user)
            messages.info(request, "Logged in successfully.")

            return redirect("dashboard")

        elif user is not None and not user.is_superuser:
            if profile_obj.is_verified:
                auth.login(request, user)
                messages.info(request, "Logged in successfully.")
                return redirect("home")
            else:
                messages.info(request, "Your are not verified")
                return redirect("login")
    else:
        return render(request, "login.html")
    return render(request, "login.html")


@login_required
def logout(request):
    django_logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect("home")


def theme(request):
    template = Template.objects.all()
    category = Category.objects.all()
    sub_category = SubCategory.objects.all()
    child_category = ChildCategory.objects.all()
    cart_num = Cart.objects.filter(user=request.user).count()
    context = {
        "template": template,
        "category": category,
        "sub_category": sub_category,
        "child_category": child_category,
        "cart_num": cart_num,
    }
    return render(request, "theme.html", context)


def theme_details(request, id):
    theme_data = Template.objects.get(id=id)
    cart_num = Cart.objects.filter(user=request.user).count()
    context = {"theme_data": theme_data, "cart_num": cart_num}
    return render(request, "theme_details.html", context)


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        contact = request.POST["contact"]
        message = request.POST["message"]
        Contact.objects.create(
            name=name, email=email, subject=subject, contact=contact, message=message
        )
        messages.info(request, "Thank you for your response.")

        return redirect("home")
    else:
        return render(request, "contact.html")


def about(request):

    return render(request, "about.html")


def categories(request):
    category = Category.objects.all()
    templates_ct = Template.objects.count()
    context = {
        "templates_ct": templates_ct,
        "category": category,
    }
    return render(request, "categories.html", context)


@login_required
def add_to_cart(request, id):
    if Cart.objects.filter(template=id, user=request.user).exists():
        messages.info(request, "This product is already in your cart")
        return redirect("cart")
    else:
        template = Template.objects.get(id=id)
        user = User.objects.get(username=request.user)
        cart = Cart(template=template, user=user)
        cart.save()
        messages.info(request, "Added to cart")
        return redirect("cart")


@login_required
def cart(request):
    carts = Cart.objects.filter(user=request.user)
    total = 0
    for cart in carts:
        template = Template.objects.get(template_name=cart.template)
        total += template.template_price
    fet_temp = Template.objects.filter(is_featured=1)
    context = {"carts": carts, "total": total, "fet_temp": fet_temp}
    return render(request, "cart.html", context)


def remove_from_cart(request, id):
    item = Cart.objects.get(template=id, user=request.user)
    item.delete()
    messages.info(request, "Removed from cart")
    return redirect(cart)


def checkout(request):
    carts = Cart.objects.filter(user=request.user)
    promo = None
    ghghgy = ""
    if request.method == "POST":
        code = request.POST["promo_code"]
        try:
            promo = PromoCode.objects.get(
                promo_code=code, expiry_date__gt=timezone.now()
            )
            ghghgy = promo.promo_code
        except:
            messages.info(request, "Invalid/Expired promo code")

    sub_total = 0
    for cart in carts:

        template = Template.objects.get(template_name=cart.template)
        sub_total += template.template_price

    discount_amt = 0
    if promo:
        if promo.discount_type == "percentage":
            discount_amt = (promo.discount * sub_total) / 100
        else:
            if promo.discount > sub_total:
                discount_amt = sub_total
            else:
                discount_amt = promo.discount
    total = sub_total - discount_amt
    tax_amt = 0.13 * total

    context = {
        "carts": carts,
        "sub_total": sub_total,
        "tax_amt": tax_amt,
        "grand_total": total + tax_amt,
        "total": total,
        "discount_amt": discount_amt,
        "promo_code": ghghgy,
    }

    return render(request, "checkout.html", context)


def blog(request):
    blog_data = Blog.objects.all()
    context = {
        "blog_data": blog_data,
    }
    return render(request, "blogs.html", context)


def blog_single(request, id):
    blogs = Blog.objects.all()
    blog_data = Blog.objects.get(id=id)
    context = {"blogs": blogs, "blog_data": blog_data}
    return render(request, "blog_single.html", context)


def page_not_found_view(request, exception):
    return render(request, "error404.html", status=404)
