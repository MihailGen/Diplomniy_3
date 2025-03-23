from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название фильма')
    director = models.CharField(max_length=100, verbose_name='Директор фильма')
    release_date = models.DateField(null=True, blank=True, verbose_name='Дата выхода на экран')
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
    def __str__(self):
        return self.title


class Film_details(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='Информация')
    tags = models.ManyToManyField('Tag', related_name='task')
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
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='Жанры')
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
    ]
    genre = models.CharField(max_length=200, choices=GENRE_CHOICES, default='Художественный')
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
    def __str__(self):
        #return ("Фильм: " + str(self.film))
        return f'Фильм: {self.film}'


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название тега')

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self):
        return self.name



"""

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория задачи')
    color = models.CharField(max_length=50, verbose_name='Цвет отметки задачи')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=150, verbose_name='Тема задачи')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    due_date = models.DateTimeField(null=True, blank=True, verbose_name='Cроки выполнения')
    author = models.CharField(max_length=50, null=True, blank=True, verbose_name='Автор')
    tags = models.ManyToManyField('Tag', related_name='task')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='task', null=True, blank=True)

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'

    def __str__(self):
        return self.name


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.id}, "{self.text}", on {self.created_at}'


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название тега')

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self):
        return self.name

"""