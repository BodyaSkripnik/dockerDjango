from django.db import models
from django.db.models.fields import TextField
from pytz import unicode

class films(models.Model):
    name_film = models.CharField('Название фильма',max_length=50)
    image_film = models.ImageField('Картинка',upload_to='media/')
    year_film = models.CharField('Год фильма',max_length=50)
    сategory_film = models.IntegerField('Категория')

    def __str__(self):
        return unicode(self.name_film)


class actors(models.Model):
    actor_name = models.CharField(max_length=200)
    actor_biography = TextField('Биография')
    actor_image = models.ImageField('Фото',upload_to='media/')
    сategory_actor = models.IntegerField('Категория')

    def __str__(self):
        return unicode(self.actor_name)

class category (models.Model):
    name_category = models.CharField('Имя категории',max_length=50)
    url_category = models.CharField("Url категория",max_length=50)
    id_category = models.AutoField(primary_key=True)

    def __str__(self):
        return unicode(self.name_category)