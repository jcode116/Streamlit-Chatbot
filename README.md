# ChatGPT-powered Streamlit Chatbot

This project is a simple chatbot web application built using **Streamlit** and **OpenAI's ChatGPT** model. The application allows users to interact with an AI assistant via a text input interface. The app is designed to run locally and can be containerized using Docker for consistent deployment across different environments.

## Features
- Chatbot interface powered by OpenAI's GPT-3.5-turbo model
- Interactive web interface built with Streamlit
- Easy deployment using Docker

## Prerequisites
- **Python 3.6+**
- **OpenAI API Key** (Sign up at [OpenAI](https://platform.openai.com/) to get your API key)

---

## Running the App Locally

### 1. Clone the Repository
```bash
git clone https://github.com/jcode116/chatgpt-streamlit-chatbot.git
cd chatgpt-streamlit-chatbot
```
### 2. Set Up a Virtual Environment
Create the virtual environment:
```bash
python3 -m venv venv
```
#### Activate the virtual environment:


On macOS/Linux:
```bash
source myenv/bin/activate
```
On Windows:
```bash
myenv\Scripts\activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Set Up Your OpenAI API Key
To use the OpenAI API, you need to set the OPENAI_API_KEY environment variable.

On macOS/Linux:

```bash
export OPENAI_API_KEY="your_openai_api_key"
```
On Windows (CMD):

Command Prompt (CMD)
``` cmd
set OPENAI_API_KEY=your_openai_api_key
```
### 5. Run the Streamlit App
```bash
streamlit run app.py
```

Once the server starts, open your browser and go to http://localhost:8501 to use the chatbot.

Running the App with Docker
You can containerize the application using Docker for a consistent deployment experience.

### 1. Build the Docker Image
```bash
docker build -t chatgpt-streamlit .
```
### 2. Run the Docker Container
To run the container with the necessary environment variable (OPENAI_API_KEY):

```bash
docker run -p 8501:8501 -e OPENAI_API_KEY="your_openai_api_key" chatgpt-streamlit
```

The application will be accessible at http://localhost:8501.

### Deploying to Azure App Service
Push the Docker Image to a Container Registry:

Tag and push the Docker image to your preferred container registry (e.g., Azure Container Registry or Docker Hub).
```bash
docker tag chatgpt-streamlit <your-registry>/chatgpt-streamlit
docker push <your-registry>/chatgpt-streamlit
```
### Create an Azure App Service:
In the Azure portal, create a new Azure App Service. 

Choose Docker container as the deployment source and select your container registry.
Set Environment Variable in Azure:

Go to Configuration > Application Settings and add OPENAI_API_KEY with your OpenAI API key as the value.
Access the App:

Once deployed, navigate to the URL provided by Azure to use your chatbot.
Project Structure
```bash
├── app.py               # Main application file for Streamlit
├── Dockerfile           # Docker configuration file
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```
### Troubleshooting
#### Error with OpenAI API Key: 
Ensure that the OPENAI_API_KEY environment variable is set correctly.

#### Docker Build Issues: 
Make sure Docker is installed and running, and that you're in the project root directory when running the docker build command.