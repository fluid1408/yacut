from datetime import datetime
from urllib.parse import urljoin
from flask import url_for

from . import db
from .const import LABELS


class URLMap(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String, nullable=False)
    short = db.Column(db.String(16), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=urljoin(
                url_for('main_view', _external=True), self.short)
        )

    def from_dict(self, data):
        for field_key, field_item in LABELS.items():
            if field_item in data:
                setattr(self, field_key, data[field_item])