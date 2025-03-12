from fastapi import FastAPI
import inngest.fast_api
from src.inngest.client import inngest_client
from src.inngest.functions import inngest_functions

app = FastAPI()

# Serve the Inngest endpoint
inngest.fast_api.serve(app, inngest_client, inngest_functions)
