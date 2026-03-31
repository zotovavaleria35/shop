from django.shortcuts import render


def index(request):
    context = {
        'title': 'Головна сторінка',
        'content': 'Це контент головної сторінки. Використовуйте навігацію нижче.',
        'show_link_to_other': True
    }
    return render(request, 'main/base.html', context)


def second_page(request):
    context = {
        'title': 'Друга сторінка',
        'content': 'Ви перейшли на іншу сторінку! Тут свій унікальний текст.',
        'show_link_to_other': False
    }
    return render(request, 'main/base.html', context)


from django.shortcuts import render

# Create your views here.
