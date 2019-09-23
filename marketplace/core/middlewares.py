from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect
from django.urls import resolve, reverse
from django.conf import settings
from django.shortcuts import redirect


class LoginRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.user.is_authenticated:
            current_path = resolve(request.path_info).url_name
            if not current_path in settings.LOGIN_EXEMPT_URL:
                return HttpResponseRedirect(reverse(settings.LOGIN_URL))
