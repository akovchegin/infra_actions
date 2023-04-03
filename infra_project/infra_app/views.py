from django.http import HttpResponse


def index(request):
    return HttpResponse(
        'Есть три вещи, на которые можно смотреть бесконечно: '
        'огонь, вода и эта страница!'
    )


def second_page(request):
    return HttpResponse('А это вторая страница!')
