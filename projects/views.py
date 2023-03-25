from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Projects, TestProjects, Logger, TestLogger, WalletMapper
from django.http import JsonResponse
import calendar
from django import http
from django.conf import settings
from .serializers import LoggerSerializer, TestLoggerSerializer, WalletMapperSerializer

# Create your views here.
class ProjectsAPI(APIView):   
    def get(self, request, format=None):
        projects = []
        data = Projects.objects.all()
        networks = {"Polygon": 137,
                    "Polygon Mumbai": 80001,
                    "Ethereum": 1,
                    "Goerli": 5
                    }

        for project in data:
            startTimestamp = project.startTimestamp
            if startTimestamp:
                startTimestamp = calendar.timegm(startTimestamp.utctimetuple())
            projectJSON = {
                            "id": str(project.id),
                            "title": project.title,
                            "contractAddress": project.contractAddress,
                            "abi": project.abi,
                            "network": {
                                "chainId": networks[project.network_name],
                                "name": project.network_name
                            },
                            "description": project.description,
                            "startTimestamp": startTimestamp,
                            "supply": project.supply,
                            "price": project.price,
                            "banner": project.banner,
                            "logo": project.logo,
                            "website_url": project.website_url,
                            "symbol": project.symbol,
                            "maxPurchase": project.maxPurchase,
                            "maxWallet": project.maxWallet,
                            "tokenStandard": project.tokenStandard,
                            "isReceivableOnWallet": project.isReceivableOnWallet,
                            "mintTimestampNotDecided": project.mintTimestampNotDecided,
                            "socials": {
                                "twitter_url": project.twitter_url,
                                "x2y2_url": project.x2y2_url,
                                "looksrare_url": project.looksrare_url,
                                "opensea_url": project.opensea_url,
                                "rarity_url": project.rarity_url,
                                "icytools_url": project.icytools_url,
                                "discord_url": project.discord_url
                            }
                        }
            projects.append(projectJSON)
        return JsonResponse(projects, safe=False)
    
class WalletMapperAPI(APIView):
    def get(self, request, walletAddress):
        data = WalletMapper.objects.get(walletAddress=walletAddress)
        return JsonResponse({data.walletAddress: data.emailAddress}, safe=False)
    
    def post(self, request):
        mapping = request.data.get('mapping')
        mapperSerializer = WalletMapperSerializer(data = mapping)
        if mapperSerializer.is_valid():
            mapperSerializer.save()
            return JsonResponse(mapperSerializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(mapperSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TestProjectsAPI(APIView):   
    def get(self, request, format=None):
        projects = []
        data = TestProjects.objects.all()
        networks = {"Polygon": 137,
                    "Polygon Mumbai": 80001,
                    "Ethereum": 1,
                    "Goerli": 5
                    }

        for project in data:
            startTimestamp = project.startTimestamp
            if startTimestamp:
                startTimestamp = calendar.timegm(startTimestamp.utctimetuple())
            projectJSON = {
                            "id": str(project.id),
                            "title": project.title,
                            "contractAddress": project.contractAddress,
                            "abi": project.abi,
                            "network": {
                                "chainId": networks[project.network_name],
                                "name": project.network_name
                            },
                            "description": project.description,
                            "startTimestamp": startTimestamp,
                            "supply": project.supply,
                            "price": project.price,
                            "banner": project.banner,
                            "logo": project.logo,
                            "website_url": project.website_url,
                            "symbol": project.symbol,
                            "maxPurchase": project.maxPurchase,
                            "maxWallet": project.maxWallet,
                            "tokenStandard": project.tokenStandard,
                            "isReceivableOnWallet": project.isReceivableOnWallet,
                            "mintTimestampNotDecided": project.mintTimestampNotDecided,
                            "socials": {
                                "twitter_url": project.twitter_url,
                                "x2y2_url": project.x2y2_url,
                                "looksrare_url": project.looksrare_url,
                                "opensea_url": project.opensea_url,
                                "rarity_url": project.rarity_url,
                                "icytools_url": project.icytools_url,
                                "discord_url": project.discord_url
                            }
                        }
            projects.append(projectJSON)
        return JsonResponse(projects, safe=False)


class LoggerAPI(APIView):   
    def get(self, request, format=None):
        if request.META['REMOTE_ADDR'] not in settings.ALLOWED_IPS:
             return http.HttpResponseForbidden('<h1>Forbidden</h1>')
        data = Logger.objects.values('id', 'error_name', 'error_description', 'error_object', 'status_code', 'wallet_address', 'slug', 'timestamp')
        return Response(data)

    def post(self, request, format=None):
        if request.META['REMOTE_ADDR'] not in settings.ALLOWED_IPS:
             return http.HttpResponseForbidden('<h1>Forbidden</h1>')

        log_data = request.data.get('logs')
        logger_serializer = LoggerSerializer(data=log_data)
        if logger_serializer.is_valid():
            logger_serializer.save()
            return JsonResponse(logger_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(logger_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TestLoggerAPI(APIView):   
    def get(self, request, format=None):
        data = TestLogger.objects.values('id', 'error_name', 'error_description', 'error_object', 'status_code', 'wallet_address', 'slug', 'timestamp')
        return Response(data)

    def post(self, request, format=None):
        test_log_data = request.data.get('logs')
        test_logger_serializer = TestLoggerSerializer(data=test_log_data)
        if test_logger_serializer.is_valid():
            test_logger_serializer.save()
            return JsonResponse(test_logger_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(test_logger_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
