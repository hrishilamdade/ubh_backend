import json
from rest_framework import serializers
from .models import *

class EmpanelmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empanelment
        fields = '__all__'

    
class MetaExpertSerializer(serializers.ModelSerializer):

    skills = serializers.JSONField()
    
    class Meta:
        model = MetaExpert
        fields = [
            "name",
            "email",
            "phone",
            "company",
            "designation",
            "reference_id",
            "biography",
            "price",
            "geography",
            "skills"
        ]

        
    def get_skills(self,obj):
        skills = obj.skills
        if skills:
            return json.loads(skills)
        return []