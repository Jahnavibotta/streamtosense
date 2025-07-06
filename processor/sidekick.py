def get_tip(emotion):
    tips = {
        "😭 Grief": (
            "- 🧠 **Acknowledge your feelings** – Let yourself mourn without judgment.\n"
            "- 💪 **Take breaks** – Even short walks or movement help ease tension.\n"
            "- 💖 **Talk it out** – Reach out to someone you trust or journal more."
        ),
        "😢 Sadness": (
            "- 🧠 **Practice self-compassion** – You're allowed to feel low.\n"
            "- 💪 **Change your environment** – Open a window, go outside briefly.\n"
            "- 💖 **Write one positive memory** – Reconnect with something meaningful."
        ),
        "😟 Anxiety": (
            "- 🧠 **Name your worry** – Identifying the fear reduces its power.\n"
            "- 💪 **Breathe deeply** – Try box breathing: 4s in, hold, 4s out.\n"
            "- 💖 **Limit inputs** – Pause social media/news for a few hours."
        ),
        "😕 Discomfort": (
            "- 🧠 **Reflect** – Ask yourself: What triggered this feeling?\n"
            "- 💪 **Stretch** – Loosen tension in your shoulders and neck.\n"
            "- 💖 **Simplify** – Do one small task you can complete easily."
        ),
        "😐 Neutral": (
            "- 🧠 **Observe** – Neutral is not bad. Explore if it’s restful or empty.\n"
            "- 💪 **Move lightly** – Walk around the room, do 5 pushups.\n"
            "- 💖 **Try music** – Listen to a track that shifts your mood."
        ),
        "🙂 Content": (
            "- 🧠 **Anchor the feeling** – Write what made you feel this way.\n"
            "- 💪 **Keep momentum** – Do one helpful thing (organize, clean).\n"
            "- 💖 **Treat yourself gently** – Celebrate even a small win."
        ),
        "😊 Calm": (
            "- 🧠 **Savor the stillness** – You earned this.\n"
            "- 💪 **Hydrate or stretch** – Calm mind, cared body.\n"
            "- 💖 **Write 1 gratitude item** – Ground calm with meaning."
        ),
        "😄 Happy": (
            "- 🧠 **Record it** – Why are you happy? Write it down.\n"
            "- 💪 **Smile at someone** – Joy grows when shared.\n"
            "- 💖 **Be present** – Take 3 breaths to lock in this feeling."
        ),
        "🤩 Excited": (
            "- 🧠 **Visualize success** – What’s the outcome you're thrilled about?\n"
            "- 💪 **Channel energy** – Dance, sing, or create something!\n"
            "- 💖 **Pause & pace** – Don't burn out; excitement needs flow."
        ),
        "🥳 Joyful": (
            "- 🧠 **Reflect** – What brought this joy? Write 3 reasons.\n"
            "- 💪 **Celebrate** – High-five yourself or move your body!\n"
            "- 💖 **Pass it on** – Message someone and share a smile."
        )
    }

    return tips.get(emotion, "🧠 Be kind to yourself. 💪 Take a breath. 💖 You’re doing better than you think.")
