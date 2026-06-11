# AI Job Application Agent

An intelligent automation system to streamline your job application process. This agent handles everything from building your experience database to automated job matching, cover letter generation, and application tracking.

## Features

✅ **Master Experience Database** - Centralized storage of your professional profile  
✅ **Job Scraping** - Automated LinkedIn job listing collection  
✅ **Job Matching** - AI-powered compatibility analysis  
✅ **Cover Letter Generation** - AI-tailored cover letters for each application  
✅ **Resume Customization** - Dynamically tailored resumes  
✅ **Application Automation** - Auto-fill and submit applications  
✅ **Status Tracking** - Dashboard to monitor all applications  

## Tech Stack

- **Backend**: Python + FastAPI
- **Database**: SQLite (lightweight, no server needed)
- **Job Scraping**: Selenium + BeautifulSoup (LinkedIn)
- **AI/NLP**: OpenAI API (GPT for content generation)

## Quick Start

### Prerequisites
- Python 3.9+
- pip

### Installation

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your API keys
uvicorn app.main:app --reload
```

API available at `http://localhost:8000`
Docs at `http://localhost:8000/api/docs`

## API Endpoints

### Profile Management
- `POST /api/profile` - Create profile
- `GET /api/profile` - Get profile
- `POST /api/profile/achievements` - Add achievements
- `GET /api/profile/skills` - Get skills

### Job Management
- `POST /api/jobs/scrape` - Scrape LinkedIn jobs
- `GET /api/jobs` - List jobs
- `GET /api/jobs/{id}/match` - Get compatibility score

### Applications
- `POST /api/applications` - Create application
- `GET /api/applications` - List applications
- `PUT /api/applications/{id}` - Update application

### Content Generation
- `POST /api/applications/generate-cover-letter` - Generate cover letter
- `POST /api/applications/generate-resume` - Generate resume

### Tracking
- `GET /api/tracking/stats` - Get statistics
- `GET /api/tracking/summary` - Get summary

## License

MIT License
