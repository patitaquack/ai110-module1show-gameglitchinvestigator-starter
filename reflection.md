# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
At first it seemed like it was running well. But as I kept playing I started noticing that certain things weren't working well. I liked the concept of the game, and I right away noticed room for improvements.

- List at least two concrete bugs you noticed at the start  

The hints were definitely backwards. The secret number would be higher, when the hint would suggest to go lower. The secret number was not consistent throught a session.


One thing that didn't seem normal were the scores. The score would sometimes be a negative number. Games don't ususally use negative score numbers.

The number of tries for all game levels were the same. The easy mode had less tries, which is not natural in a game. There was no difference about the gameplay between the easy mode compared to the other two leves. 

  

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Claude as my partner! It gave great suggestions to the improvements I had in mind. I also used chat gpt to help me undertand Streamlit better, as it was my first time using it.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

I wanted to make the easier mode easier than the normal and hard level. I wanted the hints to be more specific to the user. Claude suggested using temeperature hints aside from the higher and lower hint keywords. I made the change, and when the user plays in easy mode, the temperature suggestion hints definitely make it easier to play the game.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
When I began to play I noticed the final scores weres sometimes negative, I mentioned to claude that negative scores are not natural in games. It suggested a random positive score number. That isn't really a good way to give scores. If the user guessed the score number the second try, the final score was 20. That seemed ungfair. So I gave claude a different prompt.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I refreshed the game, and tried different approaches to the game play. I tried every plausible scenerio for a user. Only then could I test if the bug was resolved.

- Describe at least one test you ran (manual or using pytest)  and what it showed you about your code.
For the temperature hinting, and also the final score fix, I manually tested by playing the game in different levels. I also, tried to enter the secret number in different number of tries. I saw the improvement in final scores for different number of tries. I also saw the changes in game levels, specially for the easy mode.
  
- Did AI help you design or understand any tests? How? Yes, claude helped implement function stubs from logic_utils.py, it also helped fix two bugs from that. The check_guess returns a tuple, but the tests compare against a plain string. Claude wrote test_game_logic.py.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
The secret number kept changing because in Streamlit the program reruns after every interaction or progress. So the secret number wouldn't save and stay the same. If it doesn't save, then it just refreshes every rerun.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit? " In steamlit the program reruns or restarts constantly while running. It will start from the very beginning of the program. The session state will save any progress or interactions with the user, once the program reruns, it has history saved. 
- What change did you make that finally gave the game a stable secret number? the "if" statemnt helped keep the same number, and not give a new one for every rerun. It checks the the secret number is already in the state, if its not then it gives a new secret number. If it does have a secret number already in state, then it won't suggest a new secret.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
This is the first time testing a code/ program. I had never used pytest before. I will definitely be using that from now on! It is a great way to test functions!

  - This could be a testing habit, a prompting strategy, or a way you used Git.
  Using pytest in vs code was fun and also very educational for me. It is a great testing habit that I'd like to use more often. Being able to see what passed, and make sure that everything works as it should.

- What is one thing you would do differently next time you work with AI on a coding task? I think using a more suggestive prompt. I learned in this project that giving ai more room for suggestions, can help me come up with something in bettween that might actually work better. My promtps before this were very specific, and not always correct. Now with more flexible prompts, AI suggestes a few different options that I can use or improve.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
This was the first time I have used an ai extension in an IDE, I have learned that AI is a great tool to improve a program by testing. Having a partner that can help you undestand your errors by suggesting great resolutions is definitely useful in producing an effective program.
