"""
Test for the django admin modifs
"""

from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTest(TestCase):
    """Tests for django admin"""
    def setUp(self):
        """Create users and client"""
        self.client = Client()  # allows to make http requests
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testpass123',
        )
        self.client.force_login(self.admin_user) 

        self.user=get_user_model().objects.create_user(
            email='user@example.com',
            password='testpass123',
            name='test user'
        )

    def test_users_list(self):
        """test whether users are listed on page"""
        url = reverse('admin:core_user_changelist') # +info: check official docu
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        """Test the edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

