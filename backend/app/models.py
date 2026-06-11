"""Database Models"""

from sqlalchemy import Column, Integer, String, Text, Float, DateTime, Boolean, ForeignKey, Table, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
from datetime import datetime
import enum

profile_skills = Table(
    'profile_skills',
    Base.metadata,
    Column('profile_id', Integer, ForeignKey('profiles.id')),
    Column('skill_id', Integer, ForeignKey('skills.id'))
)

class ApplicationStatus(str, enum.Enum):
    """Application status enum"""
    DRAFT = "draft"
    SUBMITTED = "submitted"
    VIEWED = "viewed"
    INTERVIEW = "interview"
    OFFER = "offer"
    REJECTED = "rejected"
    WITHDRAWN = "withdrawn"

class Profile(Base):
    """User Professional Profile"""
    __tablename__ = "profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    phone = Column(String(20))
    current_title = Column(String(255))
    bio = Column(Text)
    years_experience = Column(Integer)
    
    skills = relationship("Skill", secondary=profile_skills, backref="profiles")
    achievements = relationship("Achievement", back_populates="profile", cascade="all, delete-orphan")
    applications = relationship("Application", back_populates="profile", cascade="all, delete-orphan")
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

class Skill(Base):
    """Technical and Soft Skills"""
    __tablename__ = "skills"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True, nullable=False)
    category = Column(String(100))
    proficiency = Column(String(50))
    
    created_at = Column(DateTime, server_default=func.now())

class Achievement(Base):
    """Professional Achievements and Projects"""
    __tablename__ = "achievements"
    
    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey('profiles.id'), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    impact = Column(Text)
    category = Column(String(100))
    keywords = Column(Text)
    
    profile = relationship("Profile", back_populates="achievements")
    
    created_at = Column(DateTime, server_default=func.now())

class Job(Base):
    """Job Listings Scraped from LinkedIn"""
    __tablename__ = "jobs"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    company = Column(String(255), nullable=False)
    location = Column(String(255))
    job_url = Column(String(500), unique=True, index=True)
    linkedin_job_id = Column(String(100), unique=True, index=True)
    
    description = Column(Text)
    requirements = Column(Text)
    salary_min = Column(Float)
    salary_max = Column(Float)
    salary_currency = Column(String(10))
    
    job_type = Column(String(50))
    seniority_level = Column(String(50))
    
    posted_date = Column(DateTime)
    scraped_at = Column(DateTime, server_default=func.now())
    
    applications = relationship("Application", back_populates="job", cascade="all, delete-orphan")
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

class Application(Base):
    """Job Applications"""
    __tablename__ = "applications"
    
    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey('profiles.id'), nullable=False)
    job_id = Column(Integer, ForeignKey('jobs.id'), nullable=False)
    
    status = Column(Enum(ApplicationStatus), default=ApplicationStatus.DRAFT)
    match_score = Column(Float)
    
    cover_letter = Column(Text)
    resume_content = Column(Text)
    notes = Column(Text)
    
    applied_date = Column(DateTime)
    follow_up_date = Column(DateTime)
    response_received_date = Column(DateTime)
    
    profile = relationship("Profile", back_populates="applications")
    job = relationship("Job", back_populates="applications")
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
