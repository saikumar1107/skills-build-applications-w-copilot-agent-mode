from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class BasicModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        self.user = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=self.team, is_superhero=True)
        self.workout = Workout.objects.create(name='Web Swing', description='Swinging through the city', difficulty='Medium')
        self.activity = Activity.objects.create(user=self.user, type='Swing', duration=30, date='2025-11-26')
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100, rank=1)

    def test_user_creation(self):
        self.assertEqual(self.user.name, 'Spider-Man')
        self.assertTrue(self.user.is_superhero)

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Marvel')

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, 'Web Swing')

    def test_activity_creation(self):
        self.assertEqual(self.activity.type, 'Swing')

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.points, 100)
