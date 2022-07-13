from django.urls import path
from . import views

app_name = "predict"

urlpatterns = [
    path('', views.predict, name='prediction_page'),
    path('prediction/', views.predict_chances, name='submit_prediction'),
    path('results/', views.view_results, name='results'),
    path('about/', views.about, name='about'),
    path('bmi/', views.bmi, name='bmi'),
    path('calculator/', views.calculator, name='calculator'),
]