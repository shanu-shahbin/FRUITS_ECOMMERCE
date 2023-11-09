from django.urls import path, include
from. import views
app_name = 'shop'

urlpatterns = [
    path('', views.allprodCat, name='allprodCat'),
    path('<slug:c_slug>/', views.allprodCat, name='product_by_category'),

    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('login', views.login_view, name='login'),
    path('sign', views.signup, name='sign'),

]
