# Chicagoland Mesh MeshCore Utilities

A web application for generating MeshCore repeater configurations and sending canned serial USB commands to connected devices.

Regionalized for Chicagoland Mesh from the original [Colorado Mesh MeshCore Utilities](https://github.com/Colorado-Mesh) project.

## Running with Docker

### Build the Docker image:
```bash
docker build -t chicagoland-mesh-utilities .
```

### Run the container:
```bash
docker run -p 50000:50000 chicagoland-mesh-utilities
```

### Or use Docker Compose:
```bash
docker-compose up -d
```

The application will be available at `http://localhost:50000`

## Stopping the Application

### If using docker run:
```bash
docker ps  # Find the container ID
docker stop <container-id>
```

### If using docker-compose:
```bash
docker-compose down
```

## Development

To run locally without Docker:
```bash
pip install -r requirements.txt
python app.py
```

## Features

- Repeater configuration generator
- Companion configuration generator
- Prefix matrix browser
- Serial USB command console

