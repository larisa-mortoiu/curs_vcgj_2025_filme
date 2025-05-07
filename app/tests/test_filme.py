import pytest
from filme import app
import app.lib.dynasty_description as description_dy
import app.lib.dynasty_cast as cast_dy



def test_dynasty_description():
    description = description_dy.get_description()
