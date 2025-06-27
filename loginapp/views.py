from django.contrib.auth import authenticate
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_view(request):
    if request.method == 'GET':
        return HttpResponse("""
            <h2>Login</h2>
            <form method="post">
                Usuario: <input type="text" name="username"><br><br>
                Contraseña: <input type="password" name="password"><br><br>
                <input type="submit" value="Ingresar">
            </form>
        """)
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            return HttpResponse("¡Login correcto!")
        else:
            return HttpResponse("Login fallido", status=401)
    else:
        return JsonResponse({'status': 'fail', 'message': 'Solo se permiten solicitudes GET y POST'}, status=405)
