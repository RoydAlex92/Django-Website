from django.urls import path, include
from product import views




urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view()),
    path('latest-sports/', views.SportsProductsList.as_view()),
    path('latest-casual/', views.CasualProductsList.as_view()),
    path('latest-business/', views.BusinessProductsList.as_view()),
    path('latest-boots/', views.BootProductsList.as_view()),
    path('products/search/', views.search),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
    path('discountcode/', views.DiscountDetail.as_view()),
]