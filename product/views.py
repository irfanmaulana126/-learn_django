from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Product
from .serializers import ProductSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

# Create your views here.
class ProductCreateAPIView(ListCreateAPIView):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Assign the user who created the product
        serializer.save(creator=self.request.user)

class RetrieveUpdateDestroyProductAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
