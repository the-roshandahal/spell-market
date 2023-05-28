from django.urls import path
from . import views
from django.urls import re_path
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("success/<auth_token>", views.success, name="success"),
    path("logout/", views.logout, name="logout"),
    path("theme/", views.theme, name="theme"),
    path("contact/", views.contact, name="contact"),
    path("themedetails/<int:id>", views.themedetails, name="themedetails"),
    path("categories/", views.categories, name="categories"),
    path("add_to_cart/<int:id>", views.add_to_cart, name="add_to_cart"),
    path("cart/", views.cart, name="cart"),
    path("remove_from_cart/<int:id>", views.remove_from_cart, name="remove_from_cart"),
    # path("khalti-request/", views.KhaltiRequestView, name="khaltirequest"),
    path("khalti-verify/", views.KhaltiVerifyView.as_view(), name="khaltiverify"),
    path("blog/", views.blog, name="blog"),
    path("blogdetails/<int:id>", views.blogdetails, name="blogdetails"),
    path("about/", views.about, name="about"),
    path("checkout/", views.checkout, name="checkout"),

    # path("search/", views.search, name="search"),
    path("purchasesummary/", views.purchasesummary, name="purchasesummary"),
    path(
        "purchase_details/<int:id>",
        views.purchase_details,
        name="purchase_details",
    ),
    path("purchasedtemplates/", views.purchasedtemplates, name="purchasedtemplates"),
    path(
        "download_count/<int:id>/<int:di>", views.download_count, name="download_count"
    ),
    path("comment/<int:id>", views.comment, name="comment"),
    
    
    
    
    
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
