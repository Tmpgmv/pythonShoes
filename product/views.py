from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q, ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from product.forms import ProductForm, SearchSortFilterForm
from product.models import Product


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        sort_by_stock = self.request.GET.get("stock", "more")
        search_phrase = self.request.GET.get("search", None)
        supplier_id = self.request.GET.get("supplier", None)

        queryset = Product.objects.all()
        if sort_by_stock == "more":
            queryset = queryset.order_by("-stock")
        else:
            queryset = queryset.order_by("stock")

        if supplier_id:
            queryset = queryset.filter(supplier_id=supplier_id)

        if search_phrase:
            queryset = queryset.filter(Q(sku__icontains=search_phrase) |
                                       Q(product_name__icontains=search_phrase) |
                                       Q(unit_of_measurement__icontains=search_phrase) |
                                       Q(product_category__icontains=search_phrase) |
                                       Q(description__icontains=search_phrase))

        return queryset

    def get_context_data(
            self, *, object_list=..., **kwargs
    ):
        context = super(ProductListView, self).get_context_data(**kwargs)

        form = SearchSortFilterForm(self.request.GET)
        context['form'] = form
        return context


from django.views.generic.edit import CreateView, DeleteView


class ProductCreateView(SuccessMessageMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("product_list")
    success_message = "Товар успешно добавлен."




class ProductDeleteView(SuccessMessageMixin,
                        DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')  # главная страница после удаления
    success_message = "Товар успешно удален."


    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            return response
        except ProtectedError:
            messages.error(request, "Товар, который присутствует в заказе, удалить нельзя.")
            return redirect(reverse("product_list"))



    class Meta:
        verbose_name_plural = 'Товары'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name_suffix = "_form"
    success_url = reverse_lazy('product_list')
