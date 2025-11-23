"""Deployment script for the Shopping Concierge Agent to Vertex AI Agent Engine."""

import argparse
import os
from pathlib import Path

from vertexai import agent_engines


def deploy_agent(project_id: str, location: str, agent_path: str):
    """
    Deploy the Shopping Concierge Agent to Vertex AI Agent Engine.
    
    Args:
        project_id: Google Cloud Project ID
        location: Google Cloud location (e.g., us-central1)
        agent_path: Path to the agent wheel file
    """
    print(f"Deploying agent to project {project_id} in location {location}...")
    
    
    print("Deployment script template - implement actual deployment logic here")
    print(f"Agent path: {agent_path}")
    


def delete_agent(resource_id: str):
    """
    Delete a deployed agent from Vertex AI Agent Engine.
    
    Args:
        resource_id: The resource ID of the agent to delete
    """
    print(f"Deleting agent with resource ID: {resource_id}")
    
    
    print("Deletion script template - implement actual deletion logic here")
    


def main():
    """Main deployment script."""
    parser = argparse.ArgumentParser(
        description="Deploy or delete the Shopping Concierge Agent"
    )
    parser.add_argument(
        "--delete",
        action="store_true",
        help="Delete the agent instead of deploying",
    )
    parser.add_argument(
        "--resource_id",
        type=str,
        help="Resource ID for deletion",
    )
    parser.add_argument(
        "--project_id",
        type=str,
        default=os.getenv("PROJECT_ID"),
        help="Google Cloud Project ID",
    )
    parser.add_argument(
        "--location",
        type=str,
        default=os.getenv("LOCATION", "us-central1"),
        help="Google Cloud location",
    )
    
    args = parser.parse_args()
    
    if args.delete:
        if not args.resource_id:
            print("Error: --resource_id is required for deletion")
            return
        delete_agent(args.resource_id)
    else:
        if not args.project_id:
            print("Error: PROJECT_ID environment variable or --project_id is required")
            return
        
        deployment_dir = Path(__file__).parent
        wheel_files = list(deployment_dir.glob("*.whl"))
        
        if not wheel_files:
            print("Error: No wheel file found in deployment directory")
            print("Run 'uv build --wheel --out-dir deployment' first")
            return
        
        agent_path = str(wheel_files[0])
        deploy_agent(args.project_id, args.location, agent_path)


if __name__ == "__main__":
    main()
