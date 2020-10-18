import rest
import sys, json

from html.parser import HTMLParser
from io import StringIO


# create a subclass and override the handler methods
class VideoDataParser(HTMLParser):
    def handle_data(self, data):
        if self.lasttag == 'script' and 'window.videoBridge' in data:
             for l, line in enumerate(data.split(';')):
                 if 'window.videoBridge' in line:
                     print (line.split('=')[1].lstrip().rstrip(';'))


def portalplayer(legacy_tp_media_id):
   
   parser = VideoDataParser()

   status, data = rest.client('GET', f'/portalplayer/{legacy_tp_media_id}', host='https://player.pbs.org')

   # Setup the io redirection to variable. Note: this is not thread safe, but
   # that is alright, because this is intended to be invoked in a single,
   # threaded script.
   old_stdout = sys.stdout
   sys.stdout = o = StringIO()

   # Feed the portalplayer html through the html parser.
   parser.feed(data)

   # Restore the old stdout
   sys.stdout = old_stdout

   return o.getvalue()
