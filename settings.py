AUTHOR = 'Kyle Fuller'
SITENAME = 'Kyle Fuller'
SITEURL = 'http://kylefuller.co.uk'

THEME = 'theme'

from collections import namedtuple
Project = namedtuple('Project', ('name', 'url', 'description'))

PROJECTS = (
    Project('ZNC', url='http://znc.in/', description='An IRC bouncer with modules & scripts support.'),
    Project('Textual', url='http://textualapp.com/', description='Textual is a lightweight IRC client created specifically for Mac OS X.'),
    Project('zokket', url='https://github.com/kylef/zokket', description='An asynchronous socket networking library for python'),
    Project('PyPPP', url='http://readthedocs.org/docs/pyppp/en/latest/', description='A python implementation of Perfect Paper Passwords a single-use passcode system for multifactor authentication.'),
    Project('lithium', url='http://readthedocs.org/docs/lithium/en/latest/', description='A set of applications for writing a Django website\'s, it includes a blog, a wiki, and many other useful applications.'),
    Project('rivr', url='https://github.com/kylef/rivr', description='A python micro web-framework'),
)

TIMEZONE = 'Europe/London'
DISQUS_SITENAME = 'kylefuller'

DEFAULT_PAGINATION = 5

RELATIVE_URLS = False

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

FEED_RSS = 'posts/feed/latest'
