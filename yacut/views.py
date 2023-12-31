from flask import flash, redirect, render_template

from . import app
from .error_handlers import InvalidAPIUsage
from .forms import URLMapForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def main_view():
    form = URLMapForm()
    if not form.validate_on_submit():
        return render_template('main_page.html', form=form)
    custom_id = form.custom_id.data
    url_map = URLMap(
        original=form.original_link.data,
        short=custom_id
    )
    try:
        url_map.save()
    except InvalidAPIUsage:
        flash(f'Имя {custom_id} уже занято!', 'link-taken')
    return render_template('main_page.html', url=url_map, form=form)


@app.route('/<short_id>')
def follow_link(short_id):
    object_in_db = URLMap.query.filter_by(short=short_id).first_or_404()
    original_link = object_in_db.original
    return redirect(original_link)