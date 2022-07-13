from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from .models import Prediction_Results


def bmi(request):
    return render(request, 'bmi.html')

def calculator(request):
    height = float(request.POST.get('height'))
    weight = float(request.POST.get('weight'))
    bmi = round(weight/((height/100)**2), 2)
    if bmi < 18.5:
        condition = 'Underweight'
        s1 = 'Eat more often'
        s2 = 'Drink Milk'
        s3 = 'Try Weight gainer shakes'
        s4 = 'Use Bigger Plates'
        s5 = 'Add cream to your coffee'
    if (bmi > 18.5) and (bmi < 24.9):
        condition = 'Normal'
        s1 = 'Eat healthy food'
        s2 = 'Do not eat junk food'
        s3 = 'Your meal should contain all the essential nutrients'
        s4 = 'Minimize the intake of alcohol'
        s5 = 'Do regular exercise'
    if bmi > 25:
        condition = 'Overweight'
        s1 = 'Eat Whole grains (whole wheat, steel cut oats, brown rice, quinoa)'
        s2 = 'Eat Vegetables (a colorful variety-not potatoes)'
        s3 = 'Eat Whole fruits (not fruit juices)'
        s4 = 'Eat Nuts, seeds, beans, and other healthful sources of protein (fish and poultry)'
        s5 = 'Eat Plant oils (olive and other vegetable oils)'
    return render(request, 'calculator.html', {'bmi':bmi, 'condition':condition,
           's1':s1, 's2':s2, 's3':s3, 's4':s4, 's5':s5})

def about(request):
    return render(request, 'about.html')

def predict(request):
    return render(request, 'prediction.html')

def predict_chances(request):

    if request.POST.get('action') == 'post':

        
        age = float(request.POST.get('age'))
        sex = float(request.POST.get('sex'))
        bmi = float(request.POST.get('bmi'))
        children = float(request.POST.get('children'))
        smooker = float(request.POST.get('smooker'))

        
        model = pd.read_pickle(r"C:\Users\monster\Desktop\insurance\model.pickle")
       
        result = model.predict([[age, sex, bmi, children, smooker]])

        regression = result[0]

        Prediction_Results.objects.create(age=age, sex=sex, bmi=bmi,children=children, smooker=smooker, regression=regression)

        return JsonResponse({'result': regression, 'age': age,'sex': sex, 'bmi': bmi, 'children': children, 'smooker': smooker},safe=False)

def view_results(request):

    data = {"dataset": Prediction_Results.objects.all()}
    return render(request, "results.html", data)