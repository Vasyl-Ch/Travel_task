# Travel Planner API

A Django REST API for managing travel projects and places.

## Models
- **TravelProject**: Travel projects with name, description, dates, and completion status
- **Place**: Places within projects with external ID, title, notes, and visited status

## API Endpoints

### Projects
- `GET /projects/` - List all projects
- `POST /projects/` - Create new project
- `GET /projects/{id}/` - Get project details
- `PATCH /projects/{id}/` - Update project
- `DELETE /projects/{id}/` - Delete project

### Places
- `GET /projects/{project_id}/places/` - List places in project
- `POST /projects/{project_id}/places/` - Create place in project
- `GET /projects/{project_id}/places/{id}/` - Get place details
- `PATCH /projects/{project_id}/places/{id}/` - Update place
- `DELETE /projects/{project_id}/places/{id}/` - Delete place

### Documentation
- `GET /api/docs/` - Swagger UI
- `GET /api/schema/` - OpenAPI schema

## Running

### Docker
```bash
docker-compose up --build

# Create Super User
docker-compose exec web python manage.py createsuperuser

```

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Setup environment
cp .env.example .env
# Edit .env with your SECRET_KEY

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver

# Create super user
python manage.py createsuperuser
```

## Testing
```bash
python manage.py test
```