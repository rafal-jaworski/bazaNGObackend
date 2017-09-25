from django.core.management.base import BaseCommand, CommandError
from bazango.contrib.organization.models import Organization, KRS_FIELD_MAP
import requests


class Command(BaseCommand):
    help = 'Download data from KRS API'

    def handle(self, *args, **options):
        url = "https://api-v3.mojepanstwo.pl/dane/krs_podmioty.json"

        querystring = {"conditions[krs_podmioty.forma_prawna_typ_id]": "2",
                       "conditions[krs_podmioty.powiat_id]": "100",
                       "limit": "100"}

        response = requests.get(url, params=querystring).json()
        self._process_response(response)
        while 'next' in response['Links']:
            response = requests.get(response['Links']['next']).json()
            self._process_response(response)

    def _process_response(self, response):
        data = response['Dataobject']
        parsed_data = [{KRS_FIELD_MAP[k][0]: KRS_FIELD_MAP[k][1](v) for k, v in obj['data'].items() if k in KRS_FIELD_MAP} for obj in data]
        for organization in parsed_data:
            krs = organization.pop('krs')
            self.stdout.write("KRS:\t{}".format(krs))
            Organization.objects.update_or_create(krs=krs, defaults=organization)
