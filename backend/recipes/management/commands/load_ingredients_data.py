import json
from django.core.management import BaseCommand
from tqdm import tqdm
from typing import Any, Optional
from recipes.models import Ingredient


class Command(BaseCommand):
    """
    Класс команды для загрузки данных
    игнредиентов из json файла.
    """
    filename: str = 'ingredients'
    file: str = 'static/data/' + filename + '.json'

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        if Ingredient.objects.exists():
            self.stdout.write(
                'Initial data '
                '\033[0;33;48m{}\033[0;0m '
                'already exists.'.format(self.filename)
            )
            return

        with open(self.file, 'rb') as fin:
            data: list[dict[str, str]] = json.load(fin)

            for entry in tqdm(data):
                ingredient = Ingredient()
                ingredient.name = entry.get('name')
                ingredient.measurement_unit = entry.get('measurement_unit')
                ingredient.save()