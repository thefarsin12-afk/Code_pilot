from rest_framework import serializers

from evaluation.models import Submission,Answer

from evaluation.models import QuestionModel

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

    question = serializers.PrimaryKeyRelatedField(query_set=QuestionModel.objects.all())

    class Meta:

        model = Answer

        fields = "__all__"

        read_only_fields = ["id","submission","marks_awarded","feedback","evaluated_at"]


    def validate(self,validate_data):

        marks_awarded = validate_data.get("marks_awarded")

        score = validate_data.get("score")

        if marks_awarded > score:

            return serializers.ValidationError("Marks awarded > to score")

        return marks_awarded

         