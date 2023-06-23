from django.shortcuts import render,redirect
from .models import Form


def index(request):
    return render(request, 'index.html')



def convert(request):
    if request.method != 'POST':
        return redirect('index')

#Pobieranie danych z formularza
    num = request.POST['number']
    jedn = request.POST['jednostka']

    dane = Form(num,jedn)
    dict ={"metr":"m","kilometr":"km","decymetr":"dm","centymetr":"cm","milimetr":"mm","mila":"mi",}
    miara_skrot = dict[dane.miara]
    liczba = float(dane.wartosc)
#liczenie, konwertowanie

    if miara_skrot == 'm':
        m = liczba*1
        km = liczba/1000
        dm = liczba*10
        cm = liczba*100
        mm = liczba*1000
        mi = liczba*0.0006215

    elif miara_skrot == 'km':
        m = liczba * 1000
        km = liczba * 1
        dm = liczba * 10000
        cm = liczba * 100000
        mm = liczba * 1000000
        mi = liczba * 0.6215

    elif miara_skrot == 'dm':
        m = liczba * 0.1
        km = liczba * 0.0001
        dm = liczba * 1
        cm = liczba * 10
        mm = liczba * 100
        mi = liczba * 0.00006215

    elif miara_skrot == 'cm':
        m = liczba * 0.01
        km = liczba * 0.00001
        dm = liczba * 0.1
        cm = liczba * 1
        mm = liczba * 10
        mi = liczba * 0.000006215

    elif miara_skrot == 'mm':
        m = liczba * 0.001
        km = liczba * 0.000001
        dm = liczba * 0.01
        cm = liczba * 0.11
        mm = liczba * 1
        mi = liczba * 0.0000006215

    elif miara_skrot == 'mi':
        m = liczba * 1609.344
        km = liczba * 1.609344
        dm = liczba * 16093.44
        cm = liczba * 160934.4
        mm = liczba * 1609344
        mi = liczba * 1

#wyświetlenie danych
    return render(request, 'convert.html', {'num': dane.wartosc,'jedn': miara_skrot,'m':m,'km':km,'dm':dm,'cm':cm,'mm':mm,'mi':mi})











