from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, TemplateView, View
from .models import User
from .forms import CreateUserForm, UpdateUserForm, UpdatePasswordForm, LoginForm


class ProfilePageDetail(TemplateView):
    template_name = 'accounts/profile.html'
    model = User

    def get_queryset(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        return redirect('accounts:signin')


class CreateUserView(CreateView):
    model = User
    template_name = 'accounts/signup.html'
    form_class = CreateUserForm
    object = None

    def form_invalid(self, form):
        self.object = form.instance
        return super().form_invalid(form)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = CreateUserForm(request.POST)

        if request.user.is_authenticated:
            logout(request)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            form.save()

            user = authenticate(username=username, password=password)

            login(request, user)
            return redirect('accounts:profile')

        return self.form_invalid(form)


class UpdateUserBaseView(UpdateView, LoginRequiredMixin):
    model = User

    def get_success_url(self):
        return reverse('accounts:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UpdateUserView(UpdateUserBaseView):
    model = User
    template_name = 'accounts/profile-update.html'
    form_class = UpdateUserForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_action'] = reverse('accounts:update')
        return context


class UpdatePasswordView(UpdateUserBaseView):
    model = User
    template_name = 'accounts/profile-update.html'
    form_class = UpdatePasswordForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_action'] = reverse('accounts:update.password')
        return context

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:signin')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = request.user
        response = super().post(request, *args, **kwargs)
        update_session_auth_hash(request, user)
        return response


class LoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    # form_class = LoginForm

    def get_success_url(self):
        return reverse('accounts:profile')

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)

        return redirect('planner:home')



