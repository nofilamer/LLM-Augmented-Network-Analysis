# 🔍 AI-Powered Network Analysis Tool

This project is a **Flask-based web application** that provides **real-time network diagnostics** using **system-level network statistics (`netstat -s`)** and **AI-powered insights** from OpenAI's GPT-4. The application collects raw network data, processes it into structured metrics, and analyzes potential **network bottlenecks, congestion issues, and inefficiencies** using **machine learning-driven analysis**.

## ✨ Features

✅ **Web-Based UI** – Easily accessible through a browser.  
✅ **Real-Time Network Statistics** – Uses `netstat -s` to fetch live network data.  
✅ **AI-Powered Insights** – GPT-4 analyzes network conditions and suggests optimizations.  
✅ **Structured Reporting** – Displays both **raw metrics** and **AI-generated diagnostics** in clear tables.  
✅ **Vagrant & Virtualization Support** – Configured to run inside a **Vagrant VM**, accessible from the host.  

## 🚀 How It Works

1️⃣ **User clicks "Run Network Analysis"** on the homepage.  
2️⃣ **Flask triggers network data collection** via `netstat -s`.  
3️⃣ **Data is cleaned & structured** for processing.  
4️⃣ **GPT-4 analyzes the metrics** and identifies potential issues.  
5️⃣ **Results are displayed in an easy-to-read table format**.  

## 🛠️ Technologies Used

- **Python** (Flask, OpenAI API, Pandas)  
- **HTML, CSS** (for frontend display)  
- **System Networking Commands** (`netstat -s`)  
- **Vagrant** (for virtualization & port forwarding)  

## 📂 Project Structure
/network-analysis-app ├── app.py # Main Flask application ├── templates/ │ ├── index.html # Homepage with "Run Analysis" button │ ├── results.html # Displays network metrics & AI insights └── Vagrantfile # Configures VM for running the app


python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

Flask==3.0.0
openai==1.2.3
pandas==2.2.0
python-dotenv==1.0.0

export OPENAI_API_KEY="your-api-key-here"  # Linux/macOS
setx OPENAI_API_KEY "your-api-key-here"    # Windows

python app.py

📈 Use Case Scenarios
✔️ Network Engineers – Diagnose slow network performance.
✔️ DevOps & IT Teams – Monitor and troubleshoot connectivity issues.
✔️ Cybersecurity Analysts – Detect abnormal TCP behaviors.

📝 Contributing
We welcome contributions! If you'd like to fix a bug, add a feature, or improve documentation, feel free to fork this repository, make your changes, and submit a pull request. 🚀

📜 License
This project is open-source under the MIT License.

📧 Contact
For any questions or feedback, feel free to reach out:

📩 Your Email: [amernofil@gmail.com]
🌐 GitHub: https://github.com/nofilamer/network-analysis-tool
