from django.http import HttpResponseForbidden


class AuthenticationDecorator:
    def __init__(self, view_func):
        self.view_func = view_func

    def __call__(self, request, *args, **kwargs):
        if "Auth-Token" not in request.headers:
            return HttpResponseForbidden("Authentication required")

        token = request.headers["Auth-Token"]
        if not self.authenticate(token):
            return HttpResponseForbidden("Invalid authentication token")

        return self.view_func(request, *args, **kwargs)

    def authenticate(self, token):
        return token == "valid-token"
