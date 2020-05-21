import logging
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("user_count", type=int)

    def handle(self, *args, **options):
        batch_size = 1000
        user_count = options["user_count"]
        users = []
        for i in range(1, user_count + 1):
            username = f"user_{i}"
            user = User(username=username)
            user.set_unusable_password()
            users.append(user)
            if i % batch_size == 0:
                logger.info("User #%s created", i)
        User.objects.bulk_create(
            users, batch_size=batch_size, ignore_conflicts=True)
