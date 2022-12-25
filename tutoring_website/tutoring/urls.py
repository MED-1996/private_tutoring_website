from django.urls import path
from . import views

app_name = 'tutoring'

urlpatterns = [
    path('', views.client_form, name='client_form'),
    path('testimonials/', views.TestimonialView.as_view(), name='testimonials'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('pricing/', views.PricingView.as_view(), name='pricing'),
    path('client_created/', views.ClientCreationView.as_view(), name='client_created'),
]
