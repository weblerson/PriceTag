from django.shortcuts import render, redirect
from django.http import HttpResponse

def homepage(request):
    if request.method == "GET":
        return render(request, 'homepage.html')

def hourcalc(request):
    if request.method == "GET":
        return render(request, 'hourcalc.html')
    elif request.method == "POST":
        salary = float(request.POST.get('salary'))
        hoursDay = float(request.POST.get('hoursDay'))
        monthDays = float(request.POST.get('monthDays'))

        hoursMonth = hoursDay*monthDays
        hourPrice = round(salary/hoursMonth, 2)

        return render(request, 'hourcalc.html', {'hourPrice': hourPrice})


def projectcalc(request):
    if request.method == "GET":
        return render(request, 'projectcalc.html')
    elif request.method == "POST":
        hourGain = float(request.POST.get('projectValue'))
        hourADay = float(request.POST.get('projectHour'))
        totalDays = float(request.POST.get('projectDays'))
        profit = float(request.POST.get('projectProfit'))

        totalHours = hourADay*totalDays
        value = hourGain*totalHours

        totalGainWithProfit = round(value + value*(profit/100), 2)
        
        return render(request, 'projectCalc.html', {'gain': totalGainWithProfit})