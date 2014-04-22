# coding=utf-8
import sys

from optparse import make_option

from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--stderr',
                    action='store_true',
                    dest='stderr',
                    default=False,
                    help='dublicate output to stderr'),
    )

    help = 'Print all model with count object'

    def handle(self, *args, **kwargs):
        for table in ContentType.objects.all():
            name = str(table)
            count = str(table.model_class().objects.count())
            row = 'Table: ' + name + '  object count: ' + count
            print(row)
            if kwargs.get('stderr'):
                sys.stderr.write('error: '+row+'\n')