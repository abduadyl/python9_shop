from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import Http404
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View

from product.forms import CreateProductForm, UpdateProductForm, ImagesFormSet
from product.models import Category, Product, ProductImage

class HomePageView(ListView):
    model = Category
    template_name = 'product/index.html'
    context_object_name = 'categories'


class ProductsListView(ListView):
    model = Product
    template_name = 'product/products_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_slug = self.kwargs.get('category_slug')
        if not Category.objects.filter(slug=category_slug).exists():
            raise Http404('Нет такой категории')
        queryset = queryset.filter(category_id=category_slug)
        return queryset


class ProductDetailsView(DetailView):
    model = Product
    template_name = 'product/product_details.html'


class IsAdminCheckMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and\
               (self.request.user.is_staff or self.request.user.is_superuser)


class ProductCreateView(IsAdminCheckMixin, View):
    def get(self, request):
        form = CreateProductForm()
        formset = ImagesFormSet(queryset=ProductImage.objects.none())
        return render(request, 'product/create.html', locals())

    def post(self, request):
        form = CreateProductForm(request.POST)
        formset = ImagesFormSet(request.POST,
                                request.FILES,
                                queryset=ProductImage.objects.none())

        if form.is_valid() and formset.is_valid():
            product = form.save()
            for form in formset.cleaned_data:
                image = form.get('image')
                if image is not None:
                    pic = ProductImage(product=product, image=image)
                    pic.save()
            return redirect(product.get_absolute_url())
        print(form.errors, formset.errors)


# products/edit/<int:pk>
# Product.objects.get(pk=pk)
class ProductEditView(IsAdminCheckMixin, View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = CreateProductForm(instance=product)
        formset = ImagesFormSet(queryset=product.images.all())
        return render(request, 'product/edit.html', locals())

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = CreateProductForm(instance=product, data=request.POST)
        formset = ImagesFormSet(request.POST,
                                request.FILES,
                                queryset=product.images.all())

        if form.is_valid() and formset.is_valid():
            product = form.save()
            for form in formset.cleaned_data:
                image = form.get('image')
                if not None and not ProductImage.objects.filter(product=product, image=image).exists():
                    pic = ProductImage(product=product, image=image)
                    pic.save()
            for form in formset.deleted_forms:
                image = form.cleaned_data.get('id')
                if image is not None:
                    image.delete()
            return redirect(product.get_absolute_url())
        print(form.errors, formset.errors)


class ProductDeleteView(IsAdminCheckMixin, DeleteView):
    model = Product
    template_name = 'product/delete.html'
    success_url = reverse_lazy('index-page')












#TODO: переписать вьюшку products_list +
#TODO: добавить детали продукта +
#TODO: сделать переход из категории в листинг продуктов +
#TODO: подключить картинки для товаров +
#TODO: переписать вьюшку на CBV Class Base Views +


# all() - выводит все объекты модели
# SELECT * FROM table_name;
# Category.objects.filter(...).all()

# filter() - фильтрует результаты QuerySet
# SELECT * FROM table_name WHERE ...;

# exclude(category_id=1) - исключает из результатов объекты отвечающие условию
# SELECT * FROM table_name WHERE category != 1;

# order_by() - сортировка результатов запроса
# Product.objects.order_by('price')
# SELECT * FROM product ORDER BY price ASC;
# Product.objects.order_by('-price')
# SELECT * FROM product ORDER BY price DESC;
# Product.objects.order_by('price', 'popularity')
# SELECT * FROM product ORDER BY price, popularity ASC;
# Product.objects.order_by('?') - рандомная сортировка

# reverse() - переворачивает список
# Product.objects.reverse()

# distinct() - возвращает уникальные значения
# Product.objects.values_list('category', flat=True) flat=True делает списком а без он в кортеже
# ['frukty', 'frukty', 'milk', 'myaso', 'milk']
# Product.objects.values_list('category', flat=True).distinct()
# ['frukty', 'milk', 'myaso']

# values()
# Product.objects.values() ->
# <Queryset: [{'id': 1, 'title': 'Молоко', 'description': ...}, ...]
# Product.objects.values('id', 'title') ->
# <Queryset: [{'id': 1, 'title': 'Молоко'}, ...]>

# values_list()
# Product.objects.values_list() ->
# <Queryset: [(1, 'Молоко', ...), ...]>
# Product.objects.values_list('id', 'title') ->
# <Queryset: [('id': 1, 'title': 'Молоко'), ...]>

# select_related()
# # делает запрос 2 раза
# prod = Product.objects.get(id=1)
# prod.category # запрос в БД
#
# # делает запрос 1 раз
# prod = Product.objects.select_related('category').get(id=1)
# prod.category # запроса нет

# prefetch_related()


