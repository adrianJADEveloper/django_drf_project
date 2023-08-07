from rest_framework import serializers
from .models import Journal


class JournalSerializer(serializers.ModelSerializer):

    class Meta:

        model = Journal
        fields = "__all__"

        # ADDED THIS COMMENT

    # extra_kwargs = {
    #     'price': {'min_value': 2},
    #     'inventory': {'min_value': 0}
    # }
