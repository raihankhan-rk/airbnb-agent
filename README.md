# Airbnb Agent

An AI-powered agent that interacts with Airbnb to find and display listing information based on natural language queries.

## Description

This project uses the Agno framework with GPT-4o to create an intelligent agent that can search Airbnb listings using natural language. The agent can understand complex queries and return detailed information about available accommodations.

## Features

- Natural language processing for Airbnb searches
- Detailed listing information including prices, ratings, and contact details
- Formatted responses with tabular data

## Prerequisites

- Python 3.8+
- Node.js and npm

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/raihankhan-rk/airbnb-agent.git
   cd airbnb-agent
   ```

2. Install Python dependencies:
   ```
   uv sync
   ```

3. Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the agent with a natural language query:

```python
uv run cli.py
```

You can modify the query in `cli.py` to search for different listings with various parameters:

Example query:
```
"What listings are available in San Francisco for 4 people for 3 nights from 15 to 18 June 2024?"
```

## Example Response

The agent will return formatted information about available listings, including:
- Hotel/property names
- Prices
- Locations
- Ratings
- Contact information
- Addresses

## License

[MIT](LICENSE)