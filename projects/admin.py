from django.contrib import admin
from .models import Projects, TestProjects, Logger, TestLogger, WalletMapper

# Register your models here.

admin.site.register(Projects)
admin.site.register(TestProjects)
admin.site.register(Logger)
admin.site.register(TestLogger)
admin.site.register(WalletMapper)
