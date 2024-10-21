# FrontEndcoders

Welcome to the **FrontEndcoders** repository! This project serves as a simple web app frontend for my thesis project, showcasing the capabilities of the custom-built **EncoderHubCore** library. 🚀

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Running the API](#running-the-api)

## Features
- **Dynamically interchangeable components**
- **Modular encoding models**
- **Easy configuration for different use cases**
- **User-friendly interface for encoding operations**

## Installation

To run this application locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/FrontEndcoders.git
   cd FrontEndcoders
   ```

2. **Create a `.env` file:**
   Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
   Update the `.env` file with your configuration settings.

3. **Build and run the Docker container:**
   Use the provided scripts to build and run the application:
   ```bash
   ./docker_build.sh
   ./docker_run.sh
   ```

## Usage

Once the application is running, you can access it via your web browser. You will be able to select encoding models and encode messages through a user-friendly interface.

### Encoding Messages
1. Select an encoder from the dropdown menu.
2. Enter your message in the text area.
3. Click on "Encode" to see the encoded message.

### Viewing Encoding History
You can view your previous encodings in the "Encoding History" section, where you can also clear your history if needed.

## Running the API

This application relies on the **RestfulEncoders** API, which must be running for full functionality. You can find it here: [RestfulEncoders](https://github.com/nahu02/RestfulEncoders). Follow its README for setup instructions.