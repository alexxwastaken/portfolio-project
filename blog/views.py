from django.shortcuts import render, get_object_or_404
from .models import Blog, User
from django.db.models import Q


def allblogs(request):
    blogs = Blog.objects

    def get_ip(request):
        address = request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    ip = get_ip(request)
    u = User(user=ip)
    print(ip)
    result = User.objects.filter(Q(user__icontains=ip))
    if len(result) >= 1:
        print("User exists")
    else:
        u.save()
        print("User is unique")
    count = User.objects.all().count()
    print("Total user count is ", count)
    return render(request, 'blog/allblogs.html', {'blogs': blogs, 'count': count})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
