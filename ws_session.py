
ws_conns = {}

session_id = 0


def add_session(ws):
    global session_id
    session_id += 1
    ws_conns[session_id] = ws
    return session_id


def get_all():
    return ws_conns.values()


def del_session(session_id):
    del ws_conns[session_id]
