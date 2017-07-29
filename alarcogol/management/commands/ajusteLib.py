import shutil, os
import subprocess

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        origen = 'static/models.py'
        destino = '/app/.heroku/python/lib/python3.6/site-packages/instagram/models.py'

        try:
            shutil.copyfile(origen, destino)
            print("Archivo copiado")
        except:
            print("Se ha producido un error")