from django.contrib.auth.models import User
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    events = serializers.PrimaryKeyRelatedField(many=True, queryset=Event.objects.all())

    class Meta:
        model = User
        fields = ('id', 'name', 'description')
