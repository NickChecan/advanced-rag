from typing import Any, Dict

from langchain.schema import Document
from langchain_community.tools.tavily_search import TavilySearchResults

from graph.state import GraphState
# from dotenv import load_dotenv

# load_dotenv()
# web_search_tool = TavilySearchResults(max_results=3)
web_search_tool = TavilySearchResults(k=3)

def web_search(state: GraphState) -> Dict[str, Any]:
    print("---WEB SEARCH---")
    question = state["question"]
    # documents = state["documents"]
    documents = state.get("documents", [])

    docs = web_search_tool.invoke({"query": question})
    # tavily_results = web_search_tool.invoke({"query": question})
    # joined_tavily_result = "\n".join(
    #     [tavily_result["content"] for tavily_result in tavily_results]
    # )
    # web_results = Document(page_content=joined_tavily_result)
    web_results = "\n".join([d["content"] for d in docs])
    web_results = Document(page_content=web_results)
    if documents is not None:
        documents.append(web_results)
    else:
        documents = [web_results]
    return {"documents": documents, "question": question}


# if __name__ == "__main__":
#     web_search(state={"question": "agent memory", "documents": None})