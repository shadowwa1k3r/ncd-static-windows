from rest_framework.serializers import ModelSerializer
from faq.models import Faq, FaqCategory


class FaqSerializer(ModelSerializer):
    class Meta:
        model = Faq
        fields = (
            'question_uz',
            'question_ru',
            'question_en',
            'answer_uz',
            'answer_ru',
            'answer_en',
            'status',
            )


class FaqCategorySerializer(ModelSerializer):
    faqs = FaqSerializer(many=True)

    class Meta:
        model = FaqCategory
        fields = (
            'name_uz',
            'name_ru',
            'name_en',
            'status',
            )
