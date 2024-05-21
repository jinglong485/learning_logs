"""defines URL patterns for accounts."""
from django.urls import path, include
from . import views

app_name = "accounts"
urlpatterns = [
	# Include default autho urls.
	path("", include("django.contrib.auth.urls")),
	# Registration page.
	path('register/', views.register, name='register'),
]