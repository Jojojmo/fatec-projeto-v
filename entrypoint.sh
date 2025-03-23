#!/bin/bash

# Start Ollama in the background.
/bin/ollama serve &
# Record Process ID.
pid=$!

# Pause for Ollama to start.
sleep 5

echo "🔴 Recuperar modelo LLAMA3.1..."
ollama pull llama3.1
echo "🟢 Finalizado!"

# Wait for Ollama process to finish.
wait $pid