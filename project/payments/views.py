from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import stripe
from django.views.generic.base import TemplateView 
from django.conf import settings
import psycopg2
from payment.models import StripeCharge
stripe.api_key = settings.STRIPE_SECRET_KEY

class HomePageView(TemplateView):
    template_name ='home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context 

def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='payment gate',
            source=request.POST['stripeToken'],
            )
        return render(request, 'charge.html')



def insert_data(request):
    try:
        # Creating a YourModel instance and saving it to insert data into the table
        payment = Payment(data_type='text', data_json={"tpye": "text", "data_json": "json"})
        payment.save()

        return HttpResponse("Data inserted into PostgreSQL successfully!")

    except Exception as e:
        # Handle exceptions
        return HttpResponse(f"Error: {str(e)}")
