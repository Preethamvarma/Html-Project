# Jannu - AI Personal Assistant

Jannu is an AI-powered personal assistant that can perform a variety of tasks such as controlling system applications, fetching weather information, playing media, performing web searches, and more, all through voice commands.

## Features
Jannu can:
1. Greet the user based on the time of day.
2. Tell the current time.
3. Provide weather reports for any given city.
4. Search queries on Google.
5. Browse websites.
6. Open, close, and launch applications on your system.
7. Shutdown, restart, or log off your PC.
8. Perform basic mathematical calculations.
9. Search Wikipedia for answers.
10. Tell jokes.
11. Play YouTube videos and songs.
12. Create and delete folders.
13. Play music and videos.
14. Fetch the latest news.

## Requirements
To run Jannu, the following libraries must be installed:
- `pyttsx3` (Text-to-Speech Engine)
- `speech_recognition` (Speech-to-Text)
- `datetime` (For getting current time)
- `wikipedia` (Wikipedia search)
- `webbrowser` (Open web pages)
- `os` (System operations)
- `wolframalpha` (For solving mathematical problems)
- `weather` (Weather information)
- `selenium` (For web browser interaction)
- `requests` (HTTP requests)
- `beautifulsoup4` (For parsing HTML content)
- `pyowm` (Weather service API)
- `youtube_dl` (For downloading videos from YouTube)
- `vlc` (For playing media)
- `urllib` (URL handling)
- `sympy` (Symbolic mathematics)

## Setup Instructions
1. **Install the necessary libraries** using `pip`:
    ```bash
    pip install pyttsx3 speechRecognition wikipedia selenium requests beautifulsoup4 pyowm youtube-dl vlc sympy
    ```

2. **Ensure your system has Python and all required libraries**.

3. **Configure API keys**:
    - For `pyowm` (OpenWeatherMap API), you need to replace `'ab0d5e80e8dafb2cb81fa9e82431c1fa'` with your actual API key in the code.

## Usage Instructions
1. **Run the Python script**:
    ```bash
    python jannu_assistant.py
    ```
    This will initialize the assistant and start listening for commands.

2. **Interaction**:
    - Jannu responds to voice commands. Some of the sample commands include:
        - "What can you do?"
        - "Search for [query] on Google"
        - "Play music"
        - "What is the current weather in [city]?"
        - "Tell me a joke"
        - "Open Visual Studio"

3. **Commands List**:
    - **General Commands**:
      - Greet: "Good morning/afternoon/evening"
      - Time: "Tell me the time"
      - Weather: "What's the weather in [city]?"
      - Wikipedia: "What is [query] in Wikipedia?"
      - Jokes: "Tell me a joke"
    - **Media**:
      - Music: "Play music [song]"
      - Video: "Play video [video name]"
      - YouTube: "Search video [song/video name]"
    - **System Operations**:
      - Open/Close Applications: "Open [app name]", "Close [app name]"
      - Shutdown/Restart/Logoff: "Shutdown", "Restart", "Logoff"

4. **System Commands**:
    - Launching Apps: You can launch applications like Visual Studio, Notepad++, Chrome, etc., using commands like "Open Visual Studio", "Close Chrome", etc.
    - You can also manage files and folders on the Desktop, such as creating or deleting folders.

## Code Explanation

1. **Text-to-Speech Engine**:
   The assistant uses `pyttsx3` for speaking back to the user. It checks the current time and greets the user accordingly.

2. **Speech Recognition**:
   It uses the `speech_recognition` library to listen to voice commands from the microphone and convert the speech into text.

3. **Command Execution**:
   Based on the recognized command, the assistant uses the `os` module for system-level tasks such as opening/closing apps, creating folders, and shutting down the system.

4. **Weather API**:
   The `pyowm` library is used for fetching the current weather for a given city using the OpenWeatherMap API.

5. **Google Search**:
   The assistant can search for queries on Google and open the results in a web browser using `webbrowser`.

6. **YouTube Integration**:
   Using `youtube_dl`, it can download videos from YouTube based on user input.

7. **Folder Management**:
   It supports creating and deleting folders on the desktop, allowing users to organize their files using voice commands.

8. **Mathematical Calculations**:
   The `wolframalpha` API is used to solve basic mathematical problems.

## Contributing

If you would like to contribute to the project:
1. Fork the repository.
2. Clone your fork locally.
3. Make your changes in a new branch.
4. Submit a pull request with a description of your changes.

