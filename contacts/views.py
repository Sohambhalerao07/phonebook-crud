import requests
from django.db.models import Count
from django.db.models.functions import TruncDate
from rest_framework import viewsets, decorators, response, status
from django.http import JsonResponse

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
