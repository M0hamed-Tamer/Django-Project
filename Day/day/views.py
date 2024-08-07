from django.shortcuts import render

# Create your views here.



def index(request):
    return render(request, 'day/index.html')
    
    
    
    
def portfolio(request):
    return render(request, 'day/portfolio-details.html')   