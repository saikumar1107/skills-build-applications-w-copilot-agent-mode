from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create Users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True),
            User(name='Batman', email='batman@dc.com', team=dc, is_superhero=True),
        ]
        User.objects.bulk_create(users)

        # Create Workouts
        workouts = [
            Workout(name='Web Swing', description='Swinging through the city', difficulty='Medium'),
            Workout(name='Flight', description='Flying in the suit', difficulty='Hard'),
            Workout(name='Lasso Training', description='Lasso of Truth practice', difficulty='Medium'),
            Workout(name='Martial Arts', description='Combat training', difficulty='Hard'),
        ]
        Workout.objects.bulk_create(workouts)

        # Create Activities
        activities = [
            Activity(user=users[0], type='Swing', duration=30, date='2025-11-26'),
            Activity(user=users[1], type='Flight', duration=45, date='2025-11-26'),
            Activity(user=users[2], type='Lasso', duration=40, date='2025-11-26'),
            Activity(user=users[3], type='Combat', duration=50, date='2025-11-26'),
        ]
        Activity.objects.bulk_create(activities)

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=150, rank=1)
        Leaderboard.objects.create(team=dc, points=120, rank=2)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
