# BigQuery Agent

A GCP ADK agent with full BigQuery tooling — metadata exploration, SQL execution, forecasting, and natural language data insights.

## Prerequisites

- Python 3.14+
- [uv](https://docs.astral.sh/uv/)
- A GCP project with BigQuery enabled
- Application Default Credentials configured

## Setup

**1. Authenticate with GCP:**
```bash
gcloud auth application-default login
```

**2. Set your project:**
```bash
export GOOGLE_CLOUD_PROJECT="your-project-id"
```

**3. Install dependencies:**
```bash
uv sync
```

## Running

**Interactive web UI:**
```bash
uv run adk web
```

**CLI chat:**
```bash
uv run adk run bigquery_agent
```

## Available Tools

| Tool | Description |
|------|-------------|
| `list_dataset_ids` | List all dataset IDs in the project |
| `get_dataset_info` | Get metadata about a dataset |
| `list_table_ids` | List all table IDs in a dataset |
| `get_table_info` | Get schema and metadata for a table |
| `execute_sql` | Run a SQL query and return results |
| `forecast` | Run AI time series forecasts via `AI.FORECAST` |
| `ask_data_insights` | Answer natural language questions about table data |

## Example Prompts

- "What datasets are available in my project?"
- "Show me the schema for `my_dataset.my_table`"
- "How many rows were added to `my_dataset.events` in the last 7 days?"
- "Run a forecast on the `sales` column in `my_dataset.daily_sales`"
