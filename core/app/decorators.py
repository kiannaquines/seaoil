from django.shortcuts import redirect

def check_already_loggedin(view_func):
    def _wrapped_view(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request,*args,**kwargs)
    
    return _wrapped_view