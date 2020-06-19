import datetime
from requests_html import HTMLSession
from termcolor import colored

# define url
url = 'https://www.sonnetstore.com/products/egfx-breakaway-puck-560?variant=2553178062882'

# fetch page
session = HTMLSession()
r = session.get(url)
r.html.render()

# get key content
elem = r.html.find('#AddToCartText', first=True)
kmsg = elem.text

# identify
if kmsg.upper() == 'ADD TO CART':
    is_ok = True
else:
    is_ok = False

# output
color_fg = 'white' if is_ok else 'red'
color_bg = 'on_green' if is_ok else 'on_grey'
colored_msg = colored(kmsg, color_fg, color_bg)

now = datetime.datetime.today().strftime('%H:%M:%S')
print('* %s: Sonnet eGFX Breakway Puck RX 560 is %s' % (now, colored_msg))

