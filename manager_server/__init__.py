from flask import Flask
import threading
webapp = Flask(__name__)
memcache_pool = {
    "i-0b2b1fce0022b51ea": None,
    "i-000f2b2f469cf5df4": None,
    "i-041a6b3b01c145be3": None,
    "i-0f1cd99617e4f3656": None,
    "i-06910f22c363f377e": None,
    "i-09839739293389736": None,
    "i-082877449b21341df": None,
    "i-0b4b4d2beb159a395": None
}
from manager_server import backend_client
from manager_server.statistics_server import thread_stats

th = threading.Thread(target=thread_stats)
th.start()
