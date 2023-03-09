from flask import Flask
import threading
webapp = Flask(__name__)
memcache_pool = {
    "i-0b2b1fce0022b51ea": None,
    "i-0303f5a7fd081629c": None,
    "i-058c4a6353bd7f1d4": None,
    "i-018c73777fc91954d": None,
    "i-044829f7150c411df": None,
    "i-09396032b888b6010": None,
    "i-03ae457601a8f502d": None,
    "i-049ec293fa03cdd3c": None
}
from manager_server import backend_client
from manager_server.statistics_server import thread_stats

th = threading.Thread(target=thread_stats)
th.start()
