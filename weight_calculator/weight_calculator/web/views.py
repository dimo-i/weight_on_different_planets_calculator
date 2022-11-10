from django.shortcuts import render, redirect

def index(request):
    return redirect('calculator')

def calculate(request):
    result = ''
    error_message = None
    planet = ''
    try:
        if request.method == "POST":
            weight = request.POST.get('weight')
            planet = request.POST.get('planet')
            if type(int(weight)) == int:
                weight = int(weight)
                if planet == "Venus":
                    gravity = 0.91
                elif planet == "Mercury":
                    gravity = 0.38
                elif planet == "Mars":
                    gravity = 0.38
                elif planet == "Jupiter":
                    gravity = 2.34
                elif planet == "Saturn":
                    gravity = 1.06
                elif planet == "Pluto":
                    gravity = 0.06
                elif planet == "The Sun":
                    gravity = 27.01
                elif planet == "Moon":
                    gravity = 0.166
                elif planet == "Uranus":
                    gravity = 0.92
                elif planet == "Neptune":
                    gravity = 1.19
                result = weight * gravity
    except:
        error_message = "Weight should be a number"

    context = {
        'planet': planet,
        'result': result,
        'error': error_message
    }

    return render(request, "home.html", context)
