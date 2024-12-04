// genkit-demo.mjs

// ============================
// Setup Instructions:
// 1. Ensure Node.js (v18 or later) is installed on your machine.
//    You can download it from https://nodejs.org/.
//
// 2. Install dependencies in your project directory by running:
//    npm install @genkit-ai/googleai@0.9.0-rc.3 genkit
//
// 3. Set the Google API key as an environment variable. Replace <YOUR_API_KEY> with your actual key:
//    - Linux/Mac (Bash/Zsh):
//      export GOOGLE_API_KEY=<YOUR_API_KEY>
//    - Windows (Command Prompt):
//      set GOOGLE_API_KEY=<YOUR_API_KEY>
//    - Windows (PowerShell):
//      $env:GOOGLE_API_KEY="<YOUR_API_KEY>"
//
//    Note: Obtain your Google API key from your Google Cloud Console.
//
// 4. Run the script using Node.js:
//    node genkit-demo.mjs
//
// ============================

// Import the Genkit and Google AI plugin libraries
import { gemini15Flash, googleAI } from '@genkit-ai/googleai';
import { genkit } from 'genkit';

// Configure a Genkit instance
const ai = genkit({
  plugins: [googleAI()],
  model: gemini15Flash, // Set default model
});

(async () => {
  // Make a generation request
  const { text } = await ai.generate('Hello, Gemini!');
  console.log(text); // Output the generated text
})();
