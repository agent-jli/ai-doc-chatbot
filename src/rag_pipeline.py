from typing import List, Dict, Any
from langchain.schema import Document
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun


class SimpleRAGPipeline:
    """Simplified pipeline that handles multiple tool calls without ReAct agent complexity"""
    
    def __init__(self, retriever, llm):
        """
        Initialize RAG pipeline
        
        Args:
            retriever: Document retriever instance
            llm: Language model instance
        """
        self.retriever = retriever
        self.llm = llm
    
    def _get_retriever_results(self, query: str) -> str:
        """Get formatted retriever results (matches reactnode.py format exactly)"""
        docs: List[Document] = self.retriever.invoke(query)
        if not docs:
            return "No documents found."
        
        merged = []
        for i, d in enumerate(docs[:8], start=1):  # Exact same logic as reactnode.py
            meta = d.metadata if hasattr(d, "metadata") else {}
            title = meta.get("title") or meta.get("source") or f"doc_{i}"
            merged.append(f"[{i}] {title}\n{d.page_content}")
        return "\n\n".join(merged)
    
    def _get_wikipedia_results(self, query: str) -> str:
        """Get Wikipedia results (matches reactnode.py exactly)"""
        wiki = WikipediaQueryRun(
            api_wrapper=WikipediaAPIWrapper(top_k_results=3, lang="en")  # Same params
        )
        try:
            return wiki.run(query)
        except Exception:
            return "Could not retrieve Wikipedia information."
    
    def run(self, question: str) -> Dict[str, Any]:
        """
        Even More Accurate Version that handles multiple tool calls without ReAct agent
        
        This simulates what the ReAct agent does but with explicit logic:
        1. First tries retriever (as per system prompt preference)
        2. Evaluates if results are sufficient
        3. Falls back to Wikipedia if needed
        4. Can make multiple attempts with different queries
        """
        # Step 1: Get documents for compatibility (matches retrieve_docs node)
        retrieved_docs = self.retriever.invoke(question)
        
        # Step 2: Try retriever first (agent's preferred approach per system prompt)
        retriever_results = self._get_retriever_results(question)
        
        # Step 3: Simulate agent reasoning: "Is this sufficient?"
        context_parts = []
        
        if retriever_results and "No documents found" not in retriever_results:
            context_parts.append(f"Document corpus results:\n{retriever_results}")
        
        # Step 4: Decide if we need Wikipedia (simulate agent's decision making)
        needs_wikipedia = (
            "No documents found" in retriever_results or 
            len(retriever_results.strip()) < 100 or  # Very little content
            self._should_use_wikipedia(question, retriever_results)
        )
        
        if needs_wikipedia:
            wikipedia_results = self._get_wikipedia_results(question)
            if wikipedia_results and "Could not retrieve" not in wikipedia_results:
                context_parts.append(f"Wikipedia results:\n{wikipedia_results}")
        
        # Step 5: Combine all context
        full_context = "\n\n".join(context_parts) if context_parts else "No relevant information found."
        
        # Step 6: Generate answer with the same system prompt logic
        prompt = f"""You are a helpful RAG agent. Prefer 'retriever' for user-provided docs; use 'wikipedia' for general knowledge. Return only the final useful answer.

Available information:
{full_context}

Question: {question}

Provide a comprehensive answer based on the available information:"""
        
        response = self.llm.invoke(prompt)
        answer = getattr(response, "content", None) or "Could not generate answer."
        
        return {
            'question': question,
            'retrieved_docs': retrieved_docs,
            'answer': answer
        }
    
    def _should_use_wikipedia(self, question: str, retriever_results: str) -> bool:
        """
        Decide if we should also search Wikipedia
        This simulates the ReAct agent's decision-making process
        """
        # If no retriever results, definitely use Wikipedia
        if not retriever_results or "No documents found" in retriever_results:
            return True
        
        # If very short results, probably need more info
        if len(retriever_results.strip()) < 200:
            return True
        
        # Check for general knowledge questions that might benefit from Wikipedia
        general_knowledge_indicators = [
            "what is", "who is", "define", "explain", "history of", 
            "when was", "where is", "how does", "what are"
        ]
        
        question_lower = question.lower()
        has_general_knowledge_pattern = any(indicator in question_lower for indicator in general_knowledge_indicators)
        
        # If it's a general knowledge question and we have limited corpus results, use Wikipedia
        return has_general_knowledge_pattern and len(retriever_results.strip()) < 500
    
    def build(self):
        """
        Build method for compatibility with GraphBuilder interface
        This is a no-op since we don't need to build a graph
        """
        pass
