from pytest import fixture
from flask import template_rendered

from app import create_app


@fixture
def app():
    app = create_app()
    app.config['TESTING'] = True

    yield app


@fixture
def client(app):
    with app.test_client() as client:
        yield client


@fixture
def templates(app):
    templates = []

    def gravador_de_templates(remetente, template, context, **extra):
        templates.append(template)

    template_rendered.connect(gravador_de_templates, app)

    yield templates

    template_rendered.disconnect(gravador_de_templates, app)
