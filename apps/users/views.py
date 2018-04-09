from django.shortcuts import render
from django.contrib.auth import authenticate, login


# 6.2  13:18
def login1(request):
    if request.method == "POST":
        user_name = request.POST.get("username", "")
        pass_word = request.POST.get("password", "")
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            return render(request, "index.html")
        else:
            return render(request, "login.html", {})
    elif request.method == "GET":
        return render(request, "login.html", {})

