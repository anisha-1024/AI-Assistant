import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather

def Action(user_data):
    user_data = user_data.lower()

    if "what is your name" in user_data:
        text_to_speech.text_to_speak("My name is Anisha's Virtual Assistant")
        return "My name is Anisha's Virtual Assistant"

    elif "hello" in user_data or "hi" in user_data:
        text_to_speech.text_to_speak("Hi, sir. How can i help you?")
        return "Hi, sir. How can i help you?"
    
    elif "good morning" in user_data:
        text_to_speech.text_to_speak("Good Morning sir!")
        return "Good Morning sir!"

    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = (str)(current_time) + "Hour :", (str)(current_time.minute) + "Minute "
        text_to_speech.text_to_speak(Time)
        return Time

    elif "shutdown" in user_data:
        text_to_speech.text_to_speak("Ok sir")
        return "ok sir"

    elif "play music" in user_data:
        webbrowser.open("https://gaana.com/")
        text_to_speech.text_to_speak("gaana.com is now ready for you")
        return "gaana.com is now ready for you"

    elif "youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speak("youtube.com is now ready for you")
        return "youtube.com is now ready for you"

    elif "open google" in user_data:
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speak("google.com is now ready for you")
        return "google.com is now ready for you"

    elif "weather" in user_data:
        ans = weather.weather()
        text_to_speech.text_to_speak(ans)
        return ans

    else:
        webbrowser.open(f"https://www.google.com/search?q={user_data}")
        text_to_speech.text_to_speak(f"Here is what I found for {user_data} on google")
        return f"Searching google for {user_data}"