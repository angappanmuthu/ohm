from django.shortcuts import render
from datetime import datetime

now = datetime.now().strftime('%I:%H %p')

# Create your views here.
def ohm(request):
    dict_time = {"date" : now}
    return render(request,'test_app/index.html',dict_time)
