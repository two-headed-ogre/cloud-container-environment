# Cloud Container Environment

This is a cloud-based development environment that can be accessed through a browser. It's set up with various tools and utilities to get you started with development right away.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/two-headed-ogre/cloud-container-environment)

## Features

- Pre-installed development tools:
  - Python with essential data science packages
  - Node.js with TypeScript
  - UV package manager for fast Python dependency management
  - Simple web server for testing

## Getting Started

1. Click the "Open in Gitpod" button above
2. Wait for the environment to initialize
3. Access the web server at port 8080
4. Use the terminal to execute commands and test code
5. Install additional packages as needed

## How to Use

The environment starts automatically with a simple web server running. You can modify the code in the `public` directory to see changes reflected in the browser.

## Adding Dependencies

- For Python packages: `uv pip install [package-name]`
- For Node.js packages: `npm install [package-name]`

## Environment Configuration

The environment is configured in the `.gitpod.yml` file. You can modify this file to add additional tools, change ports, or adjust other settings.