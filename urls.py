from django.urls import path
from . import views 
urlpatterns = [
   path("contactus", views.contact_page, name="contactus"),
   path("success", views.success, name="success")
]
