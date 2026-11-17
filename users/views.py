from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import generic

from users.models import CustomUser
from users.forms import CustomRegisterForm, CustomAuthLoginForm


#REGISTER
class RegisterView(generic.CreateView):
    template_name = 'users/register.html'
    form_class = CustomRegisterForm
    success_url = reverse_lazy('log')

    def form_valid(self, form):
        return super(RegisterView, self).form_valid(form=form)


#AUTHORIZATION
class AuthLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = CustomAuthLoginForm

    def get_success_url(self):
        return reverse_lazy('prof')


#LOGOUT
class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('log')


#PROFILE
class ProfileView(LoginRequiredMixin, generic.DetailView):
    template_name = 'users/profile.html'
    context_object_name = 'user'
    model = CustomUser
    login_url = reverse_lazy('log')

    def get_object(self, queryset=None):
        return CustomUser.objects.get(id=self.request.user.id)


# ---------- Старая версия на функциях (FBV) ----------
# #register
# def register_view(request):
#     if request.method == "POST":
#         #form_user = UserCreationForm(request.POST)
#         form_user = CustomRegisterForm(request.POST, request.FILES)
#         if form_user.is_valid():
#             form_user.save()
#             return redirect('/login/')
#     else:
#         #form_user = UserCreationForm()
#         form_user = CustomRegisterForm()
#     return render(request, 'users/register.html', {'form': form_user})
#
# #authorization
# def auth_login_view(request):
#     if request.method == "POST":
#         #form_user = AuthenticationForm(data=request.POST)
#         form_user = CustomAuthLoginForm(data=request.POST)
#         if form_user.is_valid():
#             user = form_user.get_user()
#             login(request, user)
#             return redirect('/profile/')
#     else:
#         #form_user = AuthenticationForm()
#         form_user = CustomAuthLoginForm()
#     return render(request, 'users/login.html', {'form': form_user})
#
# #logout
# def auth_logout_view(request):
#     logout(request)
#     return redirect('/login/')
#
# #profile
# def profile_view(request):
#     if not request.user.is_authenticated:
#         return ('/login/')
#     user = CustomUser.objects.get(id=request.user.id)
#     return render(request, 'users/profile.html', {'user': user})
