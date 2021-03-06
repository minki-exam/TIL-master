from django.shortcuts import render, HttpResponse
import random

# Create your views here.
def cube(request, num):
    #장고에서 기본 자료형은 리턴 안됨
    r = num**3
    context = {'result' : r}
    return render(request, 'cube.html', context)

def check_int(request, num):
    is_even = num % 2 == 0
    context ={'is_even' : is_even}
    return render(request, 'check_int.html', {
        'is_even' : is_even,
    })

def pick_lotto(request):
    return render(request, 'pick_lotto.html' ,{
        'lucky_numbers': random.sample(range(1,46), 6) 
    })
    