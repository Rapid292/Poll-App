from django.urls import path, include
from django.views.generic.base import TemplateView

from . import views
app_name = 'polls'
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('index/', views.IndexView.as_view(), name="index"),
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    path('<int:pk>/result/', views.ResultsView.as_view(), name="result"),
    path('<int:question_id>/vote/', views.vote, name="vote"),

]