from django.http import Http404
from django.shortcuts import render, get_list_or_404, get_object_or_404

from product.models import Category, Product


def home_page(request):
    # SELECT * FROM product_category;
    categories = Category.objects.all()
                                        # ключ может быть любым
    return render(request, 'product/index.html', {'categories': categories})


# products/category
# def products_list(request, category_slug):
#     # product = Product.objects.all()
#
#     # Вариант 1
#     # if Category.objects.filter(slug=category_slug).exists():
#     #     raise Http404
#     # # SELECT * FROM product WHERE category_id = category_slug
#     # products = Product.objects.filter(category_id=category_slug)
#
#     # Вариант 2
#     products = get_list_or_404(Product, category_id=category_slug)
#
#     # Вариант 3
#     # category = get_object_or_404(Category, slug=category_slug)
#     # products = Product.objects.filter(category=category)
#
#     return render(request, 'product/products_list.html', {'products': products})



# products/?category=slug
# def product_list2(request):
#     category_slug = request.GET.get('category')
#     products = Product.objects.all()
#     if category_slug is not None:
#         products = products.filter(category_id=category_slug)
#     return render(request, '', {'products': products})

def products_list(request, category_slug):
    if not Category.objects.filter(slug=category_slug).exists():
        raise Http404('Нет такой категории')
    products = Product.objects.filter(category_id=category_slug)
    return render(request, 'product/products_list.html', {'products': products})

def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product/product_details.html', {'product': product})




#TODO: переписать вьюшку products_list +
#TODO: добавить детали продукта +
#TODO: сделать переход из категории в листинг продуктов +
#TODO: подключить картинки для товаров +
#TODO: переписать вьюшку на CBV Class Base Views


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


