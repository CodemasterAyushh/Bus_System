from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("this is homepage")

from django.shortcuts import render

def my_view(request):
    # Your view logic here
    context = {
        'foo': 'bar',
    }
    return render(request, "index.html", context)

# from .models import BusFormModel

def fetch_bus_data(request):
    if request.method == 'POST':
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        date = request.POST.get('date')
        # matching_records = BusFormModel.objects.filter(source=source, destination=destination, date=date)
        # return render(request, 'bus/bus_data.html', {'records': matching_records})
    return render(request, 'bus/bus_form.html')

