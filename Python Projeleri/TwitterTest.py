# Bu projede Twitter.py dosyasında ki fonksiyonları test edeceğiz.

import unittest
from Twitter import Twitter

class TestTwitter(unittest.TestCase):
    
        def setUp(self):
            self.twitter = Twitter("Twitter", {}, {})
            self.twitter.addUser("User1")
            self.twitter.addUser("User2")
            self.twitter.addUser("User3")
    
        def test_Tweetle(self):
            self.twitter.tweetle("User1", "Tweet1")
            self.assertEqual(self.twitter.tweetList, {"User1": ["Tweet1"]})
            self.twitter.tweetle("User2", "Tweet2")
            self.assertEqual(self.twitter.tweetList, {"User1": ["Tweet1"], "User2": ["Tweet2"]})
            self.twitter.tweetle("User3", "Tweet3")
            self.assertEqual(self.twitter.tweetList, {"User1": ["Tweet1"], "User2": ["Tweet2"], "User3": ["Tweet3"]})

        def test_DiscoverPage(self):
            self.twitter.tweetle("User1", "Tweet1")
            self.twitter.tweetle("User2", "Tweet2")
            self.twitter.tweetle("User3", "Tweet3")
            self.assertEqual(self.twitter.discoverPage(), ["Tweet1", "Tweet2", "Tweet3"])


        def test_new_create_twitter_account(self):
            self.twitter.new_create_twitter_account("User4")
            self.assertEqual(self.twitter.userList, {"User1", "User2", "User3", "User4"})
            self.twitter.new_create_twitter_account("User5")
            self.assertEqual(self.twitter.userList, {"User1", "User2", "User3", "User4", "User5"})

        def test_notification_page(self):
            self.twitter.tweetle("User1", "Tweet1")
            self.twitter.tweetle("User2", "Tweet2")
            self.twitter.tweetle("User3", "Tweet3")
            self.assertEqual(self.twitter.notification_page("User1"), ["Tweet1", "Tweet2", "Tweet3"])
            self.assertEqual(self.twitter.notification_page("User2"), ["Tweet1", "Tweet2", "Tweet3"])
            self.assertEqual(self.twitter.notification_page("User3"), ["Tweet1", "Tweet2", "Tweet3"])

        def test_message_page(self):
            self.twitter.message_page("User1", "User2", "Message1")
            self.assertEqual(self.twitter.messageList, {"User1": {"User2": ["Message1"]}})
            self.twitter.message_page("User2", "User3", "Message2")
            self.assertEqual(self.twitter.messageList, {"User1": {"User2": ["Message1"]}, "User2": {"User3": ["Message2"]}})
            

        def test_list_page(self):
            self.twitter.list_page("User1", "User2")
            self.assertEqual(self.twitter.followList, {"User1": ["User2"]})
            self.twitter.list_page("User2", "User3")
            self.assertEqual(self.twitter.followList, {"User1": ["User2"], "User2": ["User3"]})

        def test_profile_page(self):
            self.twitter.tweetle("User1", "Tweet1")
            self.twitter.tweetle("User2", "Tweet2")
            self.twitter.tweetle("User3", "Tweet3")
            self.assertEqual(self.twitter.profile_page("User1"), ["Tweet1"])
            self.assertEqual(self.twitter.profile_page("User2"), ["Tweet2"])
            self.assertEqual(self.twitter.profile_page("User3"), ["Tweet3"])


if __name__ == '__main__':  
    unittest.main()



