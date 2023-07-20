import random
import re
from datetime import datetime
from urllib.parse import urljoin

from flask import url_for

from . import db
from .const import LABELS, PATTERN, PATTERN_FOR_GEN_URL
from .error_handlers import InvalidAPIUsage


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

    @staticmethod
    def from_dict(data):
        instance = URLMap()
        for field_key, field_item in LABELS.items():
            if field_item in data:
                setattr(instance, field_key, data[field_item])
        return instance

    def save(self):
        db.session.add(self)
        db.session.commit()


def check_unique_short_id(short_link):
    return URLMap.query.filter_by(short=short_link).first() is None


def get_unique_short_id():
    short_link = ''.join(random.choices(PATTERN_FOR_GEN_URL, k=6))
    if not check_unique_short_id(short_link):
        raise InvalidAPIUsage('Число подменных url достигла ')
    return short_link
