from django.db import models
from rest_framework import  serializers, viewsets
from rest_framework.routers import DefaultRouter


# Create your models here.


# модель
class Product(models.Model):
    articul = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    measures = models.TextField()
    price = models.IntegerField()
    supplier = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    discount = models.IntegerField()
    count = models.IntegerField()
    description = models.TextField()
    photo = models.CharField(max_length=100)


# Серилиализатор
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
# Вьюсет

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Роутер
router = DefaultRouter()
router.register('', ProductViewSet)
urlpatterns = router.urls