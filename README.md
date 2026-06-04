# 🛡️ Enterprise GenAI Compliance Agent

**Live Demo:** https://enterprise-compliance-agent.onrender.com

An end-to-end Enterprise AI application designed to automate the ingestion and analysis of dense UK regulatory documents. By leveraging Meta's Llama 3.1 architecture via the Groq LPU inference engine, this tool surgically extracts legal risks, operational obligations, and breach penalties from raw PDFs without hallucination.

### 🏗️ Architecture & Tech Stack
* **AI/Inference:** Groq API, Meta Llama-3.1-8b-instant (Temperature set to 0.1 for strict deterministic output).
* **Ingestion Engine:** PyPDF (Parses unstructured PDF layouts into readable AI context).
* **Frontend UI:** Streamlit with custom CSS injection (Glassmorphism, dark-mode OS aesthetics).
* **Cloud Infrastructure:** Docker, Render (Fully containerized for continuous deployment).

### ✨ Core Features
* **Zero-Touch Ingestion:** Drag-and-drop interface for processing multi-page regulatory PDFs.
* **Targeted Context Extraction:** Filters insights based on targeted commercial needs (e.g., High-Risk Liabilities vs. Executive Summaries).
* **High-Speed Inference:** Bypasses traditional compute bottlenecks by routing prompts through Groq's specialized LPU hardware.
* **Stateless Security:** Processes documents in memory without saving sensitive corporate data to a database.

### 🚀 How to Run Locally using Docker

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YourUsername/compliance-agent.git](https://github.com/YourUsername/compliance-agent.git)
   cd compliance-agent

2. Set up your environment variables:
Create a .env file in the root directory and add your Groq API key:

Code snippet
GROQ_API_KEY=gsk_your_api_key_here

3. Build and Run the Docker Container:

Bash
docker build -t compliance-agent .
docker run -p 8501:8501 --env-file .env compliance-agent

4. Access the Application:
Open your browser and navigate to http://localhost:8501


### Step 2: Push it to GitHub
Save the file, open your VS Code terminal, and run these three commands to send it up to your repository:

```powershell
git add README.md
git commit -m "Add project documentation"
git push