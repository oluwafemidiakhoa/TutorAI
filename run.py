"""
TutorX-MCP Runner

This script provides a command-line interface to run the MCP server,
the Gradio web interface, or both concurrently.
"""
import argparse
import multiprocessing
import uvicorn
from app import create_gradio_interface
from main import app as fastapi_app

def run_mcp_server(host, port):
    """Runs the MCP FastAPI server."""
    print(f"Starting MCP server on http://{host}:{port}")
    uvicorn.run(fastapi_app, host=host, port=port)

def run_gradio_app(host, port):
    """Runs the Gradio web interface."""
    print(f"Starting Gradio interface on http://{host}:{port}")
    gradio_app = create_gradio_interface()
    gradio_app.launch(server_name=host, server_port=port)

def main():
    """Parses command-line arguments and starts the selected services."""
    parser = argparse.ArgumentParser(description="Run TutorX-MCP Server and/or Gradio UI.")
    parser.add_argument(
        "--mode",
        type=str,
        choices=["mcp", "gradio", "both"],
        default="both",
        help="Mode to run the application in."
    )
    parser.add_argument("--host", type=str, default="127.0.0.1", help="Host for the servers.")
    parser.add_argument("--mcp-port", type=int, default=8000, help="Port for the MCP server.")
    parser.add_argument("--gradio-port", type=int, default=7860, help="Port for the Gradio UI.")
    args = parser.parse_args()

    if args.mode == "both":
        p1 = multiprocessing.Process(target=run_mcp_server, args=(args.host, args.mcp_port))
        p2 = multiprocessing.Process(target=run_gradio_app, args=(args.host, args.gradio_port))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
    elif args.mode == "mcp":
        run_mcp_server(args.host, args.mcp_port)
    elif args.mode == "gradio":
        run_gradio_app("0.0.0.0", args.gradio_port)


if __name__ == "__main__":
    main()