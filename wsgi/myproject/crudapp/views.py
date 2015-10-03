from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from django.forms import ModelForm


from crudapp.models import User

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['name', 'address', 'user_id']

def UserList(request, template_name = 'crudapp/user_list.html'):
    crudapp = User.objects.all()
    data = {}
    data['object_list'] = crudapp
    return render(request, template_name, data)

def CreateUser(request, template_name = 'crudapp/user_form.html'):
    form = UserForm(request.POST or None)
    if form.is_valid():
    	form.save()
    	return redirect('user_list')
    return render(request, template_name, {'form' : form})
    

def UpdateUser(request, pk, template_name='crudapp/user_form.html'):
    user = get_object_or_404(User, pk=pk)
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('user_list')
    return render(request, template_name, {'form':form})

def DeleteUser(request, pk, template_name='crudapp/user_confirm_delete.html'):
    user = get_object_or_404(User, pk=pk)    
    if request.method=='POST':
        user.delete()
        return redirect('user_list')
    return render(request, template_name, {'object': user})