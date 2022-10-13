'''
Docs:

custom management commands docs:
https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/

CRUD operations & working with database models/objects :
https://docs.djangoproject.com/en/4.1/intro/tutorial02/#playing-with-the-api 
'''

from django.core.management.base import BaseCommand, CommandError
from storyer.models import Student, Assignment

# to run: python3 manage.py test
# or py manage.py test


class Command(BaseCommand):
    help = 'Places students into assignment groups'

    '''
    def add_arguments(self, parser):
     '''

    # prints out all students in db
    def handle(self, *args, **options):
        print(Student.objects.all())
