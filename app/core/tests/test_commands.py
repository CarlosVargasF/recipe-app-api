"""
Test custom django management commands
"""
from unittest.mock import patch  # change behavior of dependencies while test

from psycopg2 import OperationalError as Psycopg2Error  # db adapter

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase      # no need to create db setup


@patch('core.management.commands.wait_for_db.Command.check')  # cmd to patch
class CommandTests(SimpleTestCase):
    """Test commands"""

    def test_wait_for_db_ready(self, patched_check):  # the arg comes from @
        """test waiting for db if db ready"""
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    # args should be given in order (inner to outter) according to @patches
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """test waiting for db when getting OpError"""
        # use side_effect to raise 5 diff errors (2+3) & return one OK (1)
        patched_check.side_effect = [Psycopg2Error] * 2 + \
            [OperationalError] * 3 + [True]

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])
