from rest_framework import serializers

from evaluation.models import Submission,Answer

class SubmissionSerializers(serializers.ModelSerializer):

    assessment = serializers.StringRelatedField(read_only=True)

    student = serializers.StringRelatedField(read_only=True)

    answers = serializers.SerializerMethodField(read_only=True)


    class Meta:

        model = Submission

        fields = "__all__"

        read_only_fields = [fields]

    # def get_fields(self):

    #     fields= super().get_fields()

    #     for field in fields.values():

    #         field.read_only = True

    #     return fields    

    def get_answers(self,obj):

        answer_object = Answer.objects.filter(submission=obj)

        serializer_instants = AnswerSerializer(answer_object,many=True)

        return serializer_instants.data
    

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:

        model = Answer

        fields = "__all__"

        read_only_fields = ["id","submission","marks_awarded","feedback","evaluated_at"]

