# advanced-rag

The repository structure should reflect the architecture of the project, which represent the nodes and edges implemented.

- `graph.py` - Connects all nodes and edges.
- `state.py` - Graph state objects that will be modified during the Graph execution.
- `consts.py` - Constants used in the implementation.
- `nodes/` - Contains the implementation of all nodes that will run.
- `chains/` - Each file will be a different chain that will correspond to a node (each node will run a LangChain chain).
- `tests/` - Contains the tests for the chains.
- `ingestion.py` - Hold the logic that will download information to be indexed in the vector store

### Utilities

Installing Dependencies:
```sh
poetry add beautifulsoup4 langchain langgraph langchainhub langchain-community tavily-python langchain-chroma python-dotenv black isort pytest
```

Running tests:
```sh
pytest . -s -v
```

### Reference

- [Advanced RAG control flow with Mistral and LangChain](https://www.youtube.com/watch?v=sgnrL7yo1TE)
- [LangChain's Cookbook](https://github.com/mistralai/cookbook/tree/main/third_party/langchain)
- [langgraph-course repository from Eden Marco](https://github.com/emarco177/langgaph-course)
- [LangGraph- Develop LLM powered AI agents with LangGraph](https://www.udemy.com/course/langgraph/?couponCode=KEEPLEARNING)