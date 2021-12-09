"""Models for App Tracker."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


def connect_to_db(flask_app, db_uri='postgresql:///tracker', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')



class User(db.Model):
    """A user."""

    __tablename__ = "app_user"

    user_id = db.Column(db.Integer, 
                        autoincrement = True,
                        primary_key = True)
    username = db.Column(db.String, unique = True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    job_title = db.Column(db.String)
    email = db.Column(db.String, unique = True)
    password = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    picture = db.Column(db.String)

    def __repr__(self):
        return f"User_ID: {self.user_id}, Username: {self.username}, Full Name: {self.fname} {self.lname}, Title: {self.title}, Email: {self.email}, Location: {self.city} {self.state}"


class User_Link(db.Model):
    """Links on a user's profile."""

    __tablename___ = "user_link"

    user_link_id = db.Column(db.Integer, 
                            autoincrement = True,
                            primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("app_user.user_id"))
    portfolio_url = db.Column(db.String)
    github_url = db.Column(db.String)
    linkedin_url = db.Column(db.String)
    other_url = db.Column(db.String)

    app_user = db.relationship("User", backref = "user_link")

    def __repr__(self):
        return f"User Link ID: {self.user_link_id}, User ID: {self.user_id}, Portfolio: {self.portfolio_url}, Github: {self.github_url}, LinkedIn: {self.linkedin_url} Other: {self.other_url}"


class Resume_Bio(db.Model):
    """A user's saves resumes and bios."""

    __tablename__ = "resume_bio"

    resume_id = db.Column(db.Integer,
                            autoincrement = True,
                            primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("app_user.user_id"))
    upload_resume = db.Column(db.String, default = None)
    type_resume = db.Column(db.String, default = None)
    bio = db.Column(db.String, default = None)
    label = db.Column(db.String)

    app_user = db.relationship("User", backref = "resume_bio")

    def __repr__(self):
        return f"Resume ID: {self.resume_id}, User ID: {self.user_id}, Uploaded: {self.upload_resume}, Typed: {self.type_resume}, Bio: {self.bio}, Label: {self.label}"


class Job_Info(db.Model):
    """A user's career info."""

    __tablename__ = "job_info"

    job_info_id = db.Column(db.Integer,
                            autoincrement = True,
                            primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("app_user.user_id"))
    company_name = db.Column(db.String)
    title = db.Column(db.String)
    worked_from = db.Column(db.String)
    worked_to = db.Column(db.String, default = "N/A")
    currently_working = db.Column(db.String, default = "No")
    job_description = db.Column(db.String)

    app_user = db.relationship("User", backref = "log_info")

    def __repr__(self):
        return f"Job Info ID: {self.job_info_id}, User ID: {self.user_id}, Company: {self.company_name}, Title: {self.title}, Dates Worked: {self.worked_from}-{self.worked_to} Still Working? {self.currently_working}, Job Description: {self.job_description}"


class User_App(db.Model):
    """A user's job application."""

    __tablename__ = "user_app"

    app_id = db.Column(db.Integer,
                        autoincrement = True,
                        primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("app_user.user_id"))
    company_name = db.Column(db.String)
    company_link = db.Column(db.String)
    job_posting_link = db.Column(db.String)
    posted_salary = db.Column(db.String)
    followed_up = db.Column(db.String, default = "No")
    interview = db.Column(db.String, default = "No")
    hired = db.Column(db.String, default = "No")
    notes = db.Column(db.String)

    app_user = db.relationship("User", backref = "user_app")

    def __repr__(self):
        return f"App ID: {self.app_id}, User ID: {self.user_id}, Company: {self.company_name}, Company URL: {self.company_link}, Job Posting: {self.job_posting_link}, Posted Salary: {self.posted_salary}, Followed Up? {self.followed_up}, Interview? {self.interview}, Hired? {self.hired}, Notes: {self.notes}"


class Reference(db.Model):
    """A user's professional and personal references."""

    __tablename__ = "reference"

    reference_id = db.Column(db.Integer,
                            autoincrement = True,
                            primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("app_user.user_id"))
    name = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)
    address = db.Column(db.String)
    reference_type = db.Column(db.String)
    years_known = db.Column(db.Integer)
    company = db.Column(db.String, default = None)

    app_user = db.relationship("User", backref = "reference")

    def __repr__(self):
        return f"Reference ID: {self.reference_id}, User ID: {self.user_id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Address: {self.address}, Reference Type: {self.reference_type}, Years Known: {self.years_known}, Company: {self.company}"


class Interview(db.Model):
    """A user's scheduled interview."""

    __tablename__ = "interview"

    interview_id = db.Column(db.Integer,
                            autoincrement = True,
                            primary_key = True)
    app_id = db.Column(db.Integer, db.ForeignKey("user_app.app_id"))
    interview_type = db.Column(db.String)
    interview_date = db.Column(db.String)
    contact_name = db.Column(db.String)
    contact_email = db.Column(db.String)
    notes = db.Column(db.String)

    def __repr__(self):
        f"Interview ID: {self.interview_id}, App ID: {self.app_id}, Interview Type: {self.interview_type}, Interview Date: {self.interview_date}, Contact Name: {self.contact_name}, Contact Email: {self.contact_email}, Notes: {self.notes}"


class Cover_Letter(db.Model):
    """A user's cover letter."""

    __tablename__ = "cover_letter"

    cover_letter_id = db.Column(db.Integer, 
                                autoincrement = True,
                                primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("app_user.user_id"))
    upload_letter = db.Column(db.String, default = None)
    type_letter = db.Column(db.String, default = None)
    label = db.Column(db.String)

    app_user = db.relationship("User", backref = "cover_letter")

    def __repr__(self):
        f"Cover Letter ID: {self.cover_letter_id}, User ID: {self.user_id}, Upload Letter: {self.upload_letter}, Type Letter: {self.type_letter}, Label: {self.label}"


class Follow_Up(db.Model):
    """Follow ups for a user's application."""

    __tablename__ = "follow_up"

    follow_up_id = db.Column(db.Integer, 
                            autoincrement = True,
                            primary_key = True)
    app_id = db.Column(db.Integer, db.ForeignKey("user_app.app_id"))
    date = db.Column(db.Integer)
    method = db.Column(db.String)
    contact_name = db.Column(db.String)
    contact_email = db.Column(db.String)
    notes = db.Column(db.String)

    user_app = db.relationship("User_App", backref = "follow_up")

    def __repr__(self):
        f"Follow Up ID: {self.follow_up_id}, App ID: {self.app_id}, Date: {self.date}, Method: {self.method}, Contact Name: {self.contact_name}, Contact Email: {self.contact_email}, Notes: {self.notes}"


class Interview_Link(db.Model):
    """Interview links relating to a user's scheduled interview."""

    __tablename__ = "interview_link"

    interview_link_id = db.Column(db.Integer, 
                                    autoincrement = True,
                                    primary_key = True)
    interview_id = db.Column(db.Integer, db.ForeignKey("interview.interview_id"))
    link = db.Column(db.Integer)

    interview = db.relationship("Interview", backref = "interview_link")

    def __repr__(self):
        f"Inteview Link ID: {self.interview_link_id}, Interview ID: {self.interview_id}, Link: {self.link}"



if __name__ == '__main__':
    from server import app
    connect_to_db(app)