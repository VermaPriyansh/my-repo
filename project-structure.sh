#!/bin/bash
# Create the project structure for Multi-Language AI Prompt Validator

# Create root directory
mkdir -p ai-prompt-validator
cd ai-prompt-validator

# Create backend directory structure
mkdir -p backend/app/api
mkdir -p backend/app/core
mkdir -p backend/app/models
mkdir -p backend/app/services
mkdir -p backend/tests

# Create frontend directory structure
mkdir -p frontend/src/components
mkdir -p frontend/src/hooks
mkdir -p frontend/src/pages
mkdir -p frontend/src/services
mkdir -p frontend/src/utils
mkdir -p frontend/public

# Create infrastructure directory
mkdir -p infrastructure/terraform

# Create CI/CD directory
mkdir -p .github/workflows

# Create documentation directory
mkdir -p docs

# Create root files
touch README.md
touch .gitignore

# Create backend files
touch backend/requirements.txt
touch backend/app/__init__.py
touch backend/app/main.py
touch backend/Dockerfile

# Create frontend files
touch frontend/package.json
touch frontend/tsconfig.json
touch frontend/src/index.tsx
touch frontend/Dockerfile

# Create infrastructure files
touch infrastructure/terraform/main.tf
touch infrastructure/terraform/variables.tf
touch infrastructure/terraform/outputs.tf

# Create CI/CD files
touch .github/workflows/deploy.yml

echo "Project structure created successfully!"
