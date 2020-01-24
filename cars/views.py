from django.shortcuts import render
from .models import Profile
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm,UserForm,UpdateUserForm,UpdateUserProfileForm,NewGariForm
from .models import Gari,Profile
from .serializer import ProfileSerializer,GariSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST,request.FILES)
        if form.is_valid():
            user=form.save()
            user.refresh_from_db()
            user.profile.name=form.cleaned_data.get('name')

            user.profile.Bio=form.cleaned_data.get('Bio')

            user.profile.profile_image=form.cleaned_data.get('profile_image')
            user.save()
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=user.username,password=raw_password)
            return redirect (home)
            login(request, user)
            return redirect (home)

    else:
        form=SignUpForm()
    return render (request,'registration/registration_form.html',{'form':form})

@login_required(login_url='/accounts/login/')
def home(request):
    '''
    View for the main homepage.
    '''
    all_garis=Gari.objects.all()
    logged_in_user = request.user
    logged_in_user_garis=Gari.objects.filter(user=logged_in_user)
    try:
        profile=Profile.objects.filter(user=logged_in_user)
    except Profile.DoesNotExist:
        profile=None
    return render(request,'home.html',{"garis":logged_in_user_garis,"profile":profile,"allgaris":all_garis})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.all()

    if request.method == 'POST':
        u_form = UpdateUserForm(request.POST,instance=request.user)
        p_form = UpdateUserProfileForm(request.POST, request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            
            return render(request,'profile/profile.html')
    else:
        u_form = UpdateUserForm(instance=request.user)
        p_form = UpdateUserProfileForm(instance=request.user.profile)


    context = {
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request, 'profile/profile.html',locals())

class GariList(APIView):
    '''
    End point that returns all garis posted and the details such as title,
    image,description and price
    '''
    def get(self, request, format=None):
        all_gari = Gari.objects.all()
        serializers = GariSerializer(all_gari, many=True)
        return Response(serializers.data)

    
@login_required(login_url='/accounts/login/')
def sell_gari(request):
    current_user = request.user
    print(current_user)
    if request.method == 'POST':
        form = NewGariForm(request.POST, request.FILES)
        if form.is_valid():
            gari = form.save(commit=False)
            gari.editor = request.user
          
            gari.save()
        return redirect('home')

    else:
        form = NewGariForm()
    return render(request, 'sell_gari.html', {"form": form})
