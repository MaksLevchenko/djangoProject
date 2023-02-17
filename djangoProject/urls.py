from django.contrib import admin
from django.urls import path

from Django_Stripe_Api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('success/', views.SuccessView.as_view, name='success'),
    path('cancel/', views.CancelView.as_view, name='cancel'),
    path('item/<int:pk>', views.ItemDetailView.as_view(), name='item_detail'),
    path('buy/<int:pk>', views.CreateCheckoutSessionView.as_view(), name='checkout')
]
