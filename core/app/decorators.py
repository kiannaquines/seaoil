from django.shortcuts import redirect

def check_already_loggedin(view_func):
    def _wrapped_view(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request,*args,**kwargs)
    
    return _wrapped_view


def check_if_can_edit(view_func):
    def _wrapped_view(request,*args,**kwargs):
        user = request.user
        if user.is_authenticated and user.is_staff:
            return view_func(request,*args,**kwargs)
        else:
            return redirect('/')
    
    return _wrapped_view

def check_if_can_delete(view_func):
    def _wrapped_view(request,*args,**kwargs):
        user = request.user
        if user.is_authenticated and user.is_staff:
            return view_func(request,*args,**kwargs)
        else:
            return redirect('/')
    
    return _wrapped_view

def check_if_can_view(view_func):
    def _wrapped_view(request,*args,**kwargs):
        user = request.user
        if user.is_authenticated and user.is_staff:
            return view_func(request,*args,**kwargs)
        else:
            return redirect('/')
    
    return _wrapped_view