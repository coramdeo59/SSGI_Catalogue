from rest_framework.serializers import ModelSerializer
from .models import ssgi

class SSGISerializer(ModelSerializer):
    class Meta:
        model = ssgi
        fields = '__all__'