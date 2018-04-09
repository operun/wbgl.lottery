# -*- coding: utf-8 -*-

import random

from flask import Flask, render_template, request

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    # Defaults
    form = request.form
    blacklist = []
    form_names = []
    filtered_names = []
    random_name = ''
	# Get form
    if request.method == "POST":
        form_names = form.get('namesList', False)
        if len(form_names):
            form_names = form_names.splitlines()
            filtered_names = list(set(form_names))
            for name in blacklist:
                if name in filtered_names:
                    filtered_names.remove(name)
            random_name = random.choice(filtered_names)
    context = {
        'filtered_names': filtered_names,
        'random_name': random_name,
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run()
