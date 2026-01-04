from flask import Flask, render_template, jsonify
import psutil
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Pass the Build ID from the environment variable (set by Jenkins)
    build_id = os.getenv('BUILD_ID', 'Local-Dev')
    return render_template('index.html', build_id=build_id)

@app.route('/metrics')
def metrics():
    # Gather real-time pod metrics
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    
    return jsonify({
        'cpu': cpu_usage,
        'memory_percent': memory_info.percent,
        'memory_used': f"{memory_info.used / (1024 * 1024):.2f} MB"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
