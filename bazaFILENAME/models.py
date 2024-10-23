from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

class Prosmotr(models.Model):
    title = models.CharField(max_length= 100)

    def __str__(self):
        return self.title

class Smotret(models.Model):
    title = models.CharField(max_length= 100)

    def __str__(self):
        return self.title

class Command(BaseCommand):
    help = 'Create a new permission'

    def smotr(self, *args, **options):
        content_type = ContentType.objects.get_for_model(Smotret)
        permission = Permission.objects.create(
            codename='can_do_smotret',
            name='Can Do Smotret',
            content_type=content_type,
        )

        self.stdout.write(self.style.SUCCESS(f'Created permission: {permission}'))

