# Inner Debate: Angel vs. Demon

![Inner Debate Illustration](./images/ethics-vs-chaos.webp)

## Overview
The **Inner Debate App** is a humorous interactive application where an angel and a demon, each sitting on a human's shoulder, attempt to influence the human's decisions. With witty banter, playful persuasion, and endearing attempts, the app simulates the classic moral dilemma in a fun and engaging way.

## Features
- **Dynamic Conversations**: The angel and demon adapt to the human's decisions and provide tailored responses.
- **Multiple Rounds**: The opposing party tries to persuade the human at least twice before conceding.
- **Customizable Contexts**: Modify the personality and behavior of the angel and demon using system contexts.
- **Engaging Interaction**: Light-hearted and witty responses make the decision-making process enjoyable.

## How It Works
1. The user presents a dilemma or question.
2. The angel and demon provide their perspectives in response.
3. The user interacts by sharing their thoughts or siding with one of the parties.
4. The opposing party attempts to convince the user to reconsider.
5. The process continues for multiple rounds, ensuring a lively debate.

## Prerequisites
1. **Python 3.11+**
2. **OpenAI Python Library**
3. **dotenv Library**
4. An OpenAI API Key

## Installation
1. Clone this repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd inner-debate-app
   ```
3. Install the required dependencies:
   ```bash
   pip install openai python-dotenv
   ```
4. Add your OpenAI API key to a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage
1. Run the application:
   ```bash
   python inner_debate.py
   ```
2. Enter your dilemma or question when prompted.
3. Engage with the angel and demon responses and provide your input.
4. Witness the angel and demon's playful attempts to influence your decisions.

## Example Interaction
```plaintext
****************************************************************************************************

Welcome to the Angel and Demon decision-making app!

What is your dilemma or question human?
>>> Should I eat cake or stick to my diet?

********
Angel:
********
Ah, my dear! Think of your health and well-being. Let's make the wholesome choice today!

********
Demon:
********
Oh, come on! Life’s short—grab that cake and savor every bite!

Your thoughts or actions based on their advice: I think the demon makes a good point.

********
Demon:
********
I knew you had it in you! Now, go grab that cake and live a little!

********
Angel:
********
Oh, my dear, think of your goals! Don’t let a moment of indulgence derail your progress!
```

## Future Enhancements
- **Voice Integration**: Add voice-based input and output for a more immersive experience.
- **GUI Interface**: Develop a graphical interface to make the app visually engaging.
- **Multilingual Support**: Enable the app to work in multiple languages.

## Contributing
Pull requests are welcome! If you'd like to make significant changes, please open an issue first to discuss your ideas.

## License
This project is licensed under the MIT License.

