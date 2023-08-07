from django.urls import path
from . import views

urlpatterns = [
    path('journals', views.JournalListView.as_view(), name='journal-list'),
    path('journal-item/<int:pk>', views.SingleJournalView.as_view(),
         name='journal-item-view'),
]
