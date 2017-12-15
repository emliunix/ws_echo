from os.path import dirname, join
from aiohttp import web

from handlers import webhook_input, ws_conn


def setup_routes(app):
    """
    :type app: aiohttp.web.Application
    """
    app.router.add_post('/input', webhook_input)
    app.router.add_get("/hello", lambda req: web.Response(text="Hello"))
    app.router.add_get('/ws', ws_conn)
    app.router.add_static('/static/', join(dirname(__file__), "static"))


app = web.Application()
setup_routes(app)
web.run_app(app, host="0.0.0.0", port=23333)
