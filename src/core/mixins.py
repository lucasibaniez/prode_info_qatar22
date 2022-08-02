
from django.core.exceptions import PermissionDenied

class SuperUserRequiredMixin:

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied
        return super(SuperUserRequiredMixin, self).dispatch(request, *args, **kwargs)

def superuser_required():
    def permission_required(f):
        def check(request, *arg, **kwargs):
            if not request.user.is_superuser:
                raise PermissionDenied
            return f(request, *arg, **kwargs)
    return permission_required     