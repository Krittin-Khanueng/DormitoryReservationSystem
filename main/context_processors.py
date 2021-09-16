from blog.models import Blog
from dorm.models import Dormitory


def all_dormitory(self):
    dorms = Dormitory.objects.all().values("name")
    return dict(dorms=dorms)


def all_blog(self):
    blogs = Blog.objects.filter(is_deleted=False).order_by("-created_time")[:3]
    return dict(blogs=blogs)
