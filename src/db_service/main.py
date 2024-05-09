import sys
from fastapi import FastAPI

from db.database import init_db
from contextlib import asynccontextmanager

