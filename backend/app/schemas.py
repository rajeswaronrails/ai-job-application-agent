"""Pydantic Schemas for Request/Response Validation"""

from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum

class SkillCreate(BaseModel):
    name: str
    category: Optional[str] = None
    proficiency: Optional[str] = None

class Skill(SkillCreate):
    id: int
    class Config:
        from_attributes = True

class AchievementCreate(BaseModel):
    title: str
    description: Optional[str] = None
    impact: Optional[str] = None
    category: Optional[str] = None
    keywords: Optional[str] = None

class Achievement(AchievementCreate):
    id: int
    profile_id: int
    created_at: datetime
    class Config:
        from_attributes = True

class ProfileCreate(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    current_title: Optional[str] = None
    bio: Optional[str] = None
    years_experience: Optional[int] = None

class ProfileUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    current_title: Optional[str] = None
    bio: Optional[str] = None
    years_experience: Optional[int] = None

class Profile(ProfileCreate):
    id: int
    skills: List[Skill] = []
    achievements: List[Achievement] = []
    created_at: datetime
    updated_at: datetime
    class Config:
        from_attributes = True

class JobCreate(BaseModel):
    title: str
    company: str
    location: Optional[str] = None
    job_url: str
    description: Optional[str] = None
    requirements: Optional[str] = None
    job_type: Optional[str] = None
    seniority_level: Optional[str] = None
    linkedin_job_id: Optional[str] = None

class Job(JobCreate):
    id: int
    salary_min: Optional[float] = None
    salary_max: Optional[float] = None
    salary_currency: Optional[str] = None
    posted_date: Optional[datetime] = None
    scraped_at: datetime
    created_at: datetime
    updated_at: datetime
    class Config:
        from_attributes = True

class JobWithMatch(Job):
    match_score: Optional[float] = None
    matched_skills: List[str] = []
    matched_achievements: List[str] = []

class ApplicationStatus(str, Enum):
    DRAFT = "draft"
    SUBMITTED = "submitted"
    VIEWED = "viewed"
    INTERVIEW = "interview"
    OFFER = "offer"
    REJECTED = "rejected"
    WITHDRAWN = "withdrawn"

class ApplicationCreate(BaseModel):
    profile_id: int
    job_id: int
    status: ApplicationStatus = ApplicationStatus.DRAFT
    cover_letter: Optional[str] = None
    resume_content: Optional[str] = None

class ApplicationUpdate(BaseModel):
    status: Optional[ApplicationStatus] = None
    cover_letter: Optional[str] = None
    resume_content: Optional[str] = None
    notes: Optional[str] = None
    follow_up_date: Optional[datetime] = None

class Application(ApplicationCreate):
    id: int
    match_score: Optional[float] = None
    applied_date: Optional[datetime] = None
    follow_up_date: Optional[datetime] = None
    response_received_date: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
    job: Job
    class Config:
        from_attributes = True

class LinkedInScrapingRequest(BaseModel):
    keywords: List[str] = Field(..., description="Job search keywords")
    locations: List[str] = Field(default=["Remote"], description="Job locations")
    max_results: int = Field(default=50, le=500)

class ScrapingResponse(BaseModel):
    success: bool
    jobs_scraped: int
    jobs_added: int
    jobs_skipped: int
    message: str

class CoverLetterGenerationRequest(BaseModel):
    job_id: int
    tone: Optional[str] = Field(default="professional")

class CoverLetterResponse(BaseModel):
    cover_letter: str
    job_id: int

class ResumeGenerationRequest(BaseModel):
    job_id: int
    format: Optional[str] = Field(default="text")

class ResumeResponse(BaseModel):
    resume_content: str
    job_id: int
