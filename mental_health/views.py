from django.shortcuts import redirect,render
from django.http import HttpResponse
import pickle
import numpy as np
from django.contrib.auth.decorators import login_required
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

def home(request):
    return render(request,'main.html')

@login_required(login_url='/login/')
def testpage(request):
    return render(request,"form.html")

def contact(request):
    return render(request,'contact.html')

def result(request):
    val=request.POST.getlist('res')
    for x in range(len(val)):
        val[x]=int(val[x])
    final=[np.array(val)]
    # print(final)
    predictions = model.predict(final)[0]
    print(predictions)
    predictions=int(predictions)

    return render(request,"result.html",{"predictions":predictions})
    # return render(request,"result.html")
