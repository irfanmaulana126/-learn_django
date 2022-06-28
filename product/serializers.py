from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User

class ProductSerializers(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.email')

    class Meta:
        model = Product
        fields = ('name','price','creator')

class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model
    product = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = User
        fields = ('id', 'email', 'product')