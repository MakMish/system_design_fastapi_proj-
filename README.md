# ⚡ Scalable FastAPI Backend

A production-oriented, high-performance backend system built with **FastAPI (Async)**, **Redis**, **Celery**, and **PostgreSQL**. The project focuses on scalability, performance optimization, background task processing, caching, rate limiting, load testing, and containerized deployment workflows.

### 🔗 Links

* **Live Demo:** <https://fastapi-system-design-1.onrender.com/docs>

## 🚀 Highlights

* ⚡ **320+ RPS** achieved through performance optimization and asynchronous architecture
* 🚀 **57% faster performance** after implementing a robust Redis caching layer
* 🔄 Background task processing using **Celery + Redis**
* 🛡️ JWT-based authentication and API rate limiting
* 🗄️ PostgreSQL database with **SQLAlchemy + Alembic**
* 📊 Load testing and performance benchmarking with **Locust**
* 🐳 Containerized using **Docker**
* 🏗️ Designed with scalability and production deployment in mind

## 🛠️ Tech Stack

| Technology     | Purpose                                |
| -------------- | -------------------------------------- |
| **FastAPI**    | High-performance asynchronous REST API |
| **PostgreSQL** | Relational database                    |
| **Redis**      | Caching, rate limiting & Celery broker |
| **Celery**     | Background task processing             |
| **SQLAlchemy** | Async database interaction             |
| **Alembic**    | Database schema migrations             |
| **JWT**        | Authentication & authorization         |
| **Locust**     | Load & performance testing             |
| **Docker**     | Containerization                       |

## 🏗️ Architecture

```text
                    ┌──────────────────┐
                    │      Client      │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │     FastAPI      │
                    │    Async API     │
                    └────────┬─────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
        ┌──────────┐   ┌───────────┐   ┌──────────┐
        │  Redis   │   │ PostgreSQL │   │  Celery  │
        │  Cache   │   │    DB      │   │ Workers  │
        └──────────┘   └───────────┘   └────┬─────┘
                                            │
                                            ▼
                                     Background Tasks
```

## ⚡ Performance

The backend was stress-tested using **Locust** to evaluate throughput and performance under concurrent workloads.

### Benchmark Results

* **320+ Requests Per Second**
* **57% performance improvement** after implementing Redis caching
* Asynchronous request handling with FastAPI
* Rate limiting for controlled API traffic
* Load testing with concurrent simulated users

Redis caching was implemented to reduce unnecessary database queries and efficiently serve frequently requested data, resulting in a significant improvement in overall API performance.

## 🔐 Authentication & Security

The backend implements:

* JWT-based authentication
* Protected API endpoints
* Token-based authorization
* API rate limiting
* Environment-based configuration for sensitive credentials

## 🔄 Background Task Processing

Time-consuming operations are handled asynchronously using **Celery**, preventing long-running tasks from blocking API requests.

```text
                    FastAPI
                       │
                       ▼
                Create Task
                       │
                       ▼
                    Redis
                       │
                       ▼
                Celery Worker
                       │
                       ▼
               Background Job
```

This architecture keeps the API responsive while background operations are processed independently by Celery workers.

## 🗄️ Database

The project uses **PostgreSQL** for persistent data storage and **SQLAlchemy** for database interaction.

**Alembic** is used for version-controlled database migrations and schema management.

```bash
alembic upgrade head
```

## 📊 Load Testing

Performance testing was performed using **Locust** to simulate concurrent users and measure API throughput.

```bash
locust -f locustfile.py
```

The testing process was used to:

* Measure requests per second
* Evaluate API response performance
* Simulate concurrent traffic
* Identify performance bottlenecks
* Validate the impact of Redis caching

## 🐳 Docker

The application is containerized using **Docker** to provide a consistent and reproducible development and deployment environment.

```bash
docker compose up --build
```

Docker allows the backend services and their dependencies to run in isolated containers while maintaining a consistent environment across development and deployment.

## 📁 Project Structure

```text
.
├── src/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── tasks/
│   └── main.py
│
├── alembic/
├── tests/
├── locustfile.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <project-directory>
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file and configure the required application settings.

```env
DATABASE_URL=your_database_url
REDIS_URL=your_redis_url
SECRET_KEY=your_secret_key
```

### 5. Run Database Migrations

```bash
alembic upgrade head
```

### 6. Start the API

```bash
uvicorn src.main:app --reload
```

The API documentation will be available at:

```text
http://localhost:8000/docs
```

## 📈 Performance Optimization

The project focuses on several backend performance and scalability techniques:

* Asynchronous API architecture with FastAPI
* Redis-based response caching
* API rate limiting
* Efficient PostgreSQL database interaction
* Background task processing with Celery
* Containerized deployment using Docker
* Concurrent load testing with Locust

These optimizations helped improve throughput while reducing unnecessary database workload.

## 🎯 Key Engineering Concepts

This project demonstrates practical experience with:

* Scalable asynchronous backend architecture
* REST API development with FastAPI
* Redis caching strategies
* Distributed background task processing
* PostgreSQL database integration
* Database migrations with Alembic
* JWT authentication
* API rate limiting
* Performance benchmarking
* Load testing with Locust
* Docker-based deployment workflows

---

## ⭐ Project

Built to explore and demonstrate **high-performance backend architecture, scalability, caching, asynchronous processing, and production-oriented deployment practices**.
