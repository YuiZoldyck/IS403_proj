from django.urls import include, path
from .views import indexPageView, viewPageView, createPageView, editPageView, deletePageView, submitChanges, addRecordView, reorderTable

urlpatterns = [
    path('', indexPageView, name="index"),
    path('view/', viewPageView, name="view"),
    path('create/', createPageView, name="create"),
    path('edit/<int:sid>', editPageView , name='edit'),
    path('addrecord/', addRecordView, name="add"),
    path('submitchanges/<int:sid>', submitChanges, name='submit'),
    path('delete/<int:sid>', deletePageView, name='delete'),
    path('reorder/', reorderTable, name='reorder'),
]
