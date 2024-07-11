from django.shortcuts import redirect
from app.models import CustomUser
from django.contrib import messages

def check_already_loggedin(view_func):
    def _wrapped_view(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request,*args,**kwargs)
    
    return _wrapped_view


def check_user_permission_based_on_user_type(view_func):
    def _wrapped_view(request,*args,**kwargs):
        user = request.user
        if user.user_type == CustomUser.USER_TYPE[0][0]:
            return view_func(request,*args,**kwargs)
        else:
            messages.error(request, 'Sorry, you do not have permission to access this page.',extra_tags="not_enought_permission")
            return redirect('/')
        
    return _wrapped_view


def check_if_logged_in(view_func):
    def _wrapped_view(request,*args,**kwargs):
        user = request.user
        if user.user_type == CustomUser.USER_TYPE[0][0]:
            return view_func(request,*args,**kwargs)
        else:
            messages.error(request, 'Sorry, you need to be authenticated to access this page.',extra_tags="not_enought_permission")
            return redirect('/auth/login/')
        
    return _wrapped_view
