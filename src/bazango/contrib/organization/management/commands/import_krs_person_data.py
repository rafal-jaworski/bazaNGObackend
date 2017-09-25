from django.core.management.base import BaseCommand, CommandError
from bazango.contrib.organization.models import Organization, KRS_FIELD_MAP, Person
import requests


class Command(BaseCommand):
    help = 'Download data from KRS API'

    def handle(self, *args, **options):
        querystring = {"layers[]": Organization.LAYER_MAP.keys()}
        url = "https://api-v3.mojepanstwo.pl/dane/krs_podmioty/{}.json"
        for organization in Organization.objects.exclude(krs=''):
            layers = requests.get(url.format(organization.external_id), params=querystring).json()['layers']
            organization.administration.set([])
            organization.supervisory_authority.set([])
            self._process_layers(organization, layers)

    def _process_layers(self, organization, layers):
        self.stdout.write("KRS:\t{}".format(organization.krs))
        mapped_layers = {Organization.LAYER_MAP[layer]: [{Person.FIELD_MAP[k][0]: Person.FIELD_MAP[k][1](v)
                                                          for k, v in person.items() if k in Person.FIELD_MAP.keys()}
                                                         for person in persons if person.get('osoba_id') and
                                                         person.get('data_urodzenia') == '0000-00-00']
                         for layer, persons in layers.items()
                         if layer in Organization.LAYER_MAP.keys()}

        processed_layers = {layer: [Person.objects.update_or_create(external_id=person.pop('external_id'),
                                                                    defaults=person)[0]
                                    for person in persons]
                            for layer, persons in mapped_layers.items()}

        for layer, persons in processed_layers.items():
            getattr(organization, layer).set(persons)
