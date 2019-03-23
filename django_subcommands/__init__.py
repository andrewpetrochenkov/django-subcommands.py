#!/usr/bin/env python
from django.core.management.base import BaseCommand
import public


@public.add
class SubCommands(BaseCommand):
    """SubCommands class. attrs: `subcommands` (dict)"""
    argv = []
    subcommands = {}

    def add_arguments(self, parser):
        subparsers = parser.add_subparsers(
            dest='subcommand',
            title='subcommands',
            description='')
        subparsers.required = True

        for command_name, command_class in self.subcommands.items():
            command = command_class()

            subparser = subparsers.add_parser(command_name, help=command_class.help)
            command.add_arguments(subparser)
            command_parser = command.create_parser(self.argv[0], self.argv[1])
            subparser._actions = command_parser._actions

    def run_from_argv(self, argv):
        self.argv = argv
        return super(SubCommands, self).run_from_argv(argv)

    def handle(self, *args, **options):
        command_name = self.argv[2]
        self.subcommands.get(command_name)
        if command_name not in self.subcommands:
            raise ValueError("unknown subcommand: %" % command_name)
        command_class = self.subcommands[command_name]

        if len(self.argv):
            args = [self.argv[0]] + self.argv[2:]
            return command_class().run_from_argv(args)
        return command_class().execute(*args, **options)
