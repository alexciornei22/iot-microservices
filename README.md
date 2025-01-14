# Sensors

- [Project Overview](#project-overview)
- [Implementation details](#implementation-details)
- [Setup and Usage](#setup-and-usage)
  - [Prerequisites](#prerequisites)
  - [Initial Setup](#initial-setup)
  - [Stopping and Restarting](#stopping-and-restarting)
  - [Test Sensor](#test-sensor)
  - [Data Persistence](#data-persistence)
- [Environment Variables](#environment-variables)

## Project Overview

This project sets up a Docker Swarm stack for a sensor data collection and visualization application. The stack includes:
- **Eclipse Mosquitto**: MQTT broker for sensor data.
- **InfluxDB**: Time-series database.
- **Adapter**: Custom service that subscribes to MQTT messages and writes data to InfluxDB.
- **Grafana**: Visualization tool.

## Implementation details

1. **Service Isolation**: Each service runs in its own container for modularity.
2. **Network Segmentation**: Custom networks control service communication, enhancing security.
3. **Data Persistence**: Docker volumes ensure data is not lost between restarts.
4. **Environment Variables**: Configuration is managed using environment variables for flexibility.
5. **Provisioning**: Grafana dashboards and data sources are automatically provisioned at stack creation.

## Setup and Usage

### Prerequisites

- Docker
- Docker Swarm (initialized)

### Initial Setup

- **Run the Setup Script**:
   ```sh
   ./run.sh
   ```

### Stopping and Restarting

- **Stop the Stack**:
  ```sh
  docker stack rm scd3
  ```

- **Restart the Stack**:
  ```sh
  docker stack deploy -c stack.yml scd3
  ```

### Test Sensor

The `test_sensor` directory contains a python script that runs a simulated sensor. To run the script, follow these steps in that directory:

1. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
   
2. **Run the Script**:
   ```sh
    python test_sensor.py
    ```

### Data Persistence

Data stored by InfluxDB and configuration changes in Grafana are persisted across restarts thanks to Docker volumes.

## Environment Variables

### InfluxDB

- `DOCKER_INFLUXDB_INIT_MODE`: Setup mode for InfluxDB.
- `DOCKER_INFLUXDB_INIT_USERNAME`: Initial username for InfluxDB.
- `DOCKER_INFLUXDB_INIT_PASSWORD`: Initial password for InfluxDB.
- `DOCKER_INFLUXDB_INIT_ORG`: Initial organization for InfluxDB.
- `DOCKER_INFLUXDB_INIT_BUCKET`: Initial bucket for InfluxDB.
- `DOCKER_INFLUXDB_INIT_RETENTION`: Retention policy for the bucket.
- `DOCKER_INFLUXDB_INIT_ADMIN_TOKEN`: Admin token for InfluxDB.

### Adapter

- `MQTT_BROKER_URL`: URL of the MQTT broker.
- `MQTT_BROKER_PORT`: Port of the MQTT broker.
- `INFLUXDB_URL`: URL of the InfluxDB instance.
- `INFLUXDB_TOKEN`: Token for InfluxDB authentication.
- `INFLUXDB_ORG`: Organization for InfluxDB.
- `INFLUXDB_BUCKET`: Bucket for InfluxDB.
- `DEBUG_DATA_FLOW`: Flag to enable or disable debug logging.

### Grafana

- `GF_SECURITY_ADMIN_USER`: Admin username for Grafana.
- `GF_SECURITY_ADMIN_PASSWORD`: Admin password for Grafana.
- `GF_USERS_ALLOW_SIGN_UP`: Flag to allow or disallow user sign-up.
- `INFLUXDB_URL`: URL of the InfluxDB instance.
- `INFLUXDB_TOKEN`: Token for InfluxDB authentication.
- `INFLUXDB_ORG`: Organization for InfluxDB.
- `INFLUXDB_BUCKET`: Bucket for InfluxDB.
