<!--
https://pypi.org/project/readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/django-subcommands.svg?longCache=True)](https://pypi.org/project/django-subcommands/)
[![](https://img.shields.io/pypi/v/django-subcommands.svg?maxAge=3600)](https://pypi.org/project/django-subcommands/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/django-subcommands.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/django-subcommands.py/)

#### Installation
```bash
$ [sudo] pip install django-subcommands
```

#### Classes
class|`__doc__`
-|-
`django_subcommands.SubCommands` |SubCommands class. attrs: `subcommands` (dict)

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
    <a href="https://pypi.org/project/readme-generator/">readme-generator</a>
</p>