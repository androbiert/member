from django.shortcuts import render,redirect,get_list_or_404
from .models import Member
from django.contrib import messages
from .forms import MemberForm
def home(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            # Create a new Member instance without setting the 'id' manually
            member = form.save(commit=False)
            member.save()
            messages.success(request,'Member Submited successflly')
            return redirect('home')  # Redirect to avoid re-posting the form on refresh

    else:
        form = MemberForm()

    return render(request, 'homeVillage/home.html', {'form': form})

def profile(request):
    members = Member.objects.all()
    context = {
        "members":members,
    }
    return render(request,'homeVillage/profile.html',context=context)

def delete_member(request,id):
    member = get_list_or_404(Member,id=id)[0]

    if member:
        print(member)
        member.delete()
        messages.success(request,'Member Deleted Successfully ')
    return redirect('profile')

