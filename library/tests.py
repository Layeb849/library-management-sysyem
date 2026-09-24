from django.test import SimpleTestCase
from django.urls import reverse


class AchievementUrlTests(SimpleTestCase):
    def test_achievement_list_url_name_exists(self):
        self.assertEqual(reverse('achievement_list'), '/pathagar/achievements/')

    def test_achievement_detail_url_name_exists(self):
        self.assertEqual(reverse('achievement_detail', args=['sample-achievement']), '/pathagar/achievement/sample-achievement/')
