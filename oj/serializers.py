from rest_framework import serializers
from .models import User,Question, Submission

class OjSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id' ,'question_name', 'question_description', 'question_input_file','question_output_file')
