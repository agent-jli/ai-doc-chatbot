# 🤖 AI Document Chatbot

A clean, simple RAG (Retrieval-Augmented Generation) system that lets you chat with your documents using AI. Built with LangChain and powered by OpenAI, with intelligent fallback to Wikipedia for general knowledge questions.

## ✨ Features

- **Smart Document Search**: Vector-based semantic search through your document corpus
- **Intelligent Fallback**: Automatically searches Wikipedia when document corpus lacks information
- **Multiple Interfaces**: Both CLI and beautiful Streamlit web interface
- **PDF Support**: Processes PDF documents and web URLs
- **Clean Architecture**: Simple, maintainable codebase without unnecessary complexity
- **Fast Performance**: Optimized pipeline without heavy graph frameworks

## 🏗️ Architecture

```
📁 ai-doc-chatbot/
├── 🔧 src/
│   ├── config/              # Configuration management
│   ├── document_ingestion/   # PDF and URL processing
│   ├── vectorstore/         # FAISS vector storage
│   └── rag_pipeline.py      # ✨ Main RAG pipeline (replaces complex graph frameworks)
├── 🖥️ main.py              # Command-line interface
├── 🌐 streamlit_app.py     # Web interface
└── 📊 data/                # Your documents and URLs
```

### How It Works

1. **Document Processing**: PDFs and web content are chunked and embedded
2. **Vector Storage**: Documents stored in FAISS for fast semantic search
3. **Smart Retrieval**: 
   - First searches your document corpus
   - Evaluates result quality and relevance
   - Falls back to Wikipedia for general knowledge questions
   - Combines information sources when beneficial
4. **Answer Generation**: Uses OpenAI's GPT to generate comprehensive answers

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- OpenAI API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-doc-chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or using uv (recommended):
   ```bash
   uv sync
   ```

3. **Set up environment**
   ```bash
   # Create .env file with your OpenAI API key
   echo "OPENAI_API_KEY=your_api_key_here" > .env
   ```

4. **Add your documents**
   ```bash
   # Place PDF files in data/ directory
   # Or add URLs to data/urls.txt (one per line)
   ```

### Usage

#### 🖥️ Command Line Interface
```bash
python main.py
```

#### 🌐 Web Interface (Recommended)
```bash
streamlit run streamlit_app.py
```

Then open http://localhost:8501 in your browser.

## 📝 Example Questions

Try asking questions like:
- "What is the attention mechanism in transformers?"
- "Explain the key components of LLM-powered agents"
- "What are diffusion models and how do they work?"
- "Summarize the main findings in the research paper"

The system will intelligently search your documents first, then supplement with Wikipedia knowledge when needed.

## ⚙️ Configuration

### Environment Variables
```bash
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4  # Optional, defaults to gpt-4
```

### Document Sources
- **PDFs**: Place `.pdf` files in the `data/` directory
- **URLs**: Add URLs to `data/urls.txt` (one per line)
- **Mixed**: The system handles both automatically

### Customization

Edit `src/config/config.py` to modify:
- Chunk size and overlap for document processing
- Number of retrieved documents
- Model selection
- Default URLs

## 🛠️ Technical Details

### Key Components

- **SimpleRAGPipeline**: The heart of the system - handles retrieval, evaluation, and generation
- **DocumentProcessor**: Processes PDFs and web content into searchable chunks
- **VectorStore**: FAISS-based semantic search with OpenAI embeddings
- **Smart Decision Logic**: Determines when to use Wikipedia fallback

### Why This Architecture?

This system was originally built with LangGraph but was simplified for better:
- **Performance**: No complex graph execution overhead
- **Maintainability**: Clear, linear code flow
- **Debuggability**: Easy to trace and modify logic
- **Reliability**: Fewer moving parts, fewer potential failures

The simplified pipeline provides identical functionality with much cleaner code.

## 📊 Performance

- **Fast Startup**: No complex graph compilation
- **Efficient Search**: Optimized FAISS vector similarity
- **Smart Caching**: Streamlit caching for web interface
- **Minimal Dependencies**: Only essential packages

## 🔧 Development

### Project Structure
```
src/
├── config/config.py           # System configuration
├── document_ingestion/        # PDF and URL processing
│   └── document_processor.py
├── vectorstore/              # Vector storage and retrieval
│   └── vectorstore.py
└── rag_pipeline.py           # Main RAG logic
```

### Adding New Features

The clean architecture makes it easy to:
- Add new document types in `document_processor.py`
- Modify retrieval logic in `rag_pipeline.py`
- Add new data sources or APIs
- Implement custom evaluation metrics

### Testing
```bash
# Test the pipeline directly
python -c "from src.rag_pipeline import SimpleRAGPipeline; print('✅ Import successful')"

# Run with sample question
python main.py
```

## 📋 Requirements

- `langchain` - Core LLM framework
- `langchain-community` - Community integrations
- `langchain-openai` - OpenAI integration
- `openai` - OpenAI API client
- `faiss-cpu` - Vector similarity search
- `streamlit` - Web interface
- `beautifulsoup4` - Web scraping
- `pypdf` - PDF processing
- `wikipedia` - Wikipedia API access

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Troubleshooting

### Common Issues

**"No OpenAI API key found"**
- Make sure you have a `.env` file with `OPENAI_API_KEY=your_key`

**"No documents found"**
- Check that PDFs are in the `data/` directory
- Verify URLs in `data/urls.txt` are accessible

**"Import errors"**
- Run `pip install -r requirements.txt` to install all dependencies
- Use Python 3.12+ as specified in requirements

**Slow performance**
- The system builds embeddings on first run (this is normal)
- Subsequent runs use cached embeddings and are much faster

## 🔮 Future Enhancements

- Support for more document types (Word, PowerPoint, etc.)
- Advanced query preprocessing and expansion
- Multiple embedding model support
- Custom evaluation metrics
- Batch processing capabilities
- API endpoint for integration

---

Built with ❤️ using LangChain and OpenAI
