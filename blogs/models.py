from django.db import models


class AuthorModel(models.Model):
    name = models.CharField(max_length=128)
    imge = models.ImageField(upload_to='blog-authors')
    about = models.TextField()
    position = models.CharField(max_length=128)
    profession = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'


class BlogCategoryModel(models.Model):
    name = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class BlogModel(models.Model):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to='blog-images')
    content = models.TextField()
    categories = models.ManyToManyField(BlogCategoryModel, related_name='blogs')
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE, related_name='blogs')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'

