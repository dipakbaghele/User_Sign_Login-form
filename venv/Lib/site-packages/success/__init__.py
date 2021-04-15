#
# Import Success :-)
#
# Written by Marc-Andre Lemburg <mal@egenix.com> for the PSF Python
# Brochure Project.
#
# (c) 2012 by the Python Software Foundation
#
import webbrowser

### Globals

__version__ = '1.0.0'

URL = 'http://brochure.getpython.info/'

###

def main():
    success = webbrowser.open_new_tab('http://brochure.getpython.info/')
    if success:
        print ("Please have a look at your webbrowser for instant access")
        print ("to Python success ... stories :-)")
    else:
        print ("Success is a key feature of Python. If you'd like to see how ")
        print ("many companies and projects around the world have put Python")
        print ("to successfull use, please visit our success story website")
        print ("at %s" % URL)

### Entry point

main()
