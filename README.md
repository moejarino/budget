# Budget App

A modern full-stack budget tracking application built with:

## Frontend
- Vite
- React
- Apollo Client
- TypeScript

## Backend
- FastAPI
- Strawberry GraphQL
- Supabase
- Python

## Project Structure
```
budget/
├── frontend/           # Vite/React frontend
├── backend/            # FastAPI backend
└── README.md
```

## Getting Started

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Environment Variables

### Frontend
Create a `.env` file in the frontend directory:
```
VITE_API_URL=http://localhost:8000
VITE_SUPABASE_URL=your_supabase_url
VITE_SUPABASE_ANON_KEY=your_supabase_anon_key
```

### Backend
Create a `.env` file in the backend directory:
```
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
DATABASE_URL=your_database_url
```

## Development

- Frontend runs on http://localhost:5173
- Backend runs on http://localhost:8000
- GraphQL Playground available at http://localhost:8000/graphql