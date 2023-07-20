from flask import flash, redirect, render_template

from . import app
from .forms import URLMapForm
from .models import URLMap, check_unique_short_id, get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def main_view():
    form = URLMapForm()
    if not form.validate_on_submit():
        return render_template('main_page.html', form=form)
    custom_id = form.custom_id.data
    if not custom_id:
        custom_id = get_unique_short_id()
    elif not check_unique_short_id(custom_id):
        flash(f'Имя {custom_id} уже занято!', 'link-taken')
        return render_template('main_page.html', form=form)
    url_map = URLMap(
        original=form.original_link.data,
        short=custom_id
    )
    url_map.save()
    return render_template('main_page.html', url=url_map, form=form)


@app.route('/<short_id>')
def follow_link(short_id):
    object_in_db = URLMap.query.filter_by(short=short_id).first_or_404()
    original_link = object_in_db.original
    return redirect(original_link)