
from django .shortcuts import render

from blogs.models import Blog, category
def home(request):
    categories = category.objects.all()
    featured_post = Blog.objects.filter(is_featured=True).order_by('updated_at')
    print(featured_post)
    context={
        'categories':categories,
        'featured_post':featured_post,
    }
    return render(request,'home.html',context)