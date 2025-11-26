## Description

<!-- Please describe your changes here -->

## Type of Change

- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Refactoring
- [ ] Other (please describe)

## Checklist

- [ ] I have tested my changes locally
- [ ] I have updated documentation if needed
- [ ] My code follows the project's coding style

## Testing with adk web (GitHub Codespaces)

To verify the agent's behavior with `adk web`, reviewers can use GitHub Codespaces:

### Steps to Test

1. **Open Codespace on this PR branch**
   - Click the "Code" button on this PR
   - Select "Codespaces" tab
   - Click "Create codespace on [branch-name]"

2. **Wait for environment setup**
   - The devcontainer will automatically install dependencies
   - This takes a few minutes on first setup

3. **Configure credentials**
   - Update `.env` with your Google Cloud credentials:
     ```bash
     # Edit .env file
     PROJECT_ID=your-project-id
     LOCATION=us-central1
     MODEL_NAME=gemini-2.0-flash-exp
     ```
   - For Vertex AI authentication:
     ```bash
     gcloud auth application-default login
     ```
   - Or add `GOOGLE_API_KEY` to `.env` for Gemini API

4. **Start adk web**
   ```bash
   adk web
   ```

5. **Access the web interface**
   - Codespaces will show a notification when port 8000 is available
   - Click "Open in Browser" or access via the Ports tab
   - Select `shopping_concierge` from the dropdown menu

6. **Test the agent**
   - Try example queries like:
     - "I'm looking for a gift for my tech-savvy friend"
     - "Can you help me find a comfortable office chair under $300?"
     - "What's a good laptop for video editing?"

### Testing Checklist

- [ ] Agent responds appropriately to shopping queries
- [ ] No errors in the terminal output
- [ ] Web interface loads correctly
