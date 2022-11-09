from django.db import models

# Create your models here.
class Projects(models.Model):
    title = models.TextField(null=True, blank=True)
    contractAddress = models.TextField(null=True, blank=True)
    abi = models.JSONField(null=True, blank=True)
    network_name = models.CharField(null=True, blank=True, max_length = 255, choices=[('Polygon Matic', 'Polygon Matic'), ('Polygon Mumbai', 'Polygon Mumbai'), ('Ethereum Mainnet', 'Ethereum Mainnet'), ('Ethereum Goerli', 'Ethereum Goerli')])
    description = models.TextField(null=True, blank=True)
    startTimestamp = models.DateTimeField(null=True, blank=True)
    supply = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    banner = models.TextField(null=True, blank=True)
    logo = models.TextField(null=True, blank=True)
    website_url = models.TextField(null=True, blank=True)
    symbol = models.CharField(null=True, blank=True, max_length = 10)
    maxPurchase = models.IntegerField(null=True, blank=True)
    maxWallet = models.IntegerField(null=True, blank=True)
    tokenStandard = models.CharField(null=True, blank=True, max_length=10)
    twitter_url = models.TextField(null=True, blank=True)
    x2y2_url = models.TextField(null=True, blank=True)
    looksrare_url = models.TextField(null=True, blank=True)
    opensea_url = models.TextField(null=True, blank=True)
    rarity_url = models.TextField(null=True, blank=True)
    icytools_url = models.TextField(null=True, blank=True)
    discord_url = models.TextField(null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    isReceivableOnWallet = models.BooleanField(default=False)

    def __str__(self):
         return self.title

class TestProjects(models.Model):
    title = models.TextField(null=True, blank=True)
    contractAddress = models.TextField(null=True, blank=True)
    abi = models.JSONField(null=True, blank=True)
    network_name = models.CharField(null=True, blank=True, max_length = 255, choices=[('Polygon Matic', 'Polygon Matic'), ('Polygon Mumbai', 'Polygon Mumbai'), ('Ethereum Mainnet', 'Ethereum Mainnet'), ('Ethereum Goerli', 'Ethereum Goerli')])
    description = models.TextField(null=True, blank=True)
    startTimestamp = models.DateTimeField(null=True, blank=True)
    supply = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    banner = models.TextField(null=True, blank=True)
    logo = models.TextField(null=True, blank=True)
    website_url = models.TextField(null=True, blank=True)
    symbol = models.CharField(null=True, blank=True, max_length = 10)
    maxPurchase = models.IntegerField(null=True, blank=True)
    maxWallet = models.IntegerField(null=True, blank=True)
    tokenStandard = models.CharField(null=True, blank=True, max_length=10)
    twitter_url = models.TextField(null=True, blank=True)
    x2y2_url = models.TextField(null=True, blank=True)
    looksrare_url = models.TextField(null=True, blank=True)
    opensea_url = models.TextField(null=True, blank=True)
    rarity_url = models.TextField(null=True, blank=True)
    icytools_url = models.TextField(null=True, blank=True)
    discord_url = models.TextField(null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    isReceivableOnWallet = models.BooleanField(default=False)

    def __str__(self):
         return self.title