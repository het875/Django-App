from rest_framework import serializers
from .models import *

class PollsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email_id", 
                  "mobile_number","password","gender","date_of_birth",
                  "created","updated"]





