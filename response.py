import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_FEELINGS = "I'm just a bot, so I don't have feelings, but I'm here to chat with you!"
R_WEATHER = "I don't have real-time weather information, but you can check a reliable weather website for updates."
R_QUOTES = "Here's an inspiring quote: 'The only way to do great work is to love what you do.' - Steve Jobs"
R_NAME = "I'm just a bot, so you can call me whatever you like!"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response
