from django.core.management.base import BaseCommand

import feedparser
from dateutil import parser

from podcasts.models import Episode

def save_new_episodes(feed):
        podcast_title = feed.channel.title
        podcast_image = feed.channel.image["href"]

        for item in feed.entries:
            if not Episode.objects.filter(puid=item.guid).exists():
                episode = Episode(
                    title=item.title,
                    description=item.description,
                    pub_date=parser.parse(item.published),
                    link=item.link,
                    image=podcast_image,
                    podcast_name=podcast_title,
                    puid=item.guid,
                )
                episode.save()

def commandlineheroes():
    _feed = feedparser.parse("https://feeds.pacific-content.com/commandlineheroes")
    save_new_episodes(_feed)

def ubuntu_podcast():
    _feed = feedparser.parse("https://ubuntupodcast.org/feed/")
    save_new_episodes(_feed)

def linux_for_everyone():
    _feed = feedparser.parse("https://feeds.fireside.fm/linuxforeveryone/rss")
    save_new_episodes(_feed)

def linux_lads():
    _feed = feedparser.parse("https://linuxlads.com/feed_mp3.rss")
    save_new_episodes(_feed)

def linux_cast():
    _feed = feedparser.parse("https://anchor.fm/s/a5967a8/podcast/rss")
    save_new_episodes(_feed)

def linux_unplugged():
    _feed = feedparser.parse("https://feeds.fireside.fm/linuxunplugged/rss")
    save_new_episodes(_feed)

class Command(BaseCommand):
    def handle(self, *args, **options):
        commandlineheroes()
        ubuntu_podcast()
        linux_for_everyone()
        linux_lads()
        linux_cast()
        linux_unplugged()
