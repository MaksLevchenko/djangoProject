import stripe
from django.views import View
from django.views.generic import TemplateView
from django.http import JsonResponse

from Django_Stripe_Api.models import Item
from djangoProject import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"


class ItemDetailView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        item = Item.objects.get(id=self.kwargs['pk'])
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context.update({
            'item': item,
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
        })
        return context


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        name = Item.objects.get(id=self.kwargs["pk"]).name
        description = Item.objects.get(id=self.kwargs["pk"]).description
        price = Item.objects.get(id=self.kwargs["pk"]).price
        domain = 'http://127.0.0.1:8000'
        session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'rub',
                        'unit_amount': price,
                        'product_data': {
                            'name': name,
                            'description': description,
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=domain + '/success/',
            cancel_url=domain + '/cansel/',
        )
        session_id = session['id']
        print(session_id)
        return JsonResponse(
            {
                'id': session_id
            }
        )
