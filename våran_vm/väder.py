import requests as rq
import rich.traceback

rich.traceback.install()

data = rq.get('https://www.aftonbladet.se/')

# väderinsamlaren