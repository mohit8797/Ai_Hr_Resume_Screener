import json


def extract_text(response):
    """
    Robust extractor for Gemini / LangChain responses
    """

    # Case 1: Gemini returns list of message blocks
    if isinstance(response, list) and len(response) > 0:
        block = response[0]

        # Gemini text block
        if isinstance(block, dict) and "text" in block:
            return block["text"]

        return str(block)

    # Case 2: LangChain AIMessage
    if hasattr(response, "content"):
        content = response.content

        # Sometimes content itself is a list
        if isinstance(content, list) and len(content) > 0:
            if isinstance(content[0], dict) and "text" in content[0]:
                return content[0]["text"]
            return str(content[0])

        return content

    # Fallback
    return str(response)