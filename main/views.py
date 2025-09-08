from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'I Gusti Ngurah Agung Airlangga Putra',
        'npm': '2406358794',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)