from django.shortcuts import render
from .models import AboutUsInfo, ImageBlock


def about_us(request):
    info = AboutUsInfo.objects.last()
    seo = info.text[3:160]
    blocks = ImageBlock.objects.all()

    return render(request, 'about_us/about.html', {
        'info': info,
        'blocks': blocks,
        'seo': seo,
    })