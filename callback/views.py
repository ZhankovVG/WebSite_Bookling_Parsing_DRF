from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import CallbackRequest
from .forms import CallbackForm


class CallbackRequestView(View):
    template_name = 'callback/callback.html'
    form_class = CallbackForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            request_entry = CallbackRequest(phone_number=phone_number)
            request_entry.save()
            return HttpResponse(f"Запит на передзвін надіслано на номер: {phone_number}")
        return render(request, self.template_name, {'form': form})
