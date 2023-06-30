from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import View
from .models import User

def check_ocupation_user(ocupation, user_ocupation):
    #
    
    if (ocupation == User.administrador or ocupation == user_ocupation):
        return True
    else:
        return False



class AdministradorPermisionMixin(LoginRequiredMixin):
    login_url = reverse_lazy('users_app:user-login')
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not check_ocupation_user(request.user.roles_usuario,User.administrador):
            return HttpResponseRedirect(
                reverse( 'users_app:user-login')
            )
        return super().dispatch(request,*args,**kwargs)
    

class MeseroPermisionMixin(LoginRequiredMixin):
    login_url = reverse_lazy('users_app:user-login')
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not check_ocupation_user(request.user.roles_usuario,User.mesero) :
            return HttpResponseRedirect( 
                reverse( 'users_app:user-login')
            )
        elif not check_ocupation_user(request.user.roles_usuario,User.administrador):
                reverse( 'users_app:user-login')

        
        return super().dispatch(request,*args,**kwargs)
    
class CocineroPermisionMixin(LoginRequiredMixin):
    login_url = reverse_lazy('users_app:user-login')
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not check_ocupation_user(request.user.roles_usuario,User.cocinero) or check_ocupation_user(request.user.roles_usuario,User.administrador):
            return HttpResponseRedirect(
                reverse( 'users_app:user-login')
            )
        return super().dispatch(request,*args,**kwargs)