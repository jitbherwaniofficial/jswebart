from blog.forms import SubscriptionForm
from decouple import config

def subscription_form(request):
    form = SubscriptionForm()
    SHARE_SITE_KEY = config('SHARE_SITE_KEY')
    return {'subscription_form': form, 'SHARE_SITE_KEY':SHARE_SITE_KEY}