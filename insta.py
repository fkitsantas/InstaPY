""" InstaPY by KITSANTAS FOTIOS (Frozen) & Nightmare.gr v0.1
    Using the InstaPy API - Library from Tim Großmann (https://github.com/timgrossmann/InstaPy)
    Hosted at: https://projects.nightmare.gr/instapy/ && https://github.com/FrozGR/InstaPY
    Contact me at frozen [at] nightmare.gr via email - or - DM @ https://instagram.com/frozgr
"""
import os
import time
import random
from tempfile import gettempdir
from selenium.common.exceptions import NoSuchElementException
from instapy import InstaPy
from instapy import smart_run

# # # # # # # # # # # # # # # # # # # # # # # # # # #
#                   <Settings>                      #
# # # # # # # # # # # # # # # # # # # # # # # # # # #

# Instagram Login Credentials
insta_username = 'your-Instagram-Username'
insta_password = 'your-Instagram-Password'

#### General Bot Settings
# Limit of Follows
follow_ammount_number = 250

# Follow by Tags
follow_by_tags_list = ['bodybuilding', 'fitness', 'physique', 'freemasonry', 'freemasons']

# Array List of comments to be used on posts.
comments = ['@{}', 'δυνατό πολύ', ':bowtie:', ':star2:', 'black_heart', ':fire:', ':muscle:', ':wine_glass:', ':heart:', ':100:', ':ok_hand:', ':top:', ':heavy_check_mark:']

# Array List of Hashtags that the bot will check in order to find other people's posts and like them.
hashtags_to_like_list = ['athlete', 'fitness', 'gym', 'workout', 'fit', 'training', 'bodybuilding', 'fitfam', 'fitgirl',
                    'fitnessmotivation', 'lifestyle', 'muscle', 'strength', 'sport', 'gymlife', 'gains', 'instagood',
                    'fitspo', 'healthylifestyle', 'powerlifting', 'yoga', 'healthy', 'strong', 'fitnessgoals', 'fitnessmodel', 'freemasonry', 'freemasons']

# Array List of hashtags to Ignore. Used to prevent posts that contain some plantbased meat from being skipped.
ignore_list = ['boy', 'girl', 'kid', 'kids']

# Array List of Instagram Users with similar content to yours that you want to follow their followers in order to get followbacks.
accounts_to_find_followers = ['mrolympiallc', 'unitedgrandlodgeofengland']

# Array List of friends to Whitelist. It will prevent autocommenting on and unfollowing those friends no matter if they do not follow you back. (the images will still be liked).
whitelisted_users = ['frozgr', 'friend2', 'friend3']

# Array List of Hashtags NOT to like. Will skip the picture if one of those are included on the picture's hashtags.
dont_likes = ['sex','nude','naked','beef','pork','seafood',
            'egg','chicken','cheese','sausage','lobster',
            'fisch','schwein','lamm','rind','kuh','meeresfrüchte',
            'schaf','ziege','hummer','yoghurt','joghurt','dairy',
            'meal','food','eat','pancake','cake','dessert',
            'protein','essen','mahl','breakfast','lunch',
            'dinner','turkey','truthahn','plate','bacon',
            'sushi','burger','salmon','shrimp','steak',
            'schnitzel','goat','oxtail','mayo','fur','leather',
            'cream','hunt','gun','shoot','slaughter','pussy',
            'breakfast','dinner','lunch']

# Smart Hashtags
# Enable / Disable likes by Smart hashtags with the use of True or False.
smarthashtags = False
# Array List of Smart Hashtags to use.
smarthashtags_list = ['bodybuilding', 'physique', 'freemasonry', 'freemasons']

#Smart Location Hashtags
#Generate smart hashtags based on https://displaypurposes.com/map ranking. Banned and spammy tags are filtered out.
# Enable / Disable likes by Smart Location hashtags with the use of True or False.
smartlocationhashtags = False
# Array List of Smart Location Hashtags
smart_locations = ['213385402/london-united-kingdom', 'c877119/thessaloniki-greece']

#Quota Supervisor - Sleep After Actions
sleep_after_list = ["comments_d", "follows", "unfollows", "server_calls_h"]

# Skip account by BIO
# Enable / Disable skipping a user by checking his Bio for keywords, with the use of True or False.
skip_bioz=True
# Array List of Keywords or phrases to look on a user's bio in order to skip him.
skip_bio_keywords = ['free shipping', 'visa', 'paypal']

# View User Stories
# Enable / Disable automatic view of user stories with the use of True or False.
view_stories=True

# Watch stories by Tags
story_by_tags_list = ['bodybuilding', 'fitness', 'freemasonry', 'freemasons']

# Watch stories from users
# Enable / Disable automatic view of user stories for specific users with the use of True or False.
story_by_users_status=True
# Array List of Users to watch their stories automatically.
story_by_users_list = ['mrolympiallc', 'unitedgrandlodgeofengland']

# # # # # # # # # # # # # # # # # # # # # # # # # # #
#                   </Settings>                     #
# # # # # # # # # # # # # # # # # # # # # # # # # # #



#############################################################################################################################################################
# DO NOT EDIT BELOW THIS LINE UNLESS YOU ARE A CODE MONKEY.                                                                                                 #
#############################################################################################################################################################

# Emoji / Comments to be combined as random pairs.
combined_comment = [random.choice(comments) + random.choice(comments)]

# Get an InstaPy session.
session = InstaPy(username=insta_username,
                  password=insta_password,
                  bypass_security_challenge_using='sms',
                  headless_browser=True,
                  multi_logs=True)

try:
    with smart_run(session):
        session.login()

    
        # Basic Session Settings
        session.set_relationship_bounds(enabled=True,
                    potency_ratio=-0.40,
                    delimit_by_numbers=True,
                    max_followers=60000,
                        max_following=2500,
                        min_followers=30,
                        min_following=30)
        session.set_do_comment(True, percentage=25)
        session.set_comments(comments)
        session.set_do_like(enabled=True, percentage=100)
        session.set_dont_include(whitelisted_users)
        session.set_dont_like(dont_likes)
        session.set_quota_supervisor(enabled=True, sleep_after=sleep_after_list, sleepyhead=True, stochastic_flow=True, notify_me=True,
                                    peak_likes_hourly=57,
                                    peak_likes_daily=585,
                                    peak_comments_hourly=21,
                                    peak_comments_daily=182,
                                    peak_follows_hourly=48,
                                    peak_follows_daily=None,
                                    peak_unfollows_hourly=35,
                                    peak_unfollows_daily=402,
                                    peak_server_calls_hourly=None,
                                    peak_server_calls_daily=4700)

        # Bot Actions
        session.set_user_interact(amount=2, randomize=True, percentage=30, media='Photo')
        session.like_by_tags(random.sample(hashtags_to_like_list, 3), amount=random.randint(50, 100), interact=True)
        
        if smarthashtags:
            session.set_smart_hashtags(smarthashtags_list, limit=3, sort='top', log_tags=True)
            session.like_by_tags(amount=10, use_smart_hashtags=True)

        if smartlocationhashtags:
            session.set_smart_location_hashtags(smart_locations, radius=20, limit=10)
            session.like_by_tags(amount=10, use_smart_location_hashtags=True)

        if skip_bioz:
            session.set_skip_users(skip_bio_keywords)
        
        if view_stories:
            session.set_do_story(enabled = True, percentage = 70, simulate = True)
            session.story_by_tags(story_by_tags_list)
            if story_by_users_status:
                session.story_by_users(story_by_users_list)
        
        # Unfollow Activity
        session.unfollow_users(amount=random.randint(50,150), nonFollowers=True, style="RANDOM", unfollow_after=42 * 60 * 60, sleep_delay=601)

        # Follow Activity - Massive Follow of followers from Instagram Users with similar content to yours.
        session.follow_user_followers(accounts_to_find_followers, amount=follow_ammount_number, randomize=False, interact=True, sleep_delay=240)

        # First step of Unfollow Action - Unfollow non follower users
        session.unfollow_users(amount=random.randint(50,150), instapy_followed_enabled=True, instapy_followed_param="all", style="FIFO", unfollow_after=48*60*60, sleep_delay=601)

        # Second step of Massive Follow of followers from Instagram Users with similar content to yours.
        session.follow_user_followers(accounts_to_find_followers, amount=follow_ammount_number, randomize=False, interact=False, sleep_delay=240)

        # Second step of Unfollow action - Unfollow non follower users.
        session.unfollow_users(amount=500, instapy_followed_enabled=True, instapy_followed_param="all", style="FIFO", unfollow_after=12 * 60 * 60, sleep_delay=601)

        # Last step of Follow Activity - Follow by Tags
        session.follow_by_tags(follow_by_tags_list, amount=10)

        ## Clean all followed users - Unfollow all users followed by InstaPy.
        session.unfollow_users(amount=500, instapy_followed_enabled=True, instapy_followed_param="all", style="FIFO", unfollow_after=24 * 60 * 60, sleep_delay=601)

        # Joining Engagement Pods.
        session.join_pods(topic='sports', engagement_mode='light')

except Exception as exc:
    # if changes to IG layout, upload the file to help us locate the change
    if isinstance(exc, NoSuchElementException):
        file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
        with open(file_path, 'wb') as fp:
            fp.write(session.browser.page_source.encode('utf8'))
        print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
            '*' * 70, file_path))
    # full stacktrace when raising Github issue
    raise

finally:
    # End the Bot session
    session.end()
    t = time.localtime()
    current_time = time.strftime("%d/%m/%Y-%H:%M:%S", t)
    print("("+current_time+") " +"InstaPY by Nightmare.gr execution complete.")