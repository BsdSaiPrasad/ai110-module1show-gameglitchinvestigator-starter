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
# One test I ran with pytest was checking check_guess(60, 50). It showed that the function should return "Too High" with the hint "Go LOWER!". This helped confirm that the hint direction bug was fixed correctly.

- Did AI help you design or understand any tests? How?
# AI helped me understand that my tests were failing because check_guess() was returning a tuple like ("Too High", "📉 Go LOWER!") instead of just a single string. It also helped me rewrite the test cases so they matched the actual function output.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
# The secret number kept changing in the original app because the code was not handling state properly, and some values were getting reset during reruns. Also, the app had logic that sometimes changed how the secret was used, which made the behavior inconsistent.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
# I would explain Streamlit reruns like this: every time you click a button or type something, Streamlit runs the script again from top to bottom. Session state is like a small memory box that keeps important values, such as the secret number, between reruns.
- What change did you make that finally gave the game a stable secret number?
# The change that gave the game a stable secret number was making sure the code always used st.session_state.secret directly instead of sometimes converting it to a string or recreating it unnecessarily.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
   - This could be a testing habit, a prompting strategy, or a way you used Git.
# One habit I want to reuse is testing one bug at a time instead of trying to fix everything together. That made debugging much easier and helped me understand what each change was doing.
 
- What is one thing you would do differently next time you work with AI on a coding task?
# Next time I work with AI on a coding task, I would be more careful to check every suggested code change before applying it. I learned that AI can be very helpful, but it can also make mistakes or edit the wrong file if I do not verify things.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
# This project changed the way I think about AI-generated code because I realized that AI code may look correct at first, but it still needs careful testing and debugging. I now see AI more as a helper for problem solving, not something I should trust blindly.
