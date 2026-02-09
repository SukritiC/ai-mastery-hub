import os
import fire
from dotenv import load_dotenv
import vertexai
from vertexai import agent_engines

# Load environment variables and initialize Vertex AI
load_dotenv()
vertexai.init(
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location=os.getenv("GOOGLE_CLOUD_LOCATION"),
    staging_bucket="gs://" + os.getenv("GOOGLE_CLOUD_PROJECT") + "-bucket")

# Utility functions for working with Agent Engine
def list():
    """List Agent Engine agents."""
    for agent in agent_engines.list():
        print(agent.display_name)
        print(agent.resource_name + "\n")

def delete(resource_name):
    """Delete an Agent Engine agent by its resource_name."""
    agent_engines.delete(resource_name, force=True)

if __name__ == "__main__":
    fire.Fire()