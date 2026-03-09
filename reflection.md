# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.


## 1. What was broken when you started?

- What did the game look like the first time you ran it?
## it looked look it was working fine until i tried some test cases, then it starting giving wrong hints
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
- 
## the hints were definitely backwards, 
## even if game won the current game still continues,
## even if i click new game we need to reload to start a new game, else the submit guess doesnt work. 
## once already won if i start new game it will change the secret and renews attempts but doesnt let us submit until we refresh the page
## in hard even if the game is won, it lets us enter our guess and we dont win
## in normal lets say the number is correct secret the game show anything, once its clicked the second time it will submit
## in normal, we need two submits to actually submit the guess
## attempts were inconsistent with game modes. like first it was 8 and then 7 for normal.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 
# i used claude, chatgpt.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
# when i told AI that the hints were in reverse. it actually gave me a correct code. that fixed the problem. and it was even precise with the emojis 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
# it helped me and told me to do the changes in try block but it forgot to tell me the changes to do in except block. then i reviewed it and wrote it correctly. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
# i tried testing it myself. and made sure whatever error was there it is resolved.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
