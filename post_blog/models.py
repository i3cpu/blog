from django.db import models


class Post(models.Model):
    categories = models.ForeignKey('Categories', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=267,verbose_name='Title')
    text = models.TextField(verbose_name='Text')
    created_date = models.DateField(blank=False)
    published_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.title}'

class Comments(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)

    text = models.TextField(max_length=200, verbose_name='Message')
    published_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.text}'

class Categories(models.Model):
    text = models.CharField(verbose_name='category:', max_length=200)
    def __str__(self) -> str:
        return f'{self.text}'

class Feedback(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    
    text = models.TextField(max_length=150, verbose_name="Text")
    def __str__(self) -> str:
        return f'{self.text}'
