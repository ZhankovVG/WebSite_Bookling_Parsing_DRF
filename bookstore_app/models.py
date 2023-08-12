from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200)  
    url = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Author(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Books(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Books_photo/%Y/%m/%d')
    code = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    draft = models.BooleanField(default=False)
    auhtor = models.ManyToManyField(Author, related_name='book_author')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def get_absolute_url(self):
        return reverse('detail_book', kwargs={'slug' : self.url})


class RatingsStar(models.Model):
    value = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'


class Reting(models.Model):
    ip = models.CharField('IP адресс', max_length=20)
    star = models.ForeignKey(RatingsStar, on_delete=models.CASCADE, verbose_name='звезда')
    book = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name='книга')

    def __str__(self):
        return f'{self.star} - {self.book}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True
    )
    book = models.ForeignKey(Books, verbose_name='Книги', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.book}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        