from django.urls import path
from . import views

urlpatterns = [
    path('', views.HowItWorks, name="How It Works"),
    path('GenerateLoanPaymentPlan/<int:Amount>/<int:Term>/<int:InterestRate>', views.GenerateLoanPaymentPlan),    
]
