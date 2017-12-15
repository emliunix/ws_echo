import time

from aiohttp import web, WSMsgType

from ws_session import add_session, del_session, get_all


async def ws_conn(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    session_id = add_session(ws)
    print("connected[{}] ".format(session_id))
    start_time = time.time()

    exception_exit = False

    async for msg in ws:
        if msg.type == WSMsgType.TEXT:
            if msg.data == "close":
                break
            else:
                await ws.send_str("you sent {}, but I won't do anything."
                                  .format(msg.data))
        elif msg.type == WSMsgType.ERROR:
            print("connection[{}] exception: {}"
                  .format(
                      session_id,
                      ws.exception()
                  ))
    del_session(session_id)
    if not exception_exit:
        await ws.close()
    print("closed[{}] {:.3f}s".format(session_id, time.time()))


async def webhook_input(request):
    """
    :type request: aiohttp.web.Request
    """
    if request.can_read_body:
        content = await request.read()
        data = content.decode("utf-8")
        for ws in get_all():
            await ws.send_str(data)
    return web.Response(text="ok", status=200)
