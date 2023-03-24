from django.db import models
from django.forms import ValidationError

# Create your models here.
class Projects(models.Model):
    title = models.TextField(null=True, blank=True)
    contractAddress = models.TextField(null=True, blank=True)
    abi = models.JSONField(null=True, blank=True)
    network_name = models.CharField(null=True, blank=True, max_length = 255, choices=[('Polygon', 'Polygon'), ('Polygon Mumbai', 'Polygon Mumbai'), ('Ethereum', 'Ethereum'), ('Goerli', 'Goerli')])
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
    mintTimestampNotDecided = models.BooleanField(default=False)
    isFiatPaymentAccepted = models.BooleanField(default=False)
    fiatPaymentApiIdentifier = models.TextField(null=True, blank=True)

    def __str__(self):
         return self.title
        
    def clean(self):
        if self.isFiatPaymentAccepted and self.fiatPaymentApiIdentifier=="":
            raise ValidationError("fiatPaymentApiIdentifier field cannot be empty when isFiatPaymentAccepted is true")

class TestProjects(models.Model):
    title = models.TextField(null=True, blank=True)
    contractAddress = models.TextField(null=True, blank=True)
    abi = models.JSONField(null=True, blank=True)
    network_name = models.CharField(null=True, blank=True, max_length = 255, choices=[('Polygon', 'Polygon'), ('Polygon Mumbai', 'Polygon Mumbai'), ('Ethereum', 'Ethereum'), ('Goerli', 'Goerli')])
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
    mintTimestampNotDecided = models.BooleanField(default=False)
    isFiatPaymentAccepted = models.BooleanField(default=False)
    fiatPaymentApiIdentifier = models.TextField(null=True, blank=True)

    def __str__(self):
         return self.title
        
    def clean(self):
        if self.isFiatPaymentAccepted and self.fiatPaymentApiIdentifier=="":
            raise ValidationError("fiatPaymentApiIdentifier field cannot be empty when isFiatPaymentAccepted is true")

class Logger(models.Model):
    error_name = models.TextField()
    error_description = models.TextField()
    error_object = models.JSONField(null=True, blank=True)
    status_code = models.IntegerField()
    slug = models.TextField()
    timestamp = models.CharField(max_length=30)
    wallet_address = models.TextField(null=True, blank=True)

class TestLogger(models.Model):
    error_name = models.TextField()
    error_description = models.TextField()
    error_object = models.JSONField(null=True, blank=True)
    status_code = models.IntegerField()
    slug = models.TextField()
    timestamp = models.CharField(max_length=30)
    wallet_address = models.TextField(null=True, blank=True)

class WalletMapper(models.Model):
    walletAddress = models.TextField(primary_key=True)
    emailAddress = models.EmailField()