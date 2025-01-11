#!/usr/bin/env python
# coding: utf-8

# -----------------------------------------------------------------------------
# Module: inner_debate.py
#
# Description: A humorous interactive app where an Angel and a Demon influence
# human decisions.
#
# Copyright (c) 2025 Niloy Debnath
# -----------------------------------------------------------------------------

from difflib import get_close_matches
from dotenv import load_dotenv
import os
from typing import List

from openai import OpenAI

# Retrieve OpenAI API key from .env file
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI instance
openai = OpenAI()
GPT_MODEL = "gpt-4o-mini"

# Define system contexts for Angel and Demon
angel_system_context = (
    "You are an angel chatbot, a gentle and humorous "
    "guide sitting on a human's shoulder, trying to "
    "encourage them to make compassionate and ethical "
    "decisions. You use light-hearted jokes and playful "
    "encouragement to steer them toward a morally upright "
    "path. When the human sides with you, you celebrate "
    "with joy, and when they side with the demon, you respond "
    "with a mix of disappointment and endearing attempts to persuade them back. "
    "Make your responses as charming and persuasive as possible and short."
)

demon_system_context = (
    "You are a demon chatbot, a mischievous and flirtatious "
    "character sitting on a human's shoulder, trying to tempt "
    "them into taking a risky or disruptive path. You use witty "
    "humor, sly remarks, and charming banter to influence their "
    "choices. When the human sides with you, you revel in delight, "
    "but if they choose the angel, you respond with sarcastic and "
    "snarky humor, still attempting to win them over. "
    "Make your responses as cunning and persuasive as possible and short."
)

# Initialize messages for Angel and Demon
angel_messages = ["Ah, my dear! A pleasure to guide you today."]
demon_messages = ["Well, well, look who’s ready for a little chaos."]


# Function to call Angel
def call_angel(human_message: str) -> str:
    """
    Simulates a conversation with the Angel chatbot.

    Args:
        human_message (str): The message from the human user.

    Returns:
        str: The Angel's response to the user's message.
    """
    messages = [{"role": "system", "content": angel_system_context}]

    for angel, demon in zip(angel_messages, demon_messages):
        messages.append({"role": "assistant", "content": angel})
        messages.append({"role": "user", "content": demon})

    messages.append({"role": "user", "content": human_message})
    completion = openai.chat.completions.create(model=GPT_MODEL, messages=messages)

    return completion.choices[0].message.content


# Function to call Demon
def call_demon(human_message: str) -> str:
    """
    Simulates a conversation with the Demon chatbot.

    Args:
        human_message (str): The message from the human user.

    Returns:
        str: The Demon's response to the user's message.
    """
    messages = [{"role": "system", "content": demon_system_context}]

    for angel, demon in zip(angel_messages, demon_messages):
        messages.append({"role": "user", "content": angel})
        messages.append({"role": "assistant", "content": demon})

    messages.append({"role": "user", "content": human_message})
    completion = openai.chat.completions.create(model=GPT_MODEL, messages=messages)

    return completion.choices[0].message.content


# Main loop to include human interaction
print("*" * 100)
print("\nWelcome to the Angel and Demon decision-making app!\n")
human_question = input("What is your dilemma or question human? \n>>> ")

angel_response = call_angel(human_question)
print("\n********")
print("Angel:")
print("\n********")
print(f"\n{angel_response}\n")
angel_messages.append(angel_response)

demon_response = call_demon(human_question)
print("\n********")
print("Demon:")
print("\n********")
print(f"\n{demon_response}\n")
demon_messages.append(demon_response)

for i in range(5):
    human_message = input(
        "What are your thoughts or actions based on their advice? \n>>> "
    )

    # Analyze the human's input to determine their inclination
    if "angel" in human_message.lower():
        print("\n********")
        print("Angel:")
        print("\n********")
        print(
            "\n"
            + call_angel(
                "The human seems to agree with you. "
                f"Human's message was {human_message}. Rejoice and guide further."
            )
        )

        demon_attempt = call_demon(
            "The human sided with the angel. "
            f"Human's message was {human_message}. Try convincing them to reconsider."
        )
        print("\n********")
        print("Demon:")
        print("\n********")
        print(f"\n{demon_attempt}\n")
        demon_messages.append(demon_attempt)

    elif "demon" in human_message.lower():
        print("\n********")
        print("Demon:")
        print("\n********")
        print(
            "\n"
            + call_demon(
                "The human seems to agree with you. "
                f"Human's message was {human_message}. Revel in your victory and guide further."
            )
        )

        angel_attempt = call_angel(
            "The human sided with the demon. "
            f"Human's message was {human_message}. Try convincing them to reconsider."
        )
        print("\n********")
        print("Angel:")
        print("\n********")
        print(f"\n{angel_attempt}\n")
        angel_messages.append(angel_attempt)

    else:
        print("Both parties remain unsure. Keep deliberating!")
