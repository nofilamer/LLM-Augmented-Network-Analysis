from flask import Flask, jsonify, render_template
import subprocess
import openai
import os
import re

# Initialize Flask app
app = Flask(__name__)

# Initialize OpenAI client (ensure API key is set in environment variables)
client = openai.OpenAI()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_netstat_data():
    """Runs 'netstat -s' and captures key network statistics."""
    try:
        result = subprocess.run(["netstat", "-s"], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error running netstat: {e}"

def parse_netstat_output(output):
    """Extracts relevant TCP and IP statistics from netstat output."""
    metrics = []
    capture = False
    for line in output.split("\n"):
        line = line.strip()
        if line.startswith("TcpExt:") or line.startswith("IpExt:"):
            capture = True
            continue
        if capture and line:
            parts = line.split(":")
            if len(parts) == 2:
                key = parts[0].strip()
                value = parts[1].strip()
                if value.isdigit():
                    metrics.append({"Metric": key, "Value": int(value)})
    
    return metrics

def analyze_with_openai(metrics):
    """Sends parsed network metrics to OpenAI API for analysis and returns structured data."""
    
    prompt = (
        "Analyze the following network statistics and identify potential bottlenecks, "
        "congestion issues, and system resource shortages that could cause retransmissions, "
        "packet loss, or TCP inefficiencies.\n\n"
        "Provide the response in this format:\n"
        "- **Issue Name: <Issue>**\n"
        "  Explanation: <Detailed Explanation>\n\n"
        "Metrics:\n" + "\n".join(f"{item['Metric']}: {item['Value']}" for item in metrics)
    )

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a network diagnostic expert."},
            {"role": "user", "content": prompt}
        ]
    )

    response_text = response.choices[0].message.content

    # Print raw response for debugging
    print("\n=== Raw OpenAI Response ===\n", response_text)

    # Extract structured issues
    formatted_rows = []
    lines = response_text.split("\n")

    current_issue = None
    current_explanation = ""

    for line in lines:
        line = line.strip()

        # Identify issue names
        if line.startswith("- **Issue Name:"):
            if current_issue and current_explanation:
                formatted_rows.append({"Metric": current_issue, "Analysis": current_explanation.strip()})

            current_issue = line.replace("- **Issue Name:", "").replace("**", "").strip()
            current_explanation = ""

        elif line.startswith("Explanation:"):
            current_explanation = line.replace("Explanation:", "").strip()

        elif current_issue:
            current_explanation += " " + line  # Append multi-line explanations

    # Add last captured issue
    if current_issue and current_explanation:
        formatted_rows.append({"Metric": current_issue, "Analysis": current_explanation.strip()})

    return formatted_rows

@app.route("/")
def index():
    """Render the HTML dashboard."""
    return render_template("index.html")

@app.route("/analyze")
def analyze():
    """API endpoint to get network statistics and analyze them."""
    netstat_output = get_netstat_data()
    metrics = parse_netstat_output(netstat_output)

    if not metrics:
        return jsonify({"error": "No network metrics found"}), 400

    analysis_results = analyze_with_openai(metrics)

    return render_template("results.html", metrics=metrics, analysis=analysis_results)

# Run the app on all interfaces to support Vagrant port forwarding
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

