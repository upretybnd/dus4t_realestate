from django.shortcuts import render

from listing.models import Post


def home(request):
    posts = Post.objects.all().filter(is_available=True).order_by('created_date')

    context = {
        'posts': posts,
    }
    return render(request, 'home.html', context)


def about_us(request):
    return render(request, 'about_us.html')


def contact(request):
    return render(request, 'contact.html')
