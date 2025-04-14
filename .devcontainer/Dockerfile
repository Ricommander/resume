FROM python:3.12-slim

# Install necessary system packages
RUN apt-get update && apt-get install -y \
    git \
    texlive-full \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create the vscode user
RUN useradd -ms /bin/bash vscode

# Install rendercv and PyYAML
RUN pip install "rendercv[full]" PyYAML

# Set the working directory
WORKDIR /workspace

# Default command
CMD ["/bin/bash"]
