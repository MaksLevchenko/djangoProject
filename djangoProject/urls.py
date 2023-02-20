from django.contrib import admin
from django.urls import path

from Django_Stripe_Api import views

urlpatterns = [
    path('', views.ItemListView.as_view()),
    path('add-product/<int:pk>', views.AddInOrderView.as_view(), name='add_product'),
    path('admin/', admin.site.urls),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('cancel/', views.CancelView.as_view(), name='cancel'),
    path('item/<int:pk>', views.ItemDetailView.as_view(), name='item_detail'),
    path('basket/<int:pk>', views.OrderDetailView.as_view(), name='basket'),
    path('buy/<int:pk>', views.CreateCheckoutSessionView.as_view(), name='checkout'),
    path('buy-all/<int:pk>', views.CreateOderCheckoutSessionView.as_view(), name='bay-all')
]
