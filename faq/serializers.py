from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    question_translated = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'question_translated', 'answer']

    def get_question_translated(self, obj):
        lang = self.context.get('request').GET.get('lang', 'en')
        return obj.get_translated_question(lang)

