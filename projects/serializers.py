from rest_framework import serializers 
from .models import Logger, TestLogger, WalletMapper
 
 
class LoggerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Logger
        fields = ('id',
                  'error_name',
                  'error_description',
                  'error_object',
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
                  'error_object',
                  'status_code',
                  'slug',
                  'timestamp',
                  'wallet_address')

class WalletMapperSerializer(serializers.ModelSerializer):

    class Meta:
        model = WalletMapper
        fields = "__all__"