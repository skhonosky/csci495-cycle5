"""
Tests for models.
"""

from django.test import TestCase

from core import models

class ModelTests(TestCase):
    
    ## test airport model test
    def test_create_airport(self):
        """Test Creating an Airport is Successful"""
        airport = models.Airport.objects.create(
            name="Myrtle Beach International",
            airport_code="MYR",
            address="1100 Jetport Rd",
            city="Myrtle Beach",
            state="SC",
            zip_code="29577"
        )

        self.assertEqual(str(airport), (airport.name))

    def test_create_player(self):
        player = models.Player.objects.create(
            name="Lonzo Ball",
            sport="Basketball",
            team="Chicago Bulls",
            position="Point Guard"
        )

        self.assertEqual(str(player), (player.name))

    def test_create_footballTeam(self):
        footballteam = models.footballTeam.objects.create(
            name="Kansas City Chiefs",
            conference="AFC",
            quarterback="Patrick Mahomes",
            city="Kansas City",
            state="MO",
        )

        self.assertEqual(str(footballteam), (footballteam.name))

    def test_create_basketballTeam(self):
        basketballteam = models.basketballTeam.objects.create(
            name="Kansas City Chiefs",
            conference="Eastern",
            legendary_player="Michael Jordan",
            city="Chicago",
            state="IL",
        )

        self.assertEqual(str(basketballteam), (basketballteam.name))
   
    