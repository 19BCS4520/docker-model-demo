# 🐳 LogGuard AI: Real-Time Docker Log Analysis

LogGuard AI is a localized, high-performance SRE tool that uses the **Docker Model Runner** to analyze container logs in real-time. By leveraging Apple Silicon's Metal acceleration via `llama.cpp`, it provides instant root-cause analysis and fix suggestions without sending a single byte of data to the cloud.

---

## 📊 System Architecture & Flow

![LogGuard AI Flow Diagram](https://raw.githubusercontent.com/19BCS4520/docker-model-demo/main/flow-diagram.png)

### How it Works:
1. **Python Log Analyzer:** Uses the `docker-py` SDK to monitor active containers.
2. **Log Stream:** Filters for `ERROR`, `FAIL`, or `Exception` keywords.
3. **Docker Model Runner:** Acts as the local AI gateway, routing requests to the optimized backend (`llama.cpp` for GGUF models).
4. **AI-Powered Insights:** Returns a 1-line fix and explanation directly to your terminal.

---

## 🚀 Why Docker Model Runner?

The **Docker Model Runner** (DMR) is a game-changer for AI development in 2026. It bridges the gap between complex AI infrastructure and the familiar Docker workflow.

### Key Benefits:
* **Hardware Autonomy:** Automatically detects your hardware (Metal on Mac, CUDA on NVIDIA, Vulkan on others) and optimizes the model without you writing a single line of driver code.
* **OpenAI-Compatible API:** Provides a standardized endpoint (`http://localhost:8000/v1`) so you can swap local models with OpenAI or Claude in your code by simply changing a URL.
* **Privacy & Cost:** Perform thousands of inference tasks for $0. Ideal for sensitive logs that cannot leave the local network.
* **Standardized Distribution:** Models are packaged as OCI-compliant artifacts, meaning you can `pull` and `run` models just like you do with container images.

---

## 🤖 Supported Local Models

Depending on your hardware constraints and use case, you can pull different models from the `ai` namespace on Docker Hub.

| Model | Parameters | Best For | Feature |
| :--- | :--- | :--- | :--- |
| **SmolLM2** | 135M - 1.7B | Rapid Prototyping | Extremely fast; runs on very low RAM (under 2GB). |
| **Llama 3.2** | 1B - 3B | General Purpose | The best "all-rounder" for general chat and reasoning. |
| **Qwen 2.5 Coder**| 3B - 7B | Coding & Regex | Specialized in generating code, fixing bugs, and writing shell scripts. |
| **Phi-3.5 Mini** | 3.8B | RAG & Docs | High reasoning capability in a small footprint; excellent for long logs. |

### Model Engine Backends:
* **llama.cpp:** Used for GGUF models. Optimized for high portability and running on commodity hardware (like your MacBook Air).
* **vLLM:** Used for Safetensors models. Designed for high-throughput and production-grade serving on NVIDIA GPUs.

---

## 🛠️ Step-by-Step Implementation

### 1. Initialize the Environment
```bash
# Enable the model runner
docker model status
docker model pull ai/smollm2
docker model run ai/smollm2