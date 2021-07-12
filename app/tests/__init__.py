from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = "srujan.krish971@gmail.com"
        password = "12canada34|"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'srujan.krish97@GMAIL.COM'
        user = get_user_model().objects.create_user(email, '')
        self.assertEqual(user.email, email.lower())

    def test_create_new_super_user(self):
        """Test creatting new super user"""
        user = get_user_model().objects.create_superuser(
            'srujan.krish@gmail.com',
            '12234'
        )
        self.assertEqual(user.is_superuser)
        self.assertTrue(user.is_staff)
