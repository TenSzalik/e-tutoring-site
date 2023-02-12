from rest_framework import serializers
from drf_extra_fields.fields import DateRangeField
from .models import Tutorial, PremiumTutorial


class PremiumTutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiumTutorial
        fields = [
            "id",
            "status",
        ]


class TutorialReadSerializer(serializers.ModelSerializer):
    date = DateRangeField()
    premiumtutorial_set = PremiumTutorialSerializer(many=True)

    class Meta:
        model = Tutorial
        fields = [
            "id",
            "name",
            "date",
            "price",
            "description",
            "scope",
            "lvl",
            "essential",
            "learning_form",
            "homework",
            "status",
            "place",
            "support_disabled",
            "premiumtutorial_set",
        ]


class TutorialCreateUpdateSerializer(serializers.ModelSerializer):
    date = DateRangeField()

    class Meta:
        model = Tutorial
        fields = [
            "id",
            "name",
            "date",
            "price",
            "description",
            "scope",
            "lvl",
            "essential",
            "learning_form",
            "homework",
            "status",
            "place",
            "support_disabled",
        ]
