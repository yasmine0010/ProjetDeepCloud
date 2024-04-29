FROM python:3.11.5

# Upgrade pip 
RUN pip install -U pip

# Install Streamlit
RUN pip install streamlit

# Create a new directory for the app and set it as the working directory
WORKDIR /app

# Copy the application files to the container
COPY . /app

# Copy the model file to the container
COPY efficientnet_model_1_10_classes.h5 /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Expose port 8501
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "myapp.py", "--server.port=8501", "--server.address=0.0.0.0"]
