"""
TutorX-MCP Gradio Web Interface

This script launches the Gradio web UI, providing a user-friendly
interface for interacting with the TutorX MCP tools.
"""
import gradio as gr
import uuid
from mcp.client.session_group import ClientSessionGroup, StreamableHttpParameters

# Global variable to hold the session group, initialized lazily.
mcp_client_group = None

async def get_mcp_client():
    """
    Initializes and returns a singleton MCP client session group.
    Uses lazy initialization to create the client on first use.
    """
    global mcp_client_group
    if mcp_client_group is None:
        print("Initializing MCP client for the first time...")
        server_params = StreamableHttpParameters(url="http://127.0.0.1:8000/mcp")
        group = ClientSessionGroup()
        await group.__aenter__()
        await group.connect_to_server(server_params)
        mcp_client_group = group
        print("MCP client connected.")
    return mcp_client_group

def create_gradio_interface():
    """
    Creates and returns the Gradio interface for TutorX.
    """
    with gr.Blocks(theme=gr.themes.Soft()) as demo:
        gr.Markdown("# Welcome to TutorX-MCP!")
        gr.Markdown("Your personal AI-powered tutor. Select a tool from the tabs below.")

        with gr.Tab("AI Tutor"):
            gr.Markdown("## AI Tutoring Session")
            session_id_state = gr.State(None)
            student_id_state = gr.State(str(uuid.uuid4()))

            chatbot = gr.Chatbot(label="Tutor Chat", height=500)
            msg = gr.Textbox(label="Your message", placeholder="Type your question here...")
            clear = gr.Button("Clear")

            async def handle_chat_message(session_id, student_id, message, chat_history):
                client = await get_mcp_client()
                if not client:
                    chat_history.append((message, "Error: Could not connect to MCP Client."))
                    yield chat_history, session_id
                    return

                if not message:
                    return

                chat_history.append((message, None))
                yield chat_history, session_id

                # Start a new session if one doesn't exist
                if session_id is None:
                    try:
                        result = await client.call_tool(
                            "start_tutoring_session",
                            {"student_id": student_id, "topic": "General Tutoring"}
                        )
                        session_id = result.structuredContent.get("session_id")
                        if not session_id:
                            raise Exception(result.structuredContent.get("error", "Failed to start session."))
                    except Exception as e:
                        chat_history[-1] = (message, f"Error starting session: {e}")
                        yield chat_history, None
                        return

                # Call the AI tutor chat tool
                try:
                    response = await client.call_tool(
                        "ai_tutor_chat",
                        {"session_id": session_id, "message": message}
                    )
                    ai_response = response.structuredContent.get("response")
                    if not ai_response:
                         raise Exception(response.structuredContent.get("error", "AI did not return a response."))
                except Exception as e:
                    ai_response = f"Error communicating with AI: {e}"

                chat_history[-1] = (message, ai_response)
                yield chat_history, session_id

            msg.submit(handle_chat_message, [session_id_state, student_id_state, msg, chatbot], [chatbot, session_id_state])
            clear.click(lambda: (None, None, None), None, [chatbot, msg, session_id_state], queue=False)


        with gr.Tab("Quiz Generator"):
            gr.Markdown("## AI-Powered Quiz Generation")
            with gr.Row():
                quiz_concept = gr.Textbox(label="Quiz Topic", placeholder="e.g., Photosynthesis")
                quiz_difficulty = gr.Dropdown(["easy", "medium", "hard"], label="Difficulty", value="medium")
                quiz_num_questions = gr.Slider(minimum=1, maximum=10, value=5, step=1, label="Number of Questions")

            generate_quiz_btn = gr.Button("Generate Quiz")
            quiz_output = gr.Markdown(label="Generated Quiz", value="Your quiz will appear here...")

            async def handle_quiz_generation(concept, difficulty, num_questions):
                client = await get_mcp_client()
                if not client:
                    yield "Error: Could not connect to MCP Client."
                    return

                if not concept:
                    yield "Error: Please enter a quiz topic."
                    return

                yield "Generating your quiz, please wait..."

                try:
                    result = await client.call_tool(
                        "generate_quiz_tool",
                        {
                            "concept_name": concept,
                            "difficulty": difficulty,
                            "num_questions": int(num_questions)
                        }
                    )
                    quiz_data = result.structuredContent

                    if "error" in quiz_data:
                        yield f"### Error Generating Quiz\n`{quiz_data['error']}`"
                        return

                    # Format the quiz data into markdown
                    md = f"### Quiz on {quiz_data.get('concept', 'N/A')}\n"
                    md += f"**Difficulty:** {quiz_data.get('difficulty', 'N/A')}\n---\n"

                    for i, q in enumerate(quiz_data.get('questions', []), 1):
                        md += f"**Question {i}:** {q.get('question_text', 'N/A')}\n\n"
                        md += "**Options:**\n"
                        for opt in q.get('options', []):
                            md += f"- {opt}\n"
                        md += f"\n**Correct Answer:** `{q.get('correct_answer', 'N/A')}`\n\n---\n"

                    yield md

                except Exception as e:
                    yield f"### An Unexpected Error Occurred\n`{e}`"

            generate_quiz_btn.click(
                handle_quiz_generation,
                inputs=[quiz_concept, quiz_difficulty, quiz_num_questions],
                outputs=[quiz_output]
            )

    return demo

if __name__ == "__main__":
    app = create_gradio_interface()
    app.queue().launch()