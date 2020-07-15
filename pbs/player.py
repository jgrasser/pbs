from . import utils
import argparse, json

from html.parser import HTMLParser



# create a subclass and override the handler methods
class VideoDataParser(HTMLParser):
    def handle_data(self, data):
        if self.lasttag == 'script' and 'window.videoBridge' in data:
             for l, line in enumerate(data.split(';')):
                 if 'window.videoBridge' in line:
                     print (line.split('=')[1].lstrip().rstrip(';'))


def list(argv):
   parser = argparse.ArgumentParser(
              usage="pbs.py seasons [-h] --legacy-tp-media-id LEGACY_TP_MEDIA_ID",
              description='Search and play video content from PBS.org')
   
   parser.add_argument('--legacy-tp-media-id', type=str, required=True)

   args = parser.parse_args(argv)
  
   parser = VideoDataParser()

   data = utils.plainclient('GET', f'/portalplayer/{args.legacy_tp_media_id}', host='https://player.pbs.org')

   parser.feed(data)
