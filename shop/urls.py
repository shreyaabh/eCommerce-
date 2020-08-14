from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="ContactUs"),
    path('tracker/', views.tracking, name="TrackingStatus"),
    path('search/', views.search, name="Search"),
    path('productview/<int:id>', views.product, name="Product"),
    path('checkout/', views.checkout, name="Checkout"),
]