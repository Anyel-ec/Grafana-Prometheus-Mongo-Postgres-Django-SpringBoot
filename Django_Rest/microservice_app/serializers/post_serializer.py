from rest_framework import serializers
from microservice_app.models.post import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'user_id', 'category_id', 'time_created', 'image']

        image = serializers.ImageField(required=False)  # Puedes ajustar 'required' según tus necesidades

