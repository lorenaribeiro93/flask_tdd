from app import create_app
from flask import Flask


def test_create_app_deve_retonar_um_app_flask():
    assert isinstance(create_app(), Flask)
