#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import orjson
from pydantic import BaseModel as PyDanticBaseModel


def orjson_dumps(v, *, default):
    # orjson.dumps returns bytes, to match standard json.dumps we need to decode
    return orjson.dumps(v, default=default).decode()


class BaseModel(PyDanticBaseModel):
    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps
