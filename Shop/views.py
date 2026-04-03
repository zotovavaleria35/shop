from django.shortcuts import render

# Функція для головної сторінки
def index(request):
    context = {
        'title': 'Головна Shop',
        'content': 'Ласкаво просимо до нашого магазину!',
        'is_main': True
    }
    return render(request, 'shop_page.html', context)

# Функція для сторінки "Про нас" (це та, якої зараз не вистачає)
def about(request):
    context = {
        'title': 'Про нас',
        'content': 'Ми найкращий магазин автозапчастин у Луцьку.',
        'is_main': False
    }
    return render(request, 'shop_page.html', context)