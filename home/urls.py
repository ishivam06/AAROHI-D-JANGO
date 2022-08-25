from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('ca/', views.caPage, name="ca"),
    path('coming_soon/', views.commingSoon, name="coming_soon"),
    path('team/', views.team, name="team"),
    path('previous_sponsors/', views.previous_spons, name="prev_spons"),
    path('gallery/', views.gallery, name="gallery"),
    path('social/', views.social, name="social"),
    path('booklet/', views.booklet, name="booklet"),
    path('testimonials/', views.testimonials, name="testimonial"),
    path('blogs/', views.blog),
    path('api/allimages', views.images_list),
    path('api/livestream', views.livestream_details),
    path('api/allimages/<int:pk>', views.image_details),
    path('aarohi-over-the-years/', views.aarohi_over_the_years, name="aarohi-over-the-years"),

    
]