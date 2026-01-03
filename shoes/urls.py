"""
URL configuration for shoes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from order.views import OrderListView, OrderDeleteView, OrderCreateView, OrderUpdateView
from product.views import ProductListView, ProductCreateView, ProductDeleteView, ProductUpdateView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path("accounts/", include("django.contrib.auth.urls")),
                  path('', login_required(ProductListView.as_view()), name='product_list'),
                  path('products/create/', login_required(ProductCreateView.as_view()), name='product_create'),
                  path('orders/', login_required(OrderListView.as_view()), name='order_list'),
                  path('orders/create/', login_required(OrderCreateView.as_view()), name='order_create'),
                  path('orders/<int:pk>/delete/', login_required(OrderDeleteView.as_view()), name='order_delete'),
                  path('products/<int:pk>/delete/', login_required(ProductDeleteView.as_view()), name='product_delete'),
                  path('products/<int:pk>/update/', login_required(ProductUpdateView.as_view()), name='product_update'),
                  path('orders/<int:pk>/update/', login_required(OrderUpdateView.as_view()), name='order_update'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
