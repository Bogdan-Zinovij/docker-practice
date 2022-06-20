from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'spaceship'
    app_description: str = 'Laboratory assignment 3, Bogdan Zinovij'
    app_version: str = 'dev'
    debug: bool = False
