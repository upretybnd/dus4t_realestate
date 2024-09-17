from django.shortcuts import render, get_object_or_404

from category.models import Category
from listing.models import Post
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.
def listing(request, category_slug=None):
    categories = None
    posts = None
    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        posts = Post.objects.filter(category=categories, is_available=True)
        post_count = posts.count()
    else:
        posts = Post.objects.all().filter(is_available=True)
        paginator = Paginator(posts, 6)
        page = request.GET.get('page')
        paged_posts =paginator.get_page(page)
        post_count = posts.count()

    context = {
        'posts': paged_posts,
        'post_count': post_count,
    }
    return render(request, 'listing/listing.html', context)


def post_detail(request, category_slug, post_slug):
    try:
        single_post = Post.objects.get(category__slug=category_slug, slug=post_slug)
    except Exception as e:
        raise e

    related_posts = []
    try:
        # Attempt to fetch related posts based on category
        related_posts = Post.objects.filter(category=single_post.category).exclude(id=single_post.id)[:3]
    except Exception as e:
        # Log the exception or handle it as needed
        related_posts = []

    context = {
        'single_post': single_post,
        'related_posts': related_posts,
    }
    return render(request, 'listing/post_detail.html', context)
