from .serializer import Authorise, User
from rest_framework.viewsets import ModelViewSet

class AuthoriseView(ModelViewSet):
    serializer_class = Authorise
    queryset = User.objects.all()
