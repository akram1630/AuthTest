from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages  # for success msg
# to ensure login to see ur profile:
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegistrationForm
from django.contrib.auth import login
from django.shortcuts import redirect


class HomeView(TemplateView):
  template_name = 'users/home.html'


class ProfileView(LoginRequiredMixin, TemplateView):
  template_name = 'users/profile.html'


class MyLoginView(LoginView):  #it send form in login.html
  redirect_authenticated_user = True  # if user is logged in he don't have to login again like token

  #django can detect auto login.html
  #template_name = 'registration/login.html'

  def get_success_url(self):
    messages.info(self.request, 'Welcome in your profile')
    return reverse_lazy('profile')

  def form_invalid(self, form):
    messages.error(self.request, 'Error in Username or Password')
    return self.render_to_response(self.get_context_data(form=form))


class RegisterView(FormView):
  redirect_authenticated_user = True  # if user is logged in he don't have to login again like token

  form_class = RegistrationForm

  #django can detect auto register.html
  template_name = 'registration/register.html'

  success_url = reverse_lazy('profile')

  #to check if user is logged in
  def dispatch(self, request, *args, **kwargs):
    if request.user.is_authenticated:
      return redirect('profile')
    return super(RegisterView,self).dispatch(request, *args, **kwargs)
  
  def form_valid(self, form):
    user = form.save()
    if user:  #if user filled data
      login(self.request, user)
    return super(RegisterView, self).form_valid(form)
