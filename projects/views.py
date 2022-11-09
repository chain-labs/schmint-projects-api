from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Projects, TestProjects
from django.http import JsonResponse
import calendar

# Create your views here.
class ProjectsAPI(APIView):   
    def get(self, request, format=None):
        projects = []
        data = Projects.objects.all()
        networks = {"Polygon Matic": 137,
                    "Polygon Mumbai": 80001,
                    "Ethereum Mainnet": 1,
                    "Ethereum Goerli": 5
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

class TestProjectsAPI(APIView):   
    def get(self, request, format=None):
        projects = []
        data = TestProjects.objects.all()
        networks = {"Polygon Matic": 137,
                    "Polygon Mumbai": 80001,
                    "Ethereum Mainnet": 1,
                    "Ethereum Goerli": 5
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