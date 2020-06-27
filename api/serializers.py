from rest_framework.serializers import HyperlinkedModelSerializer

from .models import PostItem


class PostItemSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = PostItem
        fields = [
            'id',
            'category_choice',
            'text',
            'upvotes',
            'downvotes',
            'submission_time',
            'magic_key',
            'vote_score',
            ]