# AI Prompt Validator

A comprehensive tool for validating, optimizing, and improving AI prompts across multiple languages. This system helps users create better prompts by checking for issues like grammar mistakes, ambiguity, and potential toxicity, while also suggesting improvements.

## Features

### Multilingual Support
- Support for 50+ languages
- Real-time translation preview
- Cultural nuance detection

### Validation Features
- Grammar and syntax checking
- Toxicity detection
- Ambiguity identification
- AI-powered correction suggestions

### Optimization Tools
- Style and tone adjustments
- Output format priming
- Contextual prompt improvements

### Analytics
- Prompt quality scoring
- Bias detection
- A/B testing for prompt variants

## Tech Stack

### Frontend
- React 19 with TypeScript
- Redux Toolkit with RTK Query
- Shadcn UI components
- i18next for localization

### Backend
- Python 3.12
- FastAPI with WebSockets
- Custom ML pipeline for prompt validation
- Azure Cognitive Services integration

### Infrastructure
- Azure Container Apps
- Azure Cosmos DB
- Terraform for IaC
- GitHub Actions for CI/CD

## Getting Started

### Prerequisites
- Node.js 18+
- Python 3.12+
- Docker
- Azure CLI (for deployment)

### Local Development

1. Clone the repository
```bash
git clone https://github.com/yourusername/ai-prompt-validator.git
cd ai-prompt-validator
```

2. Set up the backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

3. Set up the frontend
```bash
cd frontend
npm install
npm run dev
```

4. Open your browser and visit `http://localhost:5173`

### Docker Development

```bash
# Build and run the backend
docker build -t prompt-validator-backend ./backend
docker run -p 8000:8000 prompt-validator-backend

# Build and run the frontend
docker build -t prompt-validator-frontend ./frontend
docker run -p 80:80 prompt-validator-frontend
```

## Deployment

### Using Terraform

1. Set up your Azure credentials
```bash
az login
```

2