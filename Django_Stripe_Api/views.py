import stripe
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView, ListView
from django.http import JsonResponse

from Django_Stripe_Api.models import Item, Order
from djangoProject import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    """Благодарность"""
    template_name = "success.html"


class CancelView(TemplateView):
    """Отмена"""
    template_name = "cancel.html"


class ItemListView(ListView):
    """Список элементов"""
    template_name = 'index.html'
    model = Item
    queryset = Item.objects.all()


class ItemDetailView(TemplateView):
    """Страница элемента"""
    template_name = 'item_detail.html'

    def get_context_data(self, **kwargs):
        item = Item.objects.get(id=self.kwargs['pk'])
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context.update({
            'item': item,
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
        })
        return context


class CreateCheckoutSessionView(View):
    """Оформление заказа"""

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
        return JsonResponse(
            {
                'id': session_id
            }
        )


class OrderDetailView(TemplateView):
    """Оформление заказа одного элемента"""
    template_name = 'order_list.html'

    def get_context_data(self, **kwargs):
        order = Order.objects.get(id=self.kwargs['pk'])
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        context.update({
            'order': order,
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
        })
        return context


class CreateOderCheckoutSessionView(View):
    """Сессия заказа"""
    coupon = stripe.Coupon.create(percent_off=20, duration="once")

    def post(self, request, *args, **kwargs):
        price = int(Order.objects.get(id=self.kwargs["pk"]).get_all_product_price()[:-3]) * 100
        domain = 'http://127.0.0.1:8000'
        session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'rub',
                        'unit_amount': price,
                        'product_data': {
                            'name': 'all product',
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            discounts=[{
                'coupon': self.coupon.id,
            }],
            # allow_promotion_codes=True,
            success_url=domain + '/success/',
            cancel_url=domain + '/cansel/',
        )
        session_id = session['id']
        return JsonResponse(
            {
                'id': session_id
            }
        )


class AddInOrderView(View):
    """Добавление в корзину"""

    def post(self, request, pk):
        item = Item.objects.get(id=pk)
        order = Order(id=self.request.user.id, username=self.request.user)
        order.save()
        order.product.add(str(item.id))

        return redirect("/")
