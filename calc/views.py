from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html",{})

def results(request):
    # if request.method == 'POST':
        number1 = int(request.POST['number1'])
        number2 = int(request.POST['number2'])

        if 'add' in request.POST:
            result = number1 + number2
        elif 'subtract' in request.POST:
            result = number1 - number2
        elif  'multipilcation' in request.POST:
            result = number1 * number2
        elif 'division' in request.POST:
            result = number1 / number2
        return render(request,"result.html",{'result':result})




