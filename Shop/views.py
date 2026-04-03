from django.shortcuts import render

def index(request):
    context = {
        'title': 'Головна сторінка',
        'content': 'Ласкаво просимо до нашого магазину!',
        'is_main': True
    }
    return render(request, 'shop_page.html', context)

def about(request):
    context = {
        'title': 'Про нас',
        'content': 'Ми найкращий магазин автозапчастин у Луцьку.',
        'is_main': False
    }
    return render(request, 'shop_page.html', context)