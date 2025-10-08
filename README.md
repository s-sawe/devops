# E-Commerce (Django) — DevOps Pipeline

## Run locally
1. Activate venv: `source .venv/bin/activate`
2. Create `.env` (see example)
3. `docker compose up --build -d`
4. `docker compose exec web python manage.py migrate`
5. `docker compose exec web python manage.py createsuperuser`
6. Visit http://localhost:8000 and admin at /admin

## CI/CD
- GitHub Actions builds image, runs Trivy, pushes to DockerHub and deploys to EC2.

## Infra
- Terraform files under `infra/` to create a simple EC2 instance.

## Monitoring
- Start Prometheus & Grafana: `cd monitoring && docker compose -f docker-compose.monitor.yml up -d`

## Live Endpoints
- http://51.20.121.132:8000/products --> Fetches All Products
- http://51.20.121.132:8000/products/1 --> Fetches a single product
