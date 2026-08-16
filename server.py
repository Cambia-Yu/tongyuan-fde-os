#!/usr/bin/env python3
"""FDE OS 文档查看器（只读）。

用法：
    python3 server.py            # 默认 http://127.0.0.1:8795
    python3 server.py --port 8800

仅提供两类服务：
  1. 静态文件：index.html / marked.min.js
  2. JSON API：/api/files（.md 清单）、/api/content?path=（指定 .md 原文）

不写入、不修改任何 .md 文件；路径解析限制在本目录内。
"""
import argparse
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

ROOT = os.path.dirname(os.path.abspath(__file__))
REAL_ROOT = os.path.realpath(ROOT)
STATIC_WHITELIST = {"", "index.html", "marked.min.js"}


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def _send(self, code, body, ctype):
        data = body if isinstance(body, bytes) else body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def _json(self, obj, code=200):
        self._send(code, json.dumps(obj, ensure_ascii=False), "application/json; charset=utf-8")

    def do_GET(self):
        parsed = urlparse(self.path)
        route = parsed.path

        if route in ("/", "/index.html", "/marked.min.js"):
            name = "index.html" if route in ("/", "/index.html") else "marked.min.js"
            try:
                with open(os.path.join(ROOT, name), "rb") as f:
                    ctype = "text/html; charset=utf-8" if name.endswith(".html") else "application/javascript; charset=utf-8"
                    return self._send(200, f.read(), ctype)
            except OSError:
                return self._send(404, "missing " + name, "text/plain; charset=utf-8")

        if route == "/api/files":
            files, dirs = [], set()
            for dirpath, dirnames, filenames in os.walk(ROOT):
                dirnames[:] = [d for d in dirnames if not d.startswith(".") and d != "node_modules"]
                rel = os.path.relpath(dirpath, ROOT)
                dirs.add(rel)
                for fn in filenames:
                    if fn.endswith(".md"):
                        p = os.path.join(dirpath, fn)
                        files.append(
                            {
                                "path": os.path.relpath(p, ROOT),
                                "size": os.path.getsize(p),
                                "mtime": int(os.path.getmtime(p)),
                            }
                        )
            files.sort(key=lambda x: x["path"])
            return self._json({"files": files, "dirs": sorted(dirs)})

        if route == "/api/content":
            q = parse_qs(parsed.query).get("path", [""])[0]
            full = os.path.realpath(os.path.join(ROOT, q))
            if (
                not full.startswith(REAL_ROOT + os.sep)
                or not full.endswith(".md")
                or not os.path.isfile(full)
            ):
                return self._json({"error": "not found"}, 404)
            with open(full, encoding="utf-8") as f:
                text = f.read()
            return self._json({"path": q, "content": text})

        return self._send(404, "not found", "text/plain; charset=utf-8")

    def log_message(self, fmt, *args):
        pass  # 静默访问日志


def main():
    ap = argparse.ArgumentParser(description="FDE OS 只读文档查看器")
    ap.add_argument("--port", type=int, default=8795)
    ap.add_argument("--host", default="127.0.0.1")
    args = ap.parse_args()
    srv = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"FDE OS 查看器：http://{args.host}:{args.port}  （目录 {ROOT}，只读）")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\n已停止")


if __name__ == "__main__":
    main()
