from rest_framework import serializers
from .models import *

class Page1Serializer(serializers.ModelSerializer):
	class Meta:
		model = Page1
		fields = '__all__'

class QuestionSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question','option1','option2','option3','option4']