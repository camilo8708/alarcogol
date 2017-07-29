import shutil, os
import subprocess

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        origen = 'static/models.py'
        destino = '/app/.heroku/python/lib/python3.6/site-packages/instagram/models.py'

        text = open(destino, 'r')
        ct = 1
        for line in text:
            if ct > 90 and ct < 110:
                print(str(ct) + ' - ' +str(line))
            ct=ct+1