from django.shortcuts import redirect
from django.urls import path
from ecommerceapp import views
app_name = 'ecommerceapp'



urlpatterns = [
    path('',views.allProdCat,name="allProdCat"),
    path('<slug:c_slug>/',views.allProdCat,name="products_by_category"),
    path('<slug:c_slug>/<slug:product_slug>/',views.ProdCatDetail,name="ProdCatDetail"),
]
