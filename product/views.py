from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView

from product.forms import ProductForm, SearchSortFilterForm
from product.models import Product


class ProductListView(ListView):
    model = Product

    def get_context_data(
        self, *, object_list = ..., **kwargs
    ):
        context = super(ProductListView, self).get_context_data(**kwargs)

        form = SearchSortFilterForm(self.request.GET)




        context['form'] = form
        return context


from django.views.generic.edit import CreateView, DeleteView


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("product_list")

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')  # главная страница после удаления


    # Против фреймворка. По умолчанию надо создать
    # order_confirm_delete.html.
    # Но это нарушает последовательный пользовательский интерфейс.
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())

from django.views.generic.edit import UpdateView


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name_suffix = "_form"
    success_url = reverse_lazy('product_list')