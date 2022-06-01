from django.contrib.auth import get_user_model
from django.db import models
from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel

User = get_user_model()


class Category(TitleSlugDescriptionModel):
    """
    Category for a product.
    """

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Blog(TitleSlugDescriptionModel, TimeStampedModel):
    """
    Blog model.
    """

    content = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.title
