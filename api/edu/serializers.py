from rest_framework.serializers import ModelSerializer
from edu.models import Documents, Edu


class EduSerializer(ModelSerializer):
    class Meta:
        model = Edu
        fields = (
            'title_uz',
            'title_ru',
            'title_en',
            'short_content_uz',
            'short_content_ru',
            'short_content_en',
            'content_uz',
            'content_en',
            'content_ru',
            'status',
            'image',
            )

    def create(self, validated_data):
        request = self.context['request']
        if request.POST.getfiles('docs'):
            for doc in request.POST.getfiles('docs'):
                file = Documents(document=doc)
                file.save()
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context['request']
        if request.POST.getfiles('docs'):
            pass
        else:
            validated_data['category'] = instance.category
        return super().update(instance, validated_data)
