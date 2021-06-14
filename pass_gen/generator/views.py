from django.shortcuts import render
import random

# Create your views here.
def genpass(request):
    return render(request, 'generator/pass.html')

def finalpage(request):
    mylist = list('abcdefghijklmnopqrstuvwxyz')
    length = request.GET.get('length')
    upper = request.GET.get('uppercase')
    number = request.GET.get('number')
    spchar = request.GET.get('specialchar')
    if upper:
        mylist.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if spchar:
        mylist.extend(list('%$#@!&*^'))
    if number:
        mylist.extend(list('1234567890'))
    mypass = ''.join(random.sample(mylist, int(length)))
    
    return render(request, 'generator/newpage.html', {'mypass':mypass})