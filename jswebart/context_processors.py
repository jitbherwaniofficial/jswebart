from blog.forms import SubscriptionForm

def subscription_form(request):
    form = SubscriptionForm()
    
    return {'subscription_form': form}