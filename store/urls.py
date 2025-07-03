from django.urls import path

from .import views

urlpatterns = [
    #when store button is clicked this path will run
    path('', views.store, name='store'),

    # when user clicks on All categories and categories will appear then after choosing a particular category that slug
    # will go to the views.store
    path('<slug:category_slug>/', views.store, name='products_by_category'),

    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),

]