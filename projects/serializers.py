from rest_framework import serializers 
from .models import Logger, TestLogger
 
 
class LoggerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Logger
        fields = ('id',
                  'error_name',
                  'error_description',
                  'status_code',
                  'slug',
                  'timestamp',
                  'wallet_address')

class TestLoggerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = TestLogger
        fields = ('id',
                  'error_name',
                  'error_description',
                  'status_code',
                  'slug',
                  'timestamp',
                  'wallet_address')