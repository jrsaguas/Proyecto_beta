from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/info":
            data = {
                "project": "Proyecto_beta",
                "topic": "Inteligencia Artificial Agentiva",
                "date": "2026-09-29",
                "files": ["investigacion_ia_agentiva.md", "informe_ia_agentiva.docx", "comparativa_ia_agentiva.xlsx"]
            }
            body = json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        return super().do_GET()

if __name__ == "__main__":
    import os
    os.chdir(ROOT)
    print("Servidor IA agentiva: http://localhost:8000")
    ThreadingHTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
