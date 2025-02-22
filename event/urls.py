from django.urls import path
from .views import RegistrationCreateView, RegistrationListView
from django.views.generic import TemplateView

urlpatterns = [
    path('register/', RegistrationCreateView.as_view(), name='register'),
    path('registrations/', RegistrationListView.as_view(), name='registrations_list'),
    path('success/', TemplateView.as_view(template_name='events/success.html'), name='registration_success'),
]
