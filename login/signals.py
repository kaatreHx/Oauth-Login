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

        # Get token
        try:
            token_obj = SocialToken.objects.get(account=sociallogin.account)
            access_token = token_obj.token
            id_token = token_obj.token_secret  # often where Google stores id_token
        except SocialToken.DoesNotExist:
            access_token = None
            id_token = None

        print("\n✅ Google OAuth Login Successful")
        print(f"User: {user.email}")
        print("📦 Raw Google User Info:")
        print(json.dumps(extra_data, indent=2))

        print("🔑 Access Token:", access_token)
        print("🆔 ID Token:", id_token)
        print("🆔 ID Token from extra_data:", extra_data)
