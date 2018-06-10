'''
GOAL: Load state table with all of the states possible in a PR
given: A Github Webhook that gives the specific PR that has been detected
return: Inserts rows to the state model of all states related to the head and base
 of a PR.
 Adds commit information about the head and base as well as the mered pr commit
 Insert information about a pull request to the PR table
'''
from django.core.management.base import BaseCommand
from HookCatcher.management.commands.functions.add_pr_info import add_pr_info


class Command(BaseCommand):
    help = 'Fill the database with info about all the new states with a PR'

    def add_arguments(self, parser):
        # the Pull Request Number as argument
        parser.add_argument('prNumber', type=int)

    def handle(self, *args, **options):
        prNumber = options['prNumber']
        add_pr_info(prNumber)
