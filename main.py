
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import geocoder
from nearest import get
import requests
import beautifulsoup4
class lol(Gtk.Window):
    def __init__(self):
# thingy for buttons
        lol = Gtk.Box(spacing=6)
self.add(lol) # AND THIS TOO
# is it bad i got that from the example aaaaaa idk how to gui programming
switcht = Gtk.Button.new_with_label("Nearest McDonald's") # ok i had to look at example aaaaaa
switcht.connect("clicked", self.nearest) # frick idk how to gui so yeah i had to l ook at exampleand thanks example
def nearest():
# TODO: add code for finder    
    nearest.get()
# get app
maccas = requests.get("https://www.mcdonalds.com/us/en-us.html")
# get request to the mcdonalds website
headline = maccas.find(id="headline-text") # yes thanks so
# get headlines using beautifulsoup
description = maccas.find(id="headline-description")
# and the thing for the asterisks
asterisk = maccas.find(id="legal-text")
# check if we find headline
if headline:
       xd = Gtk.Label()
showheadline = xd.setmarkup("<big>" + headline + "</big>")
showdescription = xd.set_text(description)
showthingsidkwhy = xd.set_title(asterisk)

