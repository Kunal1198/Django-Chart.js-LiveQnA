from django.contrib.auth import get_user_model
from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import View
from django.http import *
from .models import *
from .forms import * 
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import QuestionSerialzer,Page1Serializer
from django.template.loader import render_to_string



#User = get_user_model() 

def exam(request):
    return render(request,'hack/exam.html')

def hel(request):
        return render(request, 'charts.html')



def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # http response


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
    model = Page1

    def get(self, request, format=None):
        qs1 = Page1.objects.filter(card='V').count()
        qs2 = Page1.objects.filter(card='M').count()
        qs3 = Page1.objects.filter(card='P').count()
        qa1 = Page1.objects.filter(question='E').count()
        qa2 = Page1.objects.filter(question='G').count()
        qa3 = Page1.objects.filter(question='A').count()
        qa4 = Page1.objects.filter(question='P').count()
        #serializer = Page1Serializer(qs_count, many=True)
        labels = ["Visa", "Master Card", "Paypal"]
        default_items = [qs1, qs2, qs3]
        labels1 = ["Excellent", "Good", "Average", "Poor"]
        default_items1 = [qa1, qa2, qa3, qa4]
        data = {
                "labels": labels,
                "default": default_items,
                "labels1": labels1,
                "default1": default_items1,
        }
        
        return Response(data)
        
@login_required
def page(request):
    if request.method == 'POST':
        form = Page1Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/polls/graph/')

    else:
        form = Page1Form()
    return render(request,'hack/page1.html',{'form':form})




def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/polls/question/')
                else:
                    return HttpResponse("User is not active")
            else:
                return HttpResponse("User is None")
    else:
        form = UserLoginForm()

    context = {
        'form': form,
    }
    return render(request, 'hack/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('/polls/login/')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            #Profile.objects.create(user=new_user)
            return redirect('/polls/login')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'hack/register.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(data=request.POST or None, instance=request.user)
        #profile_form = ProfileEditForm(data=request.POST or None, instance=request.user.profile, files=request.FILES)
        if user_form.is_valid():
            #print(profile_form)
            user_form.save()
            #profile_form.save()
            #return HttpResponseRedirect(reverse("edit_profile"))
    else:
        user_form = UserEditForm(instance=request.user)
        #profile_form = ProfileEditForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        #'profile_form': profile_form,
    }
    return render(request, 'hack/edit_profile.html', context)

    

class QuestionViewset(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerialzer

