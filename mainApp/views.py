from django.shortcuts import render

def index(request):
    return render (request, 'mainApp/homePage.html' )

def contact(request):
    return render (request, 'mainApp/basic.html', {'values': ['Если у Вас остались вопросы, то задавайте их по телефону', '(096) 256-25-25']})

