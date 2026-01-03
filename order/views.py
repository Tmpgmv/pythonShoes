from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.edit import CreateView

from django.urls import reverse_lazy

from order.forms import OrderForm
from order.models import Order


class OrderListView(ListView):
    model = Order


class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('order_list')  # главная страница после удаления
    #
    # # Против фреймворка. По умолчанию надо создать
    # # order_confirm_delete.html.
    # # Но это нарушает последовательный пользовательский интерфейс.
    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     self.object.delete()
    #     return HttpResponseRedirect(self.get_success_url())


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy("order_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name_suffix = "_form"
    success_url = reverse_lazy('order_list')
