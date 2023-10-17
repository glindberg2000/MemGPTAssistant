#!/bin/bash

# Create main.py
touch main.py

# Create requirements.txt
touch requirements.txt

# Create essential folders
mkdir models static templates

# Initialize Git
git add .
git commit -m "Initial project setup"

# Display message
echo "Project initialized successfully!"
