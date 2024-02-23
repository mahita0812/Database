from sqlalchemy import Column, Integer, Enum, String, DateTime, Text
from database import Base
import enum
from datetime import datetime

# class SeverityEnum(enum.Enum):
#     one = 1
#     two = 2
#     three = 3
#     four = 4

class PriorityEnum(enum.Enum):
    High = 'High'
    Medium = 'Medium'
    Low = 'Low'
    
class TickettypeEnum(enum.Enum):
    Incident = "Incident"
    ServiceRequest = "Service Request"

class ServiceEnum(enum.Enum):
    Phonecall = "Phonecall"
    Email = "Email"

class LLM(Base):
    __tablename__ = "LLM_job_details"

    id = Column(Integer,primary_key=True,autoincrement=True)
    ticket_id = Column(Integer, unique=True)
    requestor_name = Column(String(50))
    severity = Column(Integer)
    priority = Column(Enum(PriorityEnum))
    ticket_type = Column(Enum(TickettypeEnum))
    service = Column(Enum(ServiceEnum))
    message = Column(String(100))


class FeedbackEnum(enum.Enum):
    Positive = "Positive"
    Negative = "Negative"

class StatusEnum(enum.Enum):
    Pending = 'Pending'
    Inprogress = 'Inprogress'
    Completed = 'Completed'
    Failed = 'Failed'

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer,primary_key=True,autoincrement=True)
    LLM_id = Column(Integer)
    feedback = Column(Enum(FeedbackEnum))
    failed_reason = Column(String(100))
    response = Column(String(100))
    reference = Column(Text)
    status = Column(Enum(StatusEnum))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    created_by = Column(String(50))
    updated_by = Column(String(50))