
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Allow CORS for local frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Event and Report Models
class Event(BaseModel):
    title: str
    date: str
    description: str
    portal: str

class Report(BaseModel):
    student: str
    subject: str
    score: int
    comment: str
    portal: str

# In-memory stores for events and reports
student_events: List[dict] = []
teacher_events: List[dict] = []
parent_events: List[dict] = []
admin_events: List[dict] = []

student_reports: List[dict] = []
teacher_reports: List[dict] = []
parent_reports: List[dict] = []
admin_reports: List[dict] = []

# Student Portal Events & Reports
@app.get("/student/events")
def get_student_events():
    return {"events": student_events}

@app.post("/student/event")
def post_student_event(event: Event):
    student_events.append(event.dict())
    return {"status": "success", "event": event.dict()}

@app.get("/student/reports")
def get_student_reports():
    return {"reports": student_reports}

@app.post("/student/report")
def post_student_report(report: Report):
    student_reports.append(report.dict())
    return {"status": "success", "report": report.dict()}

# Teacher Portal Events & Reports
@app.get("/teacher/events")
def get_teacher_events():
    return {"events": teacher_events}

@app.post("/teacher/event")
def post_teacher_event(event: Event):
    teacher_events.append(event.dict())
    return {"status": "success", "event": event.dict()}

@app.get("/teacher/reports")
def get_teacher_reports():
    return {"reports": teacher_reports}

@app.post("/teacher/report")
def post_teacher_report(report: Report):
    teacher_reports.append(report.dict())
    return {"status": "success", "report": report.dict()}

# Parent Portal Events & Reports
@app.get("/parent/events")
def get_parent_events():
    return {"events": parent_events}

@app.post("/parent/event")
def post_parent_event(event: Event):
    parent_events.append(event.dict())
    return {"status": "success", "event": event.dict()}

@app.get("/parent/reports")
def get_parent_reports():
    return {"reports": parent_reports}

@app.post("/parent/report")
def post_parent_report(report: Report):
    parent_reports.append(report.dict())
    return {"status": "success", "report": report.dict()}

# Admin Portal Events & Reports
@app.get("/admin/events")
def get_admin_events():
    return {"events": admin_events}

@app.post("/admin/event")
def post_admin_event(event: Event):
    admin_events.append(event.dict())
    return {"status": "success", "event": event.dict()}

@app.get("/admin/reports")
def get_admin_reports():
    return {"reports": admin_reports}

@app.post("/admin/report")
def post_admin_report(report: Report):
    admin_reports.append(report.dict())
    return {"status": "success", "report": report.dict()}


# In-memory stores for all portals
student_notifications = [
    {"id": 1, "message": "Welcome to Sutomo Student Portal!"},
    {"id": 2, "message": "Your assignment is due tomorrow."}
]
teacher_notifications = [
    {"id": 1, "message": "Welcome to Teacher Portal!"},
    {"id": 2, "message": "New parent message received."}
]
parent_notifications = [
    {"id": 1, "message": "Welcome to Parent Portal!"},
    {"id": 2, "message": "New announcement from teacher."}
]
admin_notifications = [
    {"id": 1, "message": "Welcome to Admin Dashboard!"},
    {"id": 2, "message": "System update scheduled."}
]

class ChatMessage(BaseModel):
    user: str
    message: str

class Announcement(BaseModel):
    subject: str
    message: str
    sender: str

class PortalMessage(BaseModel):
    sender: str
    recipient: str
    message: str

# Chat histories
student_chat_history: List[dict] = []
teacher_chat_history: List[dict] = []
parent_chat_history: List[dict] = []
admin_chat_history: List[dict] = []

# Announcements
teacher_announcements: List[dict] = []
parent_announcements: List[dict] = []
admin_announcements: List[dict] = []

# Messages
teacher_messages: List[dict] = []
parent_messages: List[dict] = []
admin_messages: List[dict] = []

# Student Portal Endpoints
@app.get("/student/notifications")
def get_student_notifications():
    return {"notifications": student_notifications}

@app.post("/student/chat")
def student_chat(msg: ChatMessage):
    response = f"AI: You said '{msg.message}'"
    student_chat_history.append({"user": msg.user, "message": msg.message, "response": response})
    return {"response": response}

@app.get("/student/chat/history")
def get_student_chat_history():
    return {"history": student_chat_history}

# Teacher Portal Endpoints
@app.get("/teacher/notifications")
def get_teacher_notifications():
    return {"notifications": teacher_notifications}

@app.post("/teacher/chat")
def teacher_chat(msg: ChatMessage):
    response = f"AI: You said '{msg.message}'"
    teacher_chat_history.append({"user": msg.user, "message": msg.message, "response": response})
    return {"response": response}

@app.get("/teacher/chat/history")
def get_teacher_chat_history():
    return {"history": teacher_chat_history}

@app.post("/teacher/announcement")
def post_teacher_announcement(announcement: Announcement):
    teacher_announcements.append(announcement.dict())
    return {"status": "success", "announcement": announcement.dict()}

@app.get("/teacher/announcements")
def get_teacher_announcements():
    return {"announcements": teacher_announcements}

@app.post("/teacher/message")
def post_teacher_message(msg: PortalMessage):
    teacher_messages.append(msg.dict())
    return {"status": "success", "message": msg.dict()}

@app.get("/teacher/messages")
def get_teacher_messages():
    return {"messages": teacher_messages}

# Parent Portal Endpoints
@app.get("/parent/notifications")
def get_parent_notifications():
    return {"notifications": parent_notifications}

@app.post("/parent/chat")
def parent_chat(msg: ChatMessage):
    response = f"AI: You said '{msg.message}'"
    parent_chat_history.append({"user": msg.user, "message": msg.message, "response": response})
    return {"response": response}

@app.get("/parent/chat/history")
def get_parent_chat_history():
    return {"history": parent_chat_history}

@app.post("/parent/announcement")
def post_parent_announcement(announcement: Announcement):
    parent_announcements.append(announcement.dict())
    return {"status": "success", "announcement": announcement.dict()}

@app.get("/parent/announcements")
def get_parent_announcements():
    return {"announcements": parent_announcements}

@app.post("/parent/message")
def post_parent_message(msg: PortalMessage):
    parent_messages.append(msg.dict())
    return {"status": "success", "message": msg.dict()}

@app.get("/parent/messages")
def get_parent_messages():
    return {"messages": parent_messages}

# Admin Portal Endpoints
@app.get("/admin/notifications")
def get_admin_notifications():
    return {"notifications": admin_notifications}

@app.post("/admin/chat")
def admin_chat(msg: ChatMessage):
    response = f"AI: You said '{msg.message}'"
    admin_chat_history.append({"user": msg.user, "message": msg.message, "response": response})
    return {"response": response}

@app.get("/admin/chat/history")
def get_admin_chat_history():
    return {"history": admin_chat_history}

@app.post("/admin/announcement")
def post_admin_announcement(announcement: Announcement):
    admin_announcements.append(announcement.dict())
    return {"status": "success", "announcement": announcement.dict()}

@app.get("/admin/announcements")
def get_admin_announcements():
    return {"announcements": admin_announcements}

@app.post("/admin/message")
def post_admin_message(msg: PortalMessage):
    admin_messages.append(msg.dict())
    return {"status": "success", "message": msg.dict()}

@app.get("/admin/messages")
def get_admin_messages():
    return {"messages": admin_messages}
