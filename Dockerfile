# 1. Use a lightweight Python base image
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy your project files into the container
COPY . /app

# 4. Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# 5. Expose the port Streamlit uses
EXPOSE 8501

# 6. Command to boot up the Streamlit server
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]