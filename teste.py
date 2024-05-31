import requests
import pandas as pd
from sqlalchemy import create_engine, inspect, text
import re

# Configurações de URLs e Token
LOCAL_API_URL = 'https://crarly.github.io/Forms/teste.py'  # URL base da sua API
API_TOKEN = 'WDGmkgdVuRzYZU6VCHF0Og'  # Seu token de acesso estático
