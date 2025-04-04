# Python Task

This project enables running Python tasks using Docker containers.

## Prerequisites  

- [Docker](https://www.docker.com/)  
- [Docker Compose](https://docs.docker.com/compose/)  

## Setup Instructions  

### 1. Clone the Repository  

Clone the repository from GitHub:  
```bash
git clone https://github.com/minitaste/python-task.git
```
Navigate to the project directory:  
```bash
cd python-task
```

### 2. Build Docker Images  

Run the following command to build the images:  
```bash
docker-compose build
```

### 3. Configure Docker Network and Volumes  

Create a network for Docker containers:  
```bash
docker network create python_task
```
Create a volume for PostgreSQL data storage:  
```bash
docker volume create postgres-data
```

### 4. Start Docker Containers  

Start the container(s) using Docker Compose:  
```bash
docker-compose up -d
```

### 5. Interacting with the Python Application  

Check running containers:  
```bash
docker ps
```
Identify the container ID for the Python application and access it:  
```bash
docker exec -it <id> bash
```

### 6. Database Migrations  

Run the following commands inside the container:  

Create migrations:  
```bash
python manage.py makemigrations
```
Apply migrations:  
```bash
python manage.py migrate
```

### 7. Run Tests  

Execute tests using:  
```bash
pytest
```

## Additional Information  

Ensure that all required dependencies are installed and that your Docker environment meets the necessary requirements. For more details, refer to the project documentation.
