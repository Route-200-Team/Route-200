from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    # Auth
    path("auth/register/", views.RegisterView.as_view(), name="register"),
    path("auth/login/", views.LoginView.as_view(), name="login"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/profile/", views.ProfileView.as_view(), name="profile"),

    # Trips
    path("trips/", views.TripListCreateView.as_view(), name="trip-list"),
    path("trips/<int:pk>/", views.TripDetailView.as_view(), name="trip-detail"),

    # Saved Activities
    path("activities/", views.SavedActivityListCreateView.as_view(), name="activities"),
    path("activities/<int:pk>/", views.SavedActivityDetailView.as_view(), name="activity-detail"),

    # External APIs
    path("weather/", views.WeatherView.as_view(), name="weather"),
    path("flights/", views.FlightsView.as_view(), name="flights"),
]