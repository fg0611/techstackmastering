from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class JobListing(db.Model):
    __tablename__ = 'job_listings'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=True)
    company = db.Column(db.Text, nullable=True)
    location = db.Column(db.Text, nullable=True)
    published = db.Column(db.Date, nullable=True)
    applicants = db.Column(db.Integer, nullable=True)
    url = db.Column(db.Text, nullable=True)
    description = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "company": self.company,
            "location": self.location,
            "published": self.published.isoformat() if self.published else None,
            "applicants": self.applicants,
            "url": self.url,
            "description": self.description
        }