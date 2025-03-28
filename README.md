# AI Output Optimization Project

Welcome to the AI Output Optimization Project! This project focuses on improving how we interact with AI models to generate structured, actionable data. By leveraging powerful AI models like OpenAI, Anthropic, and Google Gemini, we can enhance responses, making them more useful and tailored to specific needs. Whether it's recommending movies or automatically filling out data models, this project aims to optimize the outputs from AI and make them more practical.

## Features

Here’s what this project can do:

### Movie Recommendations
Ever loved a movie and wondered, "What else is like this?" This project can help! By analyzing a movie you enjoy (like *Shutter Island*), the AI will recommend similar movies along with their genre and release year. It’s an easy way to discover movies that match your taste!

### Data Model Filling
If you need to automatically populate a person’s details (such as their age, birthdate, or gender), this project can do that too! Just provide basic information (e.g., “Mike was born on April 4th, 1990”), and the AI will fill out the rest of the data model for you.

### Optimizing AI Responses
The real magic happens when we optimize AI responses. Instead of receiving raw text that needs cleanup, the responses are structured and organized. The **instructor** module is the secret sauce, helping us interact with various AI models and formatting their outputs in exactly the way we need.

## How to Use It

### 1. Install Dependencies
To get started, you need to install the required Python packages. 

### 2. Set Up Your API Keys
For the AI models to work, you’ll need API keys. Create a `.env` file in your project folder, and add the following:
OPENAI_API_KEY=your_openai_api_key_here 
ANTHROPIC_API_KEY=your_anthropic_api_key_here 
GEMINI_API_KEY=your_gemini_api_key_here


Make sure to replace the placeholders with your actual API keys from OpenAI, Anthropic, and Google Gemini.

### 3. Run the Code
Once everything is set up, simply run the `example.py` script to see it in action. The script will interact with the AI models and give you back optimized, structured results.

## How It Works

Here’s a quick breakdown of what’s happening in the code:

### Movie Recommendations
The AI takes a movie you like and suggests similar ones. Using the **MovieGenreEnum**, it categorizes the genres and uses a **Movie** model to store details such as the title and release year. The recommended movies are then displayed in a clean, readable format.

### Filling Out Data Models
We send basic information (e.g., “Mike was born on April 4th, 1990”) to the AI, and it fills in the rest. The **DataModel** class defines the structure of the data (name, age, birthday, etc.), and the AI completes the rest of the information.

### Optimized Responses
Instead of receiving disorganized, raw text, we use the **instructor** module to ensure the AI’s responses are structured, making them easier to use right away. We send messages to OpenAI, Anthropic, or Gemini, telling them exactly how to format the responses, ensuring the output is ready for use.

## Why It’s Useful

When interacting with AI, responses often come as a messy block of text that requires cleaning up. This project solves that problem by ensuring you get data in a structured, usable format straight from the start—saving you time and effort.

## Contributing

If you think of ways to improve the project, feel free to fork it, open an issue, or send a pull request. Your contributions are welcome, and I’d love to see your ideas!

## License

This project is licensed under the MIT License, which means you can use it for anything you like—just be sure to check the LICENSE file for full details.






