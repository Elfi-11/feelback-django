from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "quiz/index.html")

def feedbackForm(request):
    return render(request, "quiz/feedback-form.html")

def dashboard(request):
    return render(request, "quiz/dashboard.html")