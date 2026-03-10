import os

import google.auth
from google.adk.agents import Agent
from google.adk.tools.bigquery import BigQueryCredentialsConfig, BigQueryToolset
from google.adk.tools.bigquery.config import BigQueryToolConfig

from .models import GeminiModel
from .prompt import SYSTEM_PROMPT

GOOGLE_CLOUD_PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT", "<your-project-id>")

credentials, _ = google.auth.default(
    scopes=["https://www.googleapis.com/auth/bigquery"]
)

bq_toolset = BigQueryToolset(
    credentials_config=BigQueryCredentialsConfig(credentials=credentials),
    bigquery_tool_config=BigQueryToolConfig(
        compute_project_id=GOOGLE_CLOUD_PROJECT,
    ),
)

root_agent = Agent(
    name="bigquery_agent",
    model=GeminiModel.GEMINI_2_5_FLASH,
    description="An agent that can query and analyze BigQuery data.",
    instruction=SYSTEM_PROMPT,
    tools=[bq_toolset],
)
