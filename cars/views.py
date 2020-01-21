from django.shortcuts import render

# Create your views here.
def home(request):
    return render ('home.html')


# @login_required(login_url='/accounts/login/')
def new_profile(request):
    '''
    Used for creating a new profile for the user. It includes a profile photo, a bio and contact 
    '''
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.editor = current_user
            profile.save()
        return redirect('home')

    else:
        form = NewProfileForm()
    return render(request, 'update_profile.html', {"form": form}) 