import os
import json
import time
from datetime import datetime, timezone
import requests
from flask import Flask, request, jsonify, Response, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder=".")
CORS(app)

STATE_FILE = os.path.join(os.path.dirname(__file__), "ispr_local_cache.json")
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ISPR-Media-Monitor/2.0"
}

@app.route("/")
def serve_index():
    return send_from_directory(".", "index.html")

@app.route("/<path:AssetPath>")
def serve_static_files(AssetPath):
    if os.path.exists(os.path.join(".", AssetPath)):
        return send_from_directory(".", AssetPath)
    return send_from_directory(".", "index.html")

@app.route("/api/health", methods=["GET"])
def api_health():
    return jsonify({
        "status": "operational",
        "service": "ISPR News Monitoring System C2 Backend",
        "timestamp": datetime.now(timezone.utc).isoformat()
    })

@app.route("/api/rss", methods=["GET"])
def api_rss_proxy():
    feed_url = request.args.get("url", "").strip()
    if not feed_url:
        return jsonify({"error": "Missing url parameter"}), 400
    try:
        resp = requests.get(feed_url, headers=HEADERS, timeout=8)
        return Response(
            resp.content,
            status=resp.status_code,
            content_type="application/xml; charset=utf-8"
        )
    except Exception as exc:
        return jsonify({"error": str(exc)}), 502

@app.route("/api/state", methods=["GET", "POST"])
def api_system_state():
    if request.method == "POST":
        data = request.get_json(silent=True) or {}
        try:
            with open(STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return jsonify({"saved": True})
        except Exception as exc:
            return jsonify({"saved": False, "error": str(exc)}), 500
    else:
        if os.path.exists(STATE_FILE):
            try:
                with open(STATE_FILE, "r", encoding="utf-8") as f:
                    return jsonify(json.load(f))
            except Exception:
                pass
        return jsonify({"status": "empty"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Starting ISPR News Monitoring System on http://127.0.0.1:{port}")
    app.run(host="0.0.0.0", port=port, debug=False)