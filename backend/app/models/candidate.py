from typing import Optional, Any

from pydantic import BaseModel, Field


# Profile models

class Location(BaseModel):
    city: str
    state: str
    country: str


class Contact(BaseModel):
    email: str


class Links(BaseModel):
    linkedin: Optional[str] = None
    github: Optional[str] = None
    portfolio: Optional[str] = None


class Profile(BaseModel):
    name: str
    professional_title: str
    location: Location
    contact: Contact
    links: Links
    graduation_year: int
    current_status: str


# Education model

class Education(BaseModel):
    institution: str
    degree: str
    field: str
    location: str
    start_date: str
    expected_graduation: str
    cgpa: float
    scale: int
    status: str
    coursework: list[str]


# Skills models

class ProgrammingLanguage(BaseModel):
    name: str
    level: str
    primary_use: Optional[list[str]] = None


class BackendDevelopment(BaseModel):
    languages: list[str]
    frameworks: list[str]
    concepts: list[str]


class Skills(BaseModel):
    programming_languages: list[ProgrammingLanguage]
    core_computer_science: list[str]
    backend_development: BackendDevelopment
    databases: list[str]
    machine_learning_and_ai: list[str]
    frontend_basics: list[str]
    developer_tools: list[str]


# Data structures and algorithms model

class DataStructuresAndAlgorithms(BaseModel):
    leetcode_problems_solved: int
    statement: str
    primary_language: str
    focus_areas: list[str]
    leetcode_profile: Optional[str] = None


# Project models

class Dataset(BaseModel):
    name: str
    images: int
    annotated_bounding_boxes: str


class Results(BaseModel):
    map_at_50: str
    precision: str
    recall: str


class Deployment(BaseModel):
    platform: str
    url: Optional[str] = None


class Team(BaseModel):
    size: int
    role: str


class ProjectAchievement(BaseModel):
    competition: str
    rank: int
    total_teams: str
    date: str


class Project(BaseModel):
    name: str
    category: list[str]
    status: str
    technologies: list[str]

    description: str

    problem_statement: Optional[str] = None

    key_features: list[str] = Field(default_factory=list)
    technical_implementation: list[str] = Field(default_factory=list)

    dataset: Optional[Dataset] = None
    results: Optional[Results] = None
    deployment: Optional[Deployment] = None

    repository: Optional[str] = None
    role: Optional[str] = None
    team_size: Optional[int] = None

    team: Optional[Team] = None
    achievement: Optional[ProjectAchievement] = None

    challenges: list[str] = Field(default_factory=list)
    future_improvements: list[str] = Field(default_factory=list)

    demo: Optional[str] = None


# Experience models

class TeamLeadership(BaseModel):
    subteam_size: int
    led_subteam: bool


class Experience(BaseModel):
    organization: str
    role: str
    location: str
    start_date: str
    end_date: str
    organization_size: str

    team_leadership: Optional[TeamLeadership] = None

    responsibilities: list[str]
    skills_demonstrated: list[str]


# Achievement model

class AchievementItem(BaseModel):
    title: str
    achievement: str
    project: Optional[str] = None
    category: Optional[str] = None
    date: Optional[str] = None


# Hackathon model

class Hackathon(BaseModel):
    name: str
    date: str
    result: str
    participating_teams: str
    project: str
    team_size: int


# Position of responsibility model

class PositionOfResponsibility(BaseModel):
    organization: str
    position: str
    leadership_scope: str


# Career goals model

class CareerGoals(BaseModel):
    current_target_roles: list[str]
    primary_direction: str
    preferred_domains: list[str]
    long_term_goals: list[str]
    preferred_work_environment: list[str]
    companies_of_interest: list[str]
    higher_studies_goals: list[str]


# Learning model

class Learning(BaseModel):
    currently_learning: list[str]
    completed_learning: list[str]
    future_learning: list[str]


# Portfolio model

class Portfolio(BaseModel):
    personal_website: Optional[str] = None
    github: Optional[str] = None
    linkedin: Optional[str] = None
    project_links: dict[str, Optional[str]]


# Professional summary model

class ProfessionalSummary(BaseModel):
    short: str
    detailed: str
    current_focus: list[str]


# Main candidate model

class Candidate(BaseModel):
    profile: Profile
    professional_summary: ProfessionalSummary
    education: list[Education]
    skills: Skills
    data_structures_and_algorithms: DataStructuresAndAlgorithms
    projects: list[Project]
    experience: list[Experience]
    achievements: list[AchievementItem]
    hackathons: list[Hackathon]
    positions_of_responsibility: list[PositionOfResponsibility]
    certifications: list[Any]
    career_goals: CareerGoals
    professional_strengths: list[str]
    areas_of_expertise: list[str]
    interests: list[str]
    learning: Learning
    portfolio: Portfolio