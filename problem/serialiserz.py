from rest_framework import serializers

from problem.models import QuestionModel

class QuestionSerilaizer(serializers.ModelSerializer):

    class Meta:

        model = QuestionModel

        fields = "__all__"

        read_only_fields = ["id","assesment","created_at","updated_at","created_by"]