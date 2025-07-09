# signals.py
from allauth.socialaccount.signals import social_account_added, social_account_updated
from allauth.socialaccount.models import SocialToken
from django.dispatch import receiver
import json

@receiver(social_account_added)
@receiver(social_account_updated)
def google_login_handler(request, sociallogin, **kwargs):
    if sociallogin.account.provider == 'google':
        user = sociallogin.user
        extra_data = sociallogin.account.extra_data

        access_token = None
        id_token = None

        if hasattr(sociallogin, 'token'):
            access_token = getattr(sociallogin.token, 'token', None)
            id_token = getattr(sociallogin.token, 'token_secret', None)

        print("\n✅ Google OAuth Login Successful")
        print(f"User: {user.email}")
        print("📦 Raw Google User Info:")
        print(json.dumps(extra_data, indent=2))

        print("🔑 Access Token:", access_token)
        print("🆔 ID Token:", id_token)
