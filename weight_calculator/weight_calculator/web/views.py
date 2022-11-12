from django.shortcuts import render, redirect

VENUS = 0.91
MERCURY = 0.38
MARS = 0.38
JUPITER = 2.34
SATURN = 1.06
PLUTO = 0.06
THE_SUN = 27.01
MOON = 0.166
URANUS = 0.92
NEPTUNE = 1.19

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
                    gravity = VENUS
                elif planet == "Mercury":
                    gravity = MERCURY
                elif planet == "Mars":
                    gravity = MARS
                elif planet == "Jupiter":
                    gravity = JUPITER
                elif planet == "Saturn":
                    gravity = SATURN
                elif planet == "Pluto":
                    gravity = PLUTO
                elif planet == "The Sun":
                    gravity = THE_SUN
                elif planet == "Moon":
                    gravity = MOON
                elif planet == "Uranus":
                    gravity = URANUS
                elif planet == "Neptune":
                    gravity = NEPTUNE
                result = weight * gravity
    except:
        error_message = "Weight should be a number"

    context = {
        'planet': planet,
        'result': result,
        'error': error_message
    }

    return render(request, "home.html", context)
