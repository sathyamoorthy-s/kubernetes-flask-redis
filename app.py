from flask import Flask
import redis
import os

app = Flask(__name__)

# Read Redis configuration from environment variables
REDIS_HOST = os.getenv("REDIS_HOST", "redis-service")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))

# Connect to Redis
r = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)


@app.route("/")
def home():
    count = r.incr("visits")

    return f"""
<!DOCTYPE html>
<html>

<head>
    <title>Kubernetes Flask + Redis Application</title>

    <style>

        body {{
            margin: 0;
            padding: 0;
            background: #f4f6f9;
            font-family: Arial, Helvetica, sans-serif;
        }}

        .container {{
            width: 750px;
            margin: 60px auto;
            background: white;
            padding: 35px;
            border-radius: 12px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.12);
        }}

        h1 {{
            color: #0d6efd;
            text-align: center;
            margin-bottom: 10px;
        }}

        h2 {{
            text-align: center;
            color: #555;
            margin-bottom: 25px;
        }}

        hr {{
            border: none;
            border-top: 1px solid #ddd;
            margin-bottom: 30px;
        }}

        .status {{
            background: #eef7ff;
            border-left: 5px solid #0d6efd;
            padding: 15px;
            margin-bottom: 15px;
            font-size: 18px;
        }}

        .counter {{
            background: #eafaf1;
            border-left: 5px solid #28a745;
            padding: 20px;
            margin-top: 30px;
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #28a745;
        }}

        .tech {{
            margin-top: 30px;
            text-align: center;
            color: #666;
            font-size: 15px;
        }}

        .footer {{
            margin-top: 35px;
            text-align: center;
            color: gray;
            font-size: 14px;
        }}

    </style>

</head>

<body>

<div class="container">

<h1>☸️ Kubernetes Flask + Redis Application</h1>

<h2>Production-Ready Deployment on Kubernetes</h2>

<hr>

<div class="status">
<b>Application:</b> Flask Web Application
</div>

<div class="status">
<b>Orchestration:</b> Kubernetes
</div>

<div class="status">
<b>Configuration:</b> ConfigMap & Secret
</div>

<div class="status">
<b>Database:</b> Redis Service Connected ✅
</div>

<div class="counter">
👥 Visitor Count : {count}
</div>

<div class="tech">
Kubernetes • Docker • Flask • Redis • ConfigMap • Secret
</div>

<div class="footer">
Developed by Sathya Moorthy S
</div>

</div>

</body>

</html>
"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)