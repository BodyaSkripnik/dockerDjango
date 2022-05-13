from rest_framework import  serializers
from .models import films,actors,category


class FilmsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = films
        fields = ("name_film", "image_film", "year_film",'сategory_film')


class ActorsSerializer(serializers.ModelSerializer):
    class Meta:
        model  = actors
        fields = ("actor_name", "actor_biography", "actor_image",'сategory_actor')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model  = category
        fields = ("name_category", "url_category",'id_category')