#!/usr/bin/env python3
"""
Simple Python Script for Jenkins CI/CD Demo - Browser Output
"""
import http.server
import socketserver
from datetime import datetime
import webbrowser
import threading
import time
import sys

def main():
    """Main function that runs the script and returns results"""
    results = []
    
    try:
        results.append("🚀 Jenkins CI/CD Pipeline Started!")
        results.append(f"📅 Current date and time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        results.append("✅ Script executed successfully!")
        results.append("📧 This output will be sent via email")
        
        # Perform some simple operations
        numbers = [1, 2, 3, 4, 5]
        total = sum(numbers)
        results.append(f"🧮 Sum of numbers {numbers} is: {total}")
        
        # Additional demo operations
        results.append("")
        results.append("📊 Additional Operations:")
        results.append(f"📈 Average: {total / len(numbers)}")
        results.append(f"📉 Min: {min(numbers)}, Max: {max(numbers)}")
        results.append(f"🔢 Count: {len(numbers)}")
        
        status = "SUCCESS"
        return results, status
        
    except Exception as e:
        results.append(f"❌ Error occurred: {e}")
        status = "FAILED"
        return results, status

class JenkinsDemoHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            # Run the main function and get results
            results, status = main()
            
            # Generate status-based styling
            if status == "SUCCESS":
                status_color = "#00b894"
                status_bg = "#d1f2eb"
                border_color = "#00b894"
            else:
                status_color = "#e17055"
                status_bg = "#fadbd8"
                border_color = "#e17055"
            
            # Create HTML output
            results_html = ""
            for result in results:
                if result.strip():  # Skip empty lines
                    results_html += f'<div class="output-line">{result}</div>'
                else:
                    results_html += '<div class="spacer"></div>'
            
            html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jenkins CI/CD Demo Output</title>
    <style>
        body {{
            font-family: 'Courier New', monospace;
            background: linear-gradient(135deg, #2d3436 0%, #636e72 100%);
            margin: 0;
            padding: 20px;
            min-height: 100vh;
            color: #2d3436;
        }}
        .container {{
            max-width: 900px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%);
            color: white;
            padding: 25px;
            text-align: center;
        }}
        .header h1 {{
            margin: 0;
            font-size: 2.2em;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }}
        .status-bar {{
            background: {status_bg};
            color: {status_color};
            padding: 15px 25px;
            border-left: 5px solid {border_color};
            font-weight: bold;
            font-size: 1.1em;
        }}
        .output-container {{
            background: #2d3436;
            color: #ddd;
            padding: 25px;
            font-family: 'Courier New', monospace;
            line-height: 1.6;
        }}
        .output-line {{
            padding: 5px 0;
            border-left: 3px solid transparent;
            padding-left: 15px;
            transition: all 0.3s ease;
        }}
        .output-line:hover {{
            background: rgba(116, 185, 255, 0.1);
            border-left-color: #74b9ff;
        }}
        .spacer {{
            height: 10px;
        }}
        .footer {{
            background: #f8f9fa;
            padding: 20px 25px;
            text-align: center;
            color: #636e72;
        }}
        .refresh-btn {{
            background: linear-gradient(45deg, #74b9ff, #0984e3);
            color: white;
            border: none;
            padding: 12px 25px;
            border-radius: 25px;
            font-size: 1em;
            cursor: pointer;
            margin: 0 10px;
            transition: transform 0.3s ease;
        }}
        .refresh-btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        }}
        .timestamp {{
            font-size: 0.9em;
            color: #636e72;
            margin-top: 15px;
        }}
        .jenkins-icon {{
            font-size: 1.5em;
            margin-right: 10px;
        }}
        .auto-refresh {{
            background: #00b894;
        }}
    </style>
    <script>
        let autoRefreshEnabled = false;
        let refreshInterval;
        
        function toggleAutoRefresh() {{
            const btn = document.getElementById('autoRefreshBtn');
            if (autoRefreshEnabled) {{
                clearInterval(refreshInterval);
                autoRefreshEnabled = false;
                btn.textContent = '▶️ Start Auto Refresh';
                btn.className = 'refresh-btn';
            }} else {{
                refreshInterval = setInterval(() => {{
                    location.reload();
                }}, 5000);
                autoRefreshEnabled = true;
                btn.textContent = '⏸️ Stop Auto Refresh';
                btn.className = 'refresh-btn auto-refresh';
            }}
        }}
        
        function manualRefresh() {{
            location.reload();
        }}
    </script>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1><span class="jenkins-icon">🔧</span>Jenkins CI/CD Demo</h1>
        </div>
        
        <div class="status-bar">
            Build Status: {status} ✨
        </div>
        
        <div class="output-container">
            <div style="color: #74b9ff; font-weight: bold; margin-bottom: 15px;">
                📋 Build Output:
            </div>
            {results_html}
        </div>
        
        <div class="footer">
            <button class="refresh-btn" onclick="manualRefresh()">🔄 Refresh Now</button>
            <button class="refresh-btn" id="autoRefreshBtn" onclick="toggleAutoRefresh()">▶️ Start Auto Refresh</button>
            <div class="timestamp">
                Last executed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            </div>
        </div>
    </div>
</body>
</html>
            """
            
            self.wfile.write(html_content.encode())
        else:
            self.send_error(404)

def open_browser():
    """Open browser after a short delay"""
    time.sleep(1.5)  # Wait for server to start
    webbrowser.open('http://localhost:8000')

def start_server():
    """Start the HTTP server"""
    PORT = 8000
    
    print("🚀 Starting Jenkins CI/CD Demo Server...")
    print(f"📱 Server will start at: http://localhost:{PORT}")
    print("⏹️  Press Ctrl+C to stop the server")
    
    # Start browser in a separate thread
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    # Start the server
    try:
        with socketserver.TCPServer(("", PORT), JenkinsDemoHandler) as httpd:
            print(f"✅ Server running on port {PORT}")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 Server stopped. Goodbye!")
        return 0
    except OSError as e:
        if e.errno == 98:  # Address already in use
            print(f"❌ Port {PORT} is already in use. Please try a different port.")
            return 1
        else:
            print(f"❌ Error starting server: {e}")
            return 1

if __name__ == "__main__":
    try:
        sys.exit(start_server())
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        sys.exit(1)
