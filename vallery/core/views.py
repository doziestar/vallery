from typing import Optional

from django.views.generic import DetailView, ListView, TemplateView

from vallery.core.models import Blog

"""
Pages:
1. Home
2. About
3. Contact
4. Blog
5. Blog Detail
6. Support
"""


class HomePage(TemplateView):
    template_name: str = "core/home.html"


class AboutPage(TemplateView):
    template_name: str = "core/about.html"


class ContactPage(TemplateView):
    template_name: str = "core/contact.html"


class BlogPage(ListView):
    model: Optional[type[Blog]] = Blog
    template_name: str = "core/blog.html"
    context_object_name: Optional[str] = "blogs"
    paginate_by: int = 10

    def get_queryset(self) -> Optional[type[Blog]]:
        return super().get_queryset().filter(is_published=True)


class BlogDetailPage(DetailView):
    model: Optional[type[Blog]] = Blog
    template_name: str = "core/blog_detail.html"
    context_object_name: Optional[str] = "blog"

    def get_queryset(self) -> Optional[type[Blog]]:
        return super().get_queryset().filter(is_published=True)


class SupportPage(TemplateView):
    template_name: str = "core/support.html"
