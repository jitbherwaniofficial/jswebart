from blog.forms import SubscriptionForm
from django.http import HttpResponse, JsonResponse


def subscribe(request):
    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True, "message": "Thank you for subscribing!"})
        else:
            return JsonResponse({"success": False, "message": "Failed to subscribe. This email is already in use."})
    return JsonResponse({"success": False, "message": "Invalid request."})


from django.template import loader

def robots_txt(request):
    template = loader.get_template('robots.txt')
    content = template.render({})
    return HttpResponse(content, content_type='text/plain')