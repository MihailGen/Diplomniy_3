from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название фильма', db_index=True)
    director = models.CharField(max_length=100, verbose_name='Директор фильма')
    release_date = models.DateField(null=True, blank=True, verbose_name='Дата выхода на экран')
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
    def __str__(self):
        return self.title


class Film_details(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='Информация', db_index=True)
    tags = models.ManyToManyField('Tags', related_name='Film_details')
    year = models.DateField(null=True, blank=True, verbose_name='Год выхода на экран')
    runtime = models.IntegerField(null=True, blank=True, verbose_name='Длительность (мин.)')
    writer = models.CharField(max_length=100, verbose_name='Сценарист')
    actors = models.CharField(max_length=100, verbose_name='Актёры')
    plot = models.TextField(verbose_name='Сюжет')
    language = models.CharField(max_length=100, verbose_name='Язык')
    country = models.CharField(max_length=100, verbose_name='Страна')
    awards = models.CharField(max_length=100, verbose_name='Призы и награды')
    poster = models.CharField(max_length=100, verbose_name='Ссылка на картинку')
    box_office = models.IntegerField(verbose_name='Бюджет')
    class Meta:
        verbose_name = 'информация о фильме'
        verbose_name_plural = 'информация о фильмах'

    def __str__(self):
        return ("Фильм: " + str(self.film))


class Genre(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='Жанры', db_index=True)
    GENRE_CHOICES = [
        ('драма', 'Драма'),
        ('комедия', 'Комедия'),
        ('мелодрама', 'Мелодрама'),
        ('исторический', 'Исторический'),
        ('детектив', 'Детектив'),
        ('криминал', 'Криминал'),
        ('боевик', 'Боевик'),
        ('ужасы', 'Ужасы'),
        ('мюзикл', 'Мюзикл'),
        ('художественный', 'Художественный'),
        ('экшн', 'Экшн'),
    ]
    genre = models.CharField(max_length=200, choices=GENRE_CHOICES, default='Художественный')
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
    def __str__(self):
        #return ("Фильм: " + str(self.film))
        return f'Фильм: {self.film}'


class Tags(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название тега')

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self):
        return self.name
