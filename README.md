<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/django-subcommands.svg?maxAge=3600)](https://pypi.org/project/django-subcommands/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/django-subcommands.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/django-subcommands.py/actions)

### Installation
```bash
$ [sudo] pip install django-subcommands
```

#### Examples
`management/commands/command.py`
```python
from django.core.management.base import BaseCommand
import django_subcommands

class SubCommand1(BaseCommand):
    def handle(self, *args, **options):
        ...

class SubCommand2(BaseCommand):
    def handle(self, *args, **options):
        ...

class Command(django_subcommands.SubCommands):
    subcommands = {"subcommand1": SubCommand1,"subcommand2":SubCommand2}
```

```bash
$ python manage.py command subcommand1
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>