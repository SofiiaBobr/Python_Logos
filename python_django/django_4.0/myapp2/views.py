from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app2_home.html', {})

def main(request):
    return render(request, 'app2_main.html', {})