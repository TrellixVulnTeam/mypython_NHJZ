from django.shortcuts import render, get_object_or_404
from .models import BlogArticles

# Create your views here.
def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, 'blog/titles.html', {'blogs': blogs})

def blog_article(request, article_id):
    # article = BlogArticles.objects.get(id=article_id)
    # 处理article对象找不到的情况，即404
    article = get_object_or_404(BlogArticles, id=article_id)
    return render(request, 'blog/content.html', {'article': article})