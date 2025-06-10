# More info about the API Specification: https://github.com/ollama/ollama/blob/main/docs/api.md
curl -X POST http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{
        "prompt":"List of things to do in Guayaquil, Ecuador",
        "model":"llama3.2",
        "stream":false,
        "format":"json"
      }'
