# Complete Setup Guide for AI Video Application

## Introduction
This document serves as a comprehensive guide for setting up and deploying the AI Video application.

## Prerequisites
Before you begin, ensure you have the following installed:
- **Git**: Version control system for tracking changes in your code.
- **Node.js**: A JavaScript runtime used for building scalable applications. Download from [nodejs.org](https://nodejs.org/).
- **npm**: Node package manager to manage your JavaScript libraries. It comes with Node.js by default.
- **Docker**: For containerization of the app.  Get it from [docker.com](https://www.docker.com/).

## Cloning the Repository
First, clone the repository using Git:
```bash
git clone https://github.com/dkoubek284-commits/ai-video-a.git
cd ai-video-a
```

## Setting Up the Environment
1. **Install Dependencies**: Run the following command to install the required npm packages:
   ```bash
   npm install
   ```

2. **Environment Variables**: Create a `.env` file in the root directory of your project. Below is a sample structure:
   ```bash
   touch .env
   ```
   Fill in the variables:
   ```
   DATABASE_URL=mongodb://localhost:27017/myapp
   PORT=3000
   SECRET_KEY=your_secret_key
   ```

## Running the Application Locally
To run the application in development mode:
```bash
npm run dev
```
This will start the server and you can access the application by visiting `http://localhost:3000` in your web browser.

## Docker Setup
To run the application using Docker, follow these steps:
1. Create Docker Image:
   ```bash
   docker build -t ai-video-app .
   ```

2. Run the Docker Container:
   ```bash
   docker run -p 3000:3000 ai-video-app
   ```

## Deployment Instructions
For deployment, follow these steps:
1. **Prepare Build**: Run the command to build your application for production:
   ```bash
   npm run build
   ```

2. **Deploy to Server**: Use your preferred method to deploy the `dist` folder to your server. This could be through FTP, SSH, or a CI/CD pipeline.

3. **Run the Application**: After deploying, start the server on your live environment.
   ```bash
   npm start
   ```

## Troubleshooting
If you encounter issues, consider the following steps:
- Check if all your dependencies are up to date.
- Ensure your environment variables are correctly set.
- Review the application logs for any errors.

## Conclusion
You are now set up to use the AI Video application. For more information, consult the documentation or reach out to the development team.