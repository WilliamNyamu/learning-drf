from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Gift, Merchandise
from .serializers import GiftSerializer, MerchandiseSerializer
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SessionAndTokenLoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # create session (so browsable API works)
            login(request, user)

            # get or create token
            token, _ = Token.objects.get_or_create(user=user)

            return Response({
                "message": "Login successful",
                "user": user.username,
                "token": token.key
            })
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

def index(request):
    return HttpResponse("<h2>Shop Sanity Checks</h2>")

class GiftAPIView(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Gift.objects.all()
    serializer_class = GiftSerializer

    def get_queryset(self):
        queryset = Gift.objects.all()
        name_filter = self.request.query_params.get('name', None)
        presenter_name_filter = self.request.query_params.get('presenter_name', None)
        if name_filter is not None:
            queryset = queryset.filter(name__icontains = name_filter)
        if presenter_name_filter is not None:
            # If you want to filter objects by the presenter’s name(which is a foreign key field), you use presenter__name__icontains
            queryset = queryset.filter(presenter__name__icontains = presenter_name_filter)
        
        return queryset

class MerchandiseAPIView(viewsets.ModelViewSet):
    queryset = Merchandise.objects.all()
    serializer_class = MerchandiseSerializer
    
