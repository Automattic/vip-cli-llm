# LLM CLI Setup for Querying VIP-CLI Documentation

This guide helps you install and configure [LLM CLI](https://llm.datasette.io/en/stable/index.html), download the [VIP CLI](https://docs.wpvip.com/vip-cli/) documentation, and create a queryable local AI assistant using OpenAI.

---

## 🔧 Installation

### macOS

1. Install LLM CLI:
    ```bash
    brew install llm
    ```

2. Install `html2text`:
    ```bash
    brew install html2text
    ```

### Linux (Debian/Ubuntu)

1. Install Python and pip:
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip -y
    ```

2. Install LLM CLI:
    ```bash
    pip3 install llm
    ```

3. Install `html2text`:
    ```bash
    sudo apt install html2text -y
    ```

### Windows

1. Install Python from [python.org](https://www.python.org/downloads/)

2. Open Command Prompt or PowerShell and install LLM CLI:
    ```powershell
    pip install llm
    ```

3. Install `html2text`:
    ```powershell
    pip install html2text
    ```

4. Use `wget` via [Gow](https://github.com/bmatzelle/gow/releases), [Cygwin](https://www.cygwin.com/), or WSL. Alternatively, download pages manually and use a script to convert them.

---

## 🔐 API Setup

Set your OpenAI API key:

```bash
llm keys set openai
```

---

## 🧪 Basic Test

Verify LLM CLI is working:

```bash
llm "What is the capital of United States"
```

---

## ⚙️ Default Model Configuration

Set GPT-4.1 as the default model:

```bash
llm models default gpt-4.1
```

**Note:** GPT-4.1 is recommended because it has a context window of 1M tokens. This larger context window is essential for effectively processing and querying the VIP-CLI documentation, as it allows the model to maintain more context from the documentation while answering questions.

---

## 📥 Download VIP-CLI Documentation

Use `wget` to recursively download the VIP CLI documentation:

```bash
wget --recursive --no-parent --wait=0.1 --convert-links --timestamping  https://docs.wpvip.com/vip-cli/
```

**Parameter Explanations:**
- `--recursive`: Downloads the entire website structure recursively
- `--no-parent`: Prevents wget from following links to parent directories
- `--wait=0.1`: Adds a 0.1 second delay between requests to avoid overwhelming the server
- `--convert-links`: Converts links in downloaded files to point to local files
- `--timestamping`: Only downloads files if they're newer than local copies

**Target Directory Structure:**
The documentation will be downloaded to `docs.wpvip.com/vip-cli/` with the following structure:
- `docs.wpvip.com/vip-cli/`: Root directory containing all documentation
- `docs.wpvip.com/vip-cli/commands/`: Contains command-specific documentation
- `docs.wpvip.com/vip-cli/getting-started/`: Contains setup and installation guides
- `docs.wpvip.com/vip-cli/reference/`: Contains reference documentation

If using Windows, you can install `wget` using Chocolatey:

```powershell
choco install wget
```

---

## 🧠 Create a Queryable LLM Context

### 1. Convert HTML Files to Text

```bash
find ./docs/docs.wpvip.com -name "*.html" | xargs -I {} html2text {} >> context/vip-cli-context.txt
```

**Command Breakdown:**
- `find ./docs.wpvip.com`: Searches in the downloaded documentation directory
- `-name "*.html"`: Matches all HTML files
- `xargs -I {}`: Takes each found file and passes it to the next command
- `html2text {}`: Converts HTML content to plain text
- `>> vip-cli-context.txt`: Appends the converted text to the context file

**Note for Windows:** Use WSL or convert manually using `html2text`:

```powershell
Get-ChildItem -Recurse -Filter *.html | ForEach-Object { html2text $_.FullName } >> context.txt
```

### 2. Create a Named Fragment

```bash
llm fragments set vip-cli ./context/vip-cli-context.txt
```

Set a frament for instructions:
```bash
llm fragments set instructions ./context/vip-cli-instructions.txt
```
---

## 🏷️ Optional: Shell Alias for Repeated Use

### macOS/Linux:

Add to `~/.bashrc` or `~/.zshrc`:

```bash
alias vip-cli-ai='llm -f vip-cli  -f instructions '
source ~/.zshrc  # or ~/.bashrc
```

### Windows (PowerShell):

```powershell
Set-Alias vip-cli-ai "llm -f vip-cli -f instructions "
```

---

## 🤖 Query VIP-CLI AI Assistant

Ask questions like:

```bash
vip-cli-ai "How can I trigger a backup?"
vip-cli-ai "What is the command to clear the object cache?"
```

### Formatting Output with Glow

For better markdown formatting, pipe the output through Glow:

```bash
# Install Glow
brew install glow  # macOS
sudo apt install glow  # Linux
choco install glow  # Windows

# Use with LLM CLI
vip-cli-ai "How can I trigger a backup?" | glow

# For non-streaming mode with formatting
vip-cli-ai --no-stream "How can I trigger a backup?" | glow
```

**Note:** Glow provides syntax highlighting and proper markdown rendering in the terminal.

### Interactive Chat Interface

For interactive conversations with the VIP-CLI documentation, use the LLM chat interface:

```bash
# Start an interactive chat session
llm chat -f vip-cli -f instructions

# Example chat session
> How do I use the backup command?
[AI responds with backup command details]
> Can you show me an example with the --site flag?
[AI provides example with site flag]
> exit  # or Ctrl+D to end the session
```

**Chat Interface Features:**
- Maintains conversation context
- Supports multi-turn interactions
- Allows for follow-up questions
- Preserves both VIP-CLI documentation and instructions context

---

## 📝 Notes

- To persist and share LLM context across sessions, use `llm embed` with the `--store` flag:
    ```bash
    llm embed --input context.txt --store --collection vip-cli-docs
    ```

- You can check which fragments are available:
    ```bash
    llm fragments list
    ```

- Delete old fragments if needed:
    ```bash
    llm fragments delete vip-cli
    ```

---

## 📚 Resources

- [LLM CLI Documentation](https://llm.datasette.io/)
- [VIP CLI Documentation](https://docs.wpvip.com/vip-cli/)
- [OpenAI API Key Setup](https://platform.openai.com/account/api-keys)

---

