# AIBuddy

AIBuddy: A friendly AI-based Discord bot that simulates a virtual server member, engaging in conversations and bringing a unique, interactive experience to your server.

## Project Setup for Local Development

### Prerequisites

1. Install [Pipenv](https://pipenv.pypa.io/en/latest/installation/) on your system.
2. (Optional) If using Visual Studio Code (VSCode) and encountering import errors, set up the interpreter and extra paths in your `settings.json` file. Read the **VSCode Configuration** section below for more information.

### Setup and Running the Project

1. Clone the project repository locally.
2. In a terminal, navigate to your project folder.
3. Run `pipenv install --dev` to install the required dependencies for development.
4. Run `pipenv run start` to start the project.

### VSCode Configuration

If you're using Visual Studio Code and are encountering import errors, follow these steps:

1. Find the path to your Pipenv environment's Python executable:

    - Open a Command Prompt or PowerShell in your project folder.
    - Run `pipenv shell` to activate the virtual environment.
    - Run `where python` (on Windows) or `which python` (on Unix-based systems) to get the path to the Python interpreter.

2. Find the `site-packages` directory in your Pipenv environment. It is usually located inside the `Lib` folder in the virtual environment directory, e.g.:

    ```
    C:\Users\YourUsername\.virtualenvs\your-project-name-xyz12345\Lib\site-packages
    ```

3. Open your project in VSCode, and go to the `.vscode` folder. If it doesn't exist, create it.
4. Inside the `.vscode` folder, create or edit the `settings.json` file.
5. Add/update the following JSON snippet in the `settings.json` file, replacing the paths with your actual paths:

```json
{
	"python.pythonPath": "your_interpreter_path_here",
	"python.autoComplete.extraPaths": ["your_site_packages_path_here"],
	"python.analysis.extraPaths": ["your_site_packages_path_here"]
}
```

For example (paths shown are for Windows, use single forward slashes `/` on Unix-based systems):

```json
{
	"python.pythonPath": "C:\\Users\\YourUsername\\.virtualenvs\\your-project-name-xyz12345\\Scripts\\python.exe",
	"python.autoComplete.extraPaths": ["C:\\Users\\YourUsername\\.virtualenvs\\your-project-name-xyz12345\\Lib\\site-packages"],
	"python.analysis.extraPaths": ["C:\\Users\\YourUsername\\.virtualenvs\\your-project-name-xyz12345\\Lib\\site-packages"]
}
```

Remember to use double backslashes (`\\`) in path strings within the JSON file on Windows, and single forward slashes (`/`) on Unix-based systems.

### Running the Project using Docker Compose

#### Prerequisites

1. Ensure that [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) are installed on your system.

You can run the project in a production environment using Docker Compose. Simply run the following command in your terminal:

```
docker-compose up
```

This will start the project using the production settings defined in the `docker-compose.yml` file.
