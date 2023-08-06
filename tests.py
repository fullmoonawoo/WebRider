import unittest
from ws_engine import WebRider


class TestWebScrapper(unittest.TestCase):
    def setUp(self) -> None:
        self.my_instance = WebRider("https://sortiment.metro.sk/sk/napoje-tabak/alkohol/gin/6898c/?view_price=s")
        self.my_instance.get_content()

    def test_generating(self):
        self.assertIn(2.15, self.my_instance.check_for(20, "Beefeater").values())


unittest.main()
