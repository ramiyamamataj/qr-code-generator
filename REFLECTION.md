# Module 7 Reflection: Dockerizing the QR Code Generator Application

**Student Username:** ramiyamamataj  
**Environment:** WSL 2 (Ubuntu)

## 1. Key Technical Insights & Security Practices
In this module, I containerized a Python QR Code Generator application into an isolated Docker image. Key security choices in the `Dockerfile` include:
- **Non-Root Execution:** Configured a dedicated user (`myuser`) so the application processes do not execute with root privileges inside the container, reducing container escape vulnerabilities.
- **Minimal Base Image:** Selected `python:3.12-slim-bullseye` to keep the image footprint lightweight and decrease the potential attack surface.
- **Layer Optimization:** Copied `requirements.txt` prior to copying application source files to maximize Docker's layer caching mechanism when rebuilding dependencies.

## 2. Challenges Faced & Solutions
- **Ephemeral Storage vs. Persistent Volumes:** Standard container storage is ephemeral, meaning files saved inside `/app/qr_codes` vanish when the container stops. To resolve this, I configured volume mounting (`-v $(pwd)/qr_codes:/app/qr_codes`) to map local disk storage to the container path.
- **Continuous Integration Setup:** Integrating GitHub Actions required setting up encrypted repository secrets (`DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN`) to authenticate and push the `ramiyamamataj/qr-code-generator-app` image automatically upon `git push`.

## 3. DevOps Principles Applied
This workflow demonstrates core DevOps principles by bridging local development on WSL Ubuntu with automated continuous integration (CI). By automating tests and container image builds upon every commit, we eliminate host-level dependency discrepancies ("works on my machine") and guarantee repeatable deployments.
