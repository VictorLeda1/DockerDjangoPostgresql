from rest_framework import filters, generics, viewsets
from .models import User
from .serializers import UserSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = None