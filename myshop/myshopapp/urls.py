from . import views
from django.urls import path
app_name='myshopapp'
urlpatterns = [
    path('',views.prodcat,name='prodcat'),
    path('<slug:c_slug>/',views.prodcat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.productDetail, name='productDetail')
]