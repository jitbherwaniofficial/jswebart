from blog.forms import SubscriptionForm
from django.http import JsonResponse


def subscribe(request):
    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True, "message": "Thank you for subscribing!"})
        else:
            return JsonResponse({"success": False, "message": "Failed to subscribe. This email is already in use."})
    return JsonResponse({"success": False, "message": "Invalid request."})
