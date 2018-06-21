from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import User
from .forms import UserForm


class ProfilePageDetail(TemplateView):
    template_name = 'accounts/profile.html'
    model = User

    def get_queryset(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        return redirect('accounts:signup')


class CreateUserView(CreateView):
    model = User
    template_name = 'accounts/signup.html'
    form_class = UserForm

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('accounts:profile')

        return self.form_invalid(form)





