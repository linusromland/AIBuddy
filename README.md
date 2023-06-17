# AIBuddy

AIBuddy is an AI-based Discord bot designed to enrich the user experience in your Discord server by simulating a virtual member who can actively engage in conversations. The primary objective of creating AIBuddy is to make your server more lively, unique, and interactive by using state-of-the-art AI algorithms. This project is open to collaboration; feel free to contribute and make it even better!

## Table of Contents

-   [Prerequisites](#prerequisites)
-   [Setup and Running the Project](#setup-and-running-the-project)
-   [VSCode Configuration](#vscode-configuration)
-   [Environment Variables](#environment-variables)
-   [Running the Project using Docker Compose](#running-the-project-using-docker-compose)
-   [Collaboration](#collaboration)
-   [License](#license)

## Prerequisites

1. Install [Pipenv](https://pipenv.pypa.io/en/latest/installation/) on your system.
2. (Optional) If using Visual Studio Code (VSCode) and encountering import errors, set up the interpreter and extra paths in your `settings.json` file. Read the [**VSCode Configuration**](#vscode-configuration) section below for more information.

## Setup and Running the Project

1. Clone the project repository locally.
2. In a terminal, navigate to your project folder.
3. Run `pipenv install --dev` to install the required dependencies for development.
4. Run `pipenv run start` to start the project.

To automatically reload the project when changes are made, this could be achieved using [Nodemon](https://nodemon.io/). Have [Node.JS](https://nodejs.org/en/) and [NPM](https://www.npmjs.com/)
installed on your system, and run `npx nodemon --watch src --ext py --exec pipenv run start` instead of `pipenv run start`. This will start the project using Nodemon, which will automatically reload the project when changes are made.

## VSCode Configuration

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

## Environment Variables

To run the project, you must create a `.env` file in your project root directory if you're running the project locally. For Docker, you must set the environment variables in the Docker container. The required environment variables are:

| Variable Name           | Description                    | Required |
| ----------------------- | ------------------------------ | -------- |
| DISCORD_TOKEN           | Your Discord bot token         | Yes      |
| DISCORD_SERVER_GUILD_ID | Your Discord server's guild ID | No       |
| OPENAI_API_KEY          | Your OpenAI API key            | Yes      |

To create a Discord bot and get the `DISCORD_TOKEN`, follow this tutorial: [How to create a bot for your Discord server](https://www.writebots.com/discord-bot-token/)

To obtain the `DISCORD_SERVER_GUILD_ID`, follow this tutorial: [How to get your Discord Server ID](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-)

To obtain the `OPENAI_API_KEY`, sign up for an [OpenAI](https://beta.openai.com/signup/) account. Once you've signed up, you can find your API key in the [Settings](https://beta.openai.com/account/api-keys) page.

## Running the Project using Docker Compose

#### Prerequisites

1. Ensure that [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) are installed on your system.

You can run the project in a production environment using Docker Compose. Simply run the following command in your terminal:

```
docker-compose up
```

This will start the project using the production settings defined in the `docker-compose.yml` file.

## Collaboration

This project is open to collaboration; everyone is encouraged to contribute and improve the AIBuddy experience. If you have any suggestions, feature requests, or want to help with the overall development process, feel free to open new issues or submit pull requests.

## License

AIBuddy is licensed under the [MIT License](https://opensource.org/licenses/MIT), meaning you're free to use, modify, and distribute the project, as long as the copyright notice and the permission notice are included.
