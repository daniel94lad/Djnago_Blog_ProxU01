from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import logout
class ProfileCompletionMiddleware:
    # Ensure every user have it´s profile complete 

    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('users:update_profile'),reverse('users:logout')]:
                        return redirect('users:update_profile')

        response = self.get_response(request)
        return response