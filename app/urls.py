from django.conf.urls import url
from . import views

urlpatterns = [
    url('products', views.ProductListView.as_view()),
    url('api/product', views.ProductListCreate.as_view()),
]
