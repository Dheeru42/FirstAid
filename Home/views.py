from django.shortcuts import render
from django.http import JsonResponse
from bp import *
from diesese import *
import time

# Create your views here.
def index(request):
    return render(request,'index.html')

def model_form(request):
    if request.method == 'POST':
        die = request.POST.get('die')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        headache = request.POST.get('Headache')
        cough = request.POST.get('cough')
        fever = request.POST.get('fever')
        dizz = request.POST.get('dizz')
        blu_vis = request.POST.get('blu_vis')
        ches_pai = request.POST.get('ches_pai')
        fati = request.POST.get('fati')
        shor_brea = request.POST.get('shor_brea')
        diff_brea = request.POST.get('diff_brea')
        ireg_hertb = request.POST.get('ireg_hertb')
        sweat = request.POST.get('sweat')
        slp_pr = request.POST.get('slp_pr')
        swel_leg = request.POST.get('swel_leg')
        tinnit = request.POST.get('tinnit')
        duration = request.POST.get('duration')
        time.sleep(10)
        result = bpmodel(age,gender,headache,dizz,blu_vis,ches_pai,fati,shor_brea,ireg_hertb,sweat,slp_pr,swel_leg,tinnit)
        if result == 0:
            text = "Low Blood Pressure"
            bp = 'Low'
        elif result == 1:
            text = "Normal Blood Pressure"
            bp = 'Normal'
        else:
            text = "High Blood Pressure"
            bp = 'High'
            
            
        result1 = dies(die,fever,cough,fati,diff_brea,age,gender,bp)
        if result1 == 'Negative':
            text1 = f"You Don't Have {die}"
        else:
            text1 = f"You Have {die} ,Take An Medical Help"   
            
        # Sample response - should be mapped to real predictions
        response = {
            "condition": text,
            "description": text1,
            "prescription": {
                "medications": ["Sample Medicine 1", "Sample Medicine 2"],
                "recommendations": ["Drink fluids", "Get rest"],
                "warning": "See a doctor if condition worsens."
            }
        }

        return JsonResponse(response)
