import argparse
import subprocess
import sys

def main():
    """
    Main function to run the TutorX application.
    This function parses command-line arguments to run the MCP server,
    the Gradio interface, or both, with customizable host and port settings.
    """
    parser = argparse.ArgumentParser(description="Run the TutorX-MCP server and/or Gradio interface.")
    parser.add_argument("--mode", type=str, choices=["mcp", "gradio", "both"], default="both",
                        help="Mode to run the application in.")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host for the MCP server.")
    parser.add_argument("--mcp-port", type=int, default=8000, help="Port for the MCP server.")
    parser.add_argument("--gradio-port", type=int, default=7860, help="Port for the Gradio interface.")
    args = parser.parse_args()

    processes = []

    if args.mode in ["mcp", "both"]:
        mcp_process = subprocess.Popen(
            [sys.executable, "main.py", f"--host={args.host}", f"--port={args.mcp_port}"]
        )
        processes.append(mcp_process)
        print(f"MCP server started on http://{args.host}:{args.mcp_port}")

    if args.mode in ["gradio", "both"]:
        gradio_process = subprocess.Popen(
            [sys.executable, "app.py", f"--server-port={args.gradio_port}"]
        )
        processes.append(gradio_process)
        print(f"Gradio interface started on http://127.0.0.1:{args.gradio_port}")

    try:
        for p in processes:
            p.wait()
    except KeyboardInterrupt:
        print("Shutting down...")
        for p in processes:
            p.terminate()

if __name__ == "__main__":
    main()