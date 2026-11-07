"""Send commands to the Blender MCP add-on socket (localhost:9876).
Usage: python bl.py info | python bl.py run script.py"""
import json, socket, sys

def send(cmd_type, params=None, host="localhost", port=9876):
    with socket.create_connection((host, port), timeout=120) as s:
        s.sendall(json.dumps({"type": cmd_type, "params": params or {}}).encode())
        buf = b""
        while True:
            chunk = s.recv(65536)
            if not chunk:
                break
            buf += chunk
            try:
                return json.loads(buf.decode())
            except ValueError:
                continue
    return json.loads(buf.decode())

if __name__ == "__main__":
    if sys.argv[1] == "info":
        print(json.dumps(send("get_scene_info"), indent=2))
    elif sys.argv[1] == "run":
        print(json.dumps(send("execute_code", {"code": open(sys.argv[2], encoding="utf-8").read()}), indent=2))
