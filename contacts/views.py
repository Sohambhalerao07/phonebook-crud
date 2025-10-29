import requests
from django.db.models import Count
from django.db.models.functions import TruncDate
from rest_framework import viewsets, decorators, response, status
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Contact
from .serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('-created_at')
    serializer_class = ContactSerializer

    # Example external API: Predict age based on name
    @decorators.action(detail=True, methods=['post'], url_path='predict-age')
    def predict_age(self, request, pk=None):
        contact = self.get_object()
        name = contact.full_name.split()[0]
        try:
            r = requests.get("https://api.agify.io", params={"name": name}, timeout=10)
            data = r.json()
            return response.Response({"predicted_age": data.get("age", "N/A")})
        except requests.RequestException as e:
            return response.Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@decorators.api_view(['GET'])
def contact_report(request):
    data = (
        Contact.objects
        .annotate(day=TruncDate('created_at'))
        .values('day')
        .annotate(count=Count('id'))
        .order_by('day')
    )
    labels = [d['day'].strftime('%Y-%m-%d') for d in data]
    values = [d['count'] for d in data]
    return JsonResponse({'labels': labels, 'values': values})


# Web UI views
def contact_list(request):
    contacts = Contact.objects.all().order_by('-created_at')
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})


def contact_create(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        Contact.objects.create(full_name=full_name, email=email, phone=phone)
        messages.success(request, 'Contact created successfully.')
        return redirect('contact_list')
    return render(request, 'contacts/contact_form.html', {'action': 'Create'})


def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.full_name = request.POST.get('full_name')
        contact.email = request.POST.get('email')
        contact.phone = request.POST.get('phone')
        contact.save()
        messages.success(request, 'Contact updated successfully.')
        return redirect('contact_list')
    return render(request, 'contacts/contact_form.html', {'contact': contact, 'action': 'Update'})


def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        messages.success(request, 'Contact deleted successfully.')
        return redirect('contact_list')
    return render(request, 'contacts/contact_confirm_delete.html', {'contact': contact})
