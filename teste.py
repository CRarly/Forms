import requests
import pandas as pd
from sqlalchemy import create_engine, inspect, text
import re

# Configurações de URLs e Token
LOCAL_API_URL = 'https://api.seudominio.com/'  # URL base da sua API
API_TOKEN = 'seu-token-de-acesso'  # Seu token de acesso estático
