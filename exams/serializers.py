from rest_framework import serializers

from exams.models import AssementModel

class AssementSerializer(serializers.ModelSerializer):

    class Meta:

        model = AssementModel

        fields = '__all__'

        read_only_fields = ["id","end_time","created_by"]