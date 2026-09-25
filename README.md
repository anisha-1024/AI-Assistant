# ANISHA'S AI Voice Assistant 🤖

Anisha's AI Voice Assistant is a Python-based desktop voice assistant that listens to your voice commands, performs actions, and speaks back to you. It can open websites, tell time, give weather updates, and search anything on Google if it doesn't understand the command.

This project was built as a part of Third Year Python Project.

### ✨ Demo
> You say: "Open YouTube" -> It opens YouTube  
> You say: "What is the time" -> It speaks the current time  
> You say: "Who is APJ Abdul Kalam" -> It searches Google for it

### 🚀 Features
- **Voice Controlled:** Uses Speech Recognition to understand commands
- **Text to Speech:** Talks back using pyttsx3
- **Smart Actions:** 
    - Open Google, YouTube, Gmail, News
    - Tell current time and date
    - Get live weather of any city
    - Play songs / videos
- **Google Fallback:** If command is not in the list (like 6-7 conditions), it automatically searches it on Google instead of saying "I don't understand"
- **Simple GUI:** Easy to use interface built with Tkinter / CustomTkinter

### 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Libraries:** 
    - `speech_recognition` - for voice input
    - `pyttsx3` - for text to speech
    - `webbrowser` - to open browser
    - `requests` - for weather API
    - `tkinter` - for GUI

### 📁 Project Structure
