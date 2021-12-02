from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from model import db, User, User_Link, Resume_Bio, Job_Info, User_App, Reference, Interview, Cover_Letter, Follow_Up, Interview_Link 


def create_user(username, fname, lname, job_title, email, password, city, state, picture):
    """Create and return a new user."""

    user = User(username = username,
                fname = fname, 
                lname = lname,
                job_title = job_title,
                email = email,
                password = password,
                city = city,
                state = state,
                picture = picture)

    db.session.add(user)
    db.session.commit()

    return user


def create_user_link(user_id, portfolio_id, github_url, linkedin_url, other_url):
    """Create a new link on a user's profile."""

    user_link = User_Link(user_id = user_id,
                        portfolio_url = portfolio_id,
                        github_url = github_url,
                        linkedin_url = linkedin_url,
                        other_url = other_url)

    db.session.add(user_link)
    db.session.commit()

    return user_link


def create_resume_or_bio(user_id, upload_resume, type_resume, bio, label):
    """Creates a new resume or bio for a user."""

    resume_or_bio = Resume_Bio(user_id = user_id,
                                upload_resume = upload_resume,
                                type_resume = type_resume,
                                bio = bio,
                                label = label)

    db.session.add(resume_or_bio)
    db.session.commit()

    return resume_or_bio


def create_job_info(user_id, company_name, title, worked_from, worked_to, currently_working, job_description):
    """Adds previous job information to a user's profile."""

    job_info = Job_Info(user_id = user_id,
                        company_name = company_name,
                        title = title,
                        worked_from = worked_from,
                        worked_to = worked_to,
                        currently_working = currently_working,
                        job_description = job_description)

    db.session.add(job_info)
    db.session.commit()

    return job_info
    

def create_user_app(user_id, company_name, company_link, job_posting_link, posted_salary, followed_up, interview, hired, notes):
    """Adds an application to a user's profile."""

    user_app = User_App(user_id = user_id,
                        company_name = company_name,
                        company_link = company_link,
                        job_posting_link = job_posting_link,
                        posted_salary = posted_salary,
                        followed_up = followed_up,
                        interview = interview,
                        hired = hired,
                        notes = notes)

    db.session.add(user_app)
    db.session.commit()

    return user_app


def create_reference(user_id, name, email, phone, address, reference_type, years_known, company):
    """Adds a personal or professional reference to a user's profile."""

    reference = Reference(user_id = user_id,
                        name = name,
                        email = email,
                        phone = phone, 
                        address = address,
                        reference_type = reference_type,
                        years_known = years_known,
                        company = company)

    db.session.add(reference)
    db.session.commit()

    return reference


def create_interview(app_id, interview_type, interview_date, contact_name, contact_email, notes):
    """Adds a scheduled interview to a user's profile."""

    interview = Interview(app_id = app_id,
                        interview_type = interview_type,
                        interview_date = interview_date,
                        contact_name = contact_name,
                        contact_email = contact_email,
                        notes = notes)
    
    db.session.add(interview)
    db.session.commit()

    return interview


def create_cover_letter(user_id, upload_letter, type_letter, label):
    """Adds a cover letter to a user's profile."""

    cover_letter = Cover_Letter(user_id = user_id,
                                upload_letter = upload_letter,
                                type_letter = type_letter,
                                label = label)

    db.session.add(cover_letter)
    db.session.commit()

    return cover_letter


def create_follow_up(app_id, date, method, contact_name, contact_email, notes):
    """Adds a follow up to a user's application."""

    follow_up = Follow_Up(app_id = app_id,
                        date = date,
                        method = method,
                        contact_name = contact_name,
                        contact_email = contact_email,
                        notes = notes)

    db.session.add(follow_up)
    db.session.commit()

    return follow_up


def create_interview_link(interview_id, link):
    """Adds a link to a user's scheduled interview."""

    interview_link = Interview_Link(interview_id = interview_id, 
                                    link = link)

    db.session.add(interview_link)
    db.session.commit()

    return interview_link


def get_username(email):
    """Gets a user's username by email."""

    return User.query.filter(User.username == email).first()


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


def get_user_fname(email):
    """Return a user's first name by email."""

    users = User.query.all()

    for user in users:
        if user.email == email:
            return user.fname


def get_user_lname(email):
    """Return a user's last name by email."""

    users = User.query.all()

    for user in users:
        if user.email == email:
            return user.lname

def get_user_city(email):
    """Return a user's city by email."""

    users = User.query.all()

    for user in users:
        if user.email == email:
            return user.city

def get_user_state(email):
    """Return a user's state by email."""

    users = User.query.all()

    for user in users:
        if user.email == email:
            return user.state

def get_user_job_title(email):
    """Return a user's job title by email."""

    users = User.query.all()

    for user in users:
        if user.email == email:
            return user.job_title

def get_user_photo(email):
    """Returns a user's photo by email."""

    users = User.query.all()

    for user in users:
        if user.email == email:
            return user.picture


def login_user(email, password):
    """Returns a user by email and password."""

    return User.query.filter(User.email == email, User.password == password).first()


def user_username(username):
    """Return a username by email."""

    return User.query.filter(User.username == username).first()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)