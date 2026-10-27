from rest_framework import serializers

from exams.models import AssementModel

from problem.models import QuestionModel
from problem.serialiserz import QuestionSerilaizer

from django.db.models import Sum

class AssementSerializer(serializers.ModelSerializer):


    question_count = serializers.SerializerMethodField(read_only=True)

    total_marks = serializers.SerializerMethodField(read_only =True)

    question = serializers.SerializerMethodField(read_only=True)

    class Meta:

        model = AssementModel

        fields = '__all__'

        read_only_fields = ["id","end_time","created_by"]



    def get_question_count(self,obj):

        return QuestionModel.objects.filter(assesment=obj).count()

    def get_total_marks(self,obj):

        return QuestionModel.objects.filter(assesment=obj).values("score").aggregate(total=Sum("score")).get("total")

    def get_question(self,obj):

        question_object = QuestionModel.objects.filter(assesment=obj)

        serializer_instance = QuestionSerilaizer(question_object,many=True)

        return serializer_instance.data

    