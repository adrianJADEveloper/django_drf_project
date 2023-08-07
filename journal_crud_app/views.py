from django.shortcuts import render
from django.http import HttpResponse
from .models import Journal
from .serializers import JournalSerializer
from rest_framework import generics

# Create your views here.


class JournalListView(generics.ListCreateAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer


class SingleJournalView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
