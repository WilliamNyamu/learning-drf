from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Gift, Merchandise
from .serializers import GiftSerializer, MerchandiseSerializer
# Create your views here.

def index(request):
    return HttpResponse("<h2>Shop Sanity Checks</h2>")

class GiftAPIView(viewsets.ModelViewSet):
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
    
