from flask import abort, redirect, render_template, url_for
from http import HTTPStatus

from . import db, app
from .models import URLMap
from .forms import URLMapForm
from .utils import get_unique_short_id, validate_custom_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        if form.custom_id.data not in (None, ''):
            validate_custom_id(form.custom_id.data)
            short = form.custom_id.data
        else:
            short = get_unique_short_id()
        url_map = URLMap(
            original=form.original_link.data,
            short=short,
        )
        db.session.add(url_map)
        db.session.commit()
        return render_template(
            'index.html',
            form=form,
            short=url_for('index_view', _external=True) + url_map.short
        )
    return render_template('index.html', form=form)


@app.route('/<string:short>', methods=['GET'])
def redirect_view(short):
    url_map = URLMap.query.filter_by(short=short).first()
    if url_map is None:
        abort(HTTPStatus.NOT_FOUND)
    return redirect(url_map.original, HTTPStatus.FOUND)
