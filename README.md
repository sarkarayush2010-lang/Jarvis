# JARVIS AI Assistant & Audio Visualizer Interface

HUD visualizer Site: https://jarvis-ten-beta.vercel.app/

---

## Description
We ALL love iron man right? Thats why we're here in hack club  
I was able to build this. IN A CAVE (my room). WITH A BOX OF SCRAPS (My non-scrappy laptop)  
So what's this project?

## two parts
# python script as .exe
You can run this file(found in releases), and it should automatically work. 
Start a sentence by saying "Jarvis" and use a command from the list on the bottom of ym readme. 
You can open Google and Spotify, your email, search up anything on google, OR ask it math problems. I also previously coded a dice roller game so now you can roll dice with jarvis!

# index.html (alternate site: https://jarvis-fpmozjzgn-coolbeardeddragon11-8956s-projects.vercel.app/)
yes i searched up how to make an audio visualizer and rewrote it to fit my jarvis
It doesn't need to work alongside the app, but they both work well together!
but it works! click on the inner core for jarvis, and connect to a tab or system's audio. The circle expands and contracts based on audio coming from your laptop. While I intended to use this for my jarvis project, it honestly works better as a visualizer for spotify so if you want to use it like that, then go ahead!  
It displays the current time, date, and has jarvis in the midle..  

If you don't connect to an audio source, it falls back on your microphone input, and allows you to visualize that instead!
ooh a good idea would be to connect this with a projector and project on a black wall, that would look super tuff

---

## System Requirements
* **OS:** Windows 64 bit (I think thats 10 and 11 only)
* **Storage** the app only takes like 380 mb, which actually seems like a lot, but since it doesnt need python i guess that makes sense
*  **RAM** this started lagging on my brothers laptop with 8gb so 16gb is reccomended, but I dont think the limit is very high. If it starts getting super laggy, just use either one of the two parts, you dont need them together
* **Hardware:** Microphone for input *Default index is 2.*

## First-Run Setup Instructions
Because this executable is a custom standalone build, Windows SmartScreen may flag it on your first open.
1. Download From releases
2. Extract `Jarvis-Windows-v1.0.zip`.
3. Right-click `testjarvis.exe` and select **Properties**.
4. Check the **Unblock** checkbox at the bottom right if it appears, then click **Apply**.
5. Double-click the file to launch. If a blue Windows SmartScreen popup appears, click **"More Info"** and then select **"Run Anyway"**.

## How to use
Run the code
Say "jarvis ", and then one of the commands below. for example i could say "Jarvis, Search for six seven", and if it heard you properly, it would use the default web browser (or whatever you have open if you do have anything open at all) and it would search for "six seven"  
To exit, you have to say "Jarvis shut down". Jarvis should say goodbye and the program will stop. Alternatively, you can shut it down through task manager (which is more reliable)


## Screenshots
<img width="2559" height="1353" alt="image" src="https://github.com/user-attachments/assets/847f6aa7-771a-40d1-b9dc-588f3909f298" />
Visualizer Site

<img width="901" height="872" alt="image" src="https://github.com/user-attachments/assets/e382aa23-a36a-4675-bfcd-2df555eb3681" />
pop up looks like this - make sure to select "Also share System Audio"

No screenshots for the app because it literally just runs by itself in the background!

## Motivation
It's every engineers goal to become Iron Man, so why would it be different for me?  
Also now it makes it easier to open up youtube or spotify and doomscroll or listen to music! it also is a really nice audio visualizer for my spotify so i can keep it running on a second screen and that looks tuff!
For further implementations of this, I want to connect this to the camera so i can actually use my hands like Tony Stank does and like navigate my screen without touching the keyboard.



## Full list of commands - you have to say "jarvis" before asking any one of these commands, kind of like siri before ios 27 or alexa before the alexa plus update

"thank you" / "jarvis thank you" — Jarvis politely replies, "You're welcome Sir".

"shut down" — SHUTS DOWN - VERY VERY IMPORTANT OTHERWISE YOU HAVE TO SHUT DOWN THROUGH TASK MANAGER

"open spotify" — If you have spotify app installed(not from browser, desktop version), it should boot up

"open google" — opens google from the default path. If yours is any different, it won't work

"open email" — uses webbrowser to go to gmail.com

"open youtube" — I love to doomscroll, so why not make it easier for me to waste time and lose more sleep? (opens youtube, duh)

"search for ____ " — searches google for whatever you said after the "for"

" ___.com" / "_____  dot com" — Extracts the domain name, injects a secure https:// prefix, and navigates straight to that URL.

"volume increase" / "volume up" — Raises audio level. I dont know why but it loves numbers that end with a 4 for some reason

"volume decrease" / "volume down" — Lowers audio level. same thing abt the 4s idk why it loves it

"volume set to _____ " — DO NOT SAY PERCENT, just say the number (ex: set volume to 8 --- ps why are my beats so loud like i have to keep the volume at around 10, anything higher than 40 hurts my ears)

"reminder to [task]" / "reminder for [task]" — I was too lazy to actually make it tell you when the actual time is, so it just says it back to you!

"current time" / "clock" — gives you the current time (duh)

"date" / "today" — gives you today's date

"plus" / "add" — Adds two spoken numbers together.

"minus" / "subtract" — subtracts two numbers (second from first)

"times" / "multiply" — Multiplies two  numbers

"divide" / "divided by" — divides first number into second numbers' partses

"power" / "exponent" — calculates first number to the power of second number

"square root" — finds square root of ONE SINGLE number DO NOT try two numbers it made everything super laggy

"dice" — yes, i already made a dice game. But this ones easier. There are also more parts:  
For example if you  
Saying nothing else: Rolls a single 6-sided die.  
Providing one number: Rolls a custom die with that many sides.   
Providing two numbers: Corrects the order seamlessly to roll X amount of dice with Y number of sides!  



## AI use + More
uh oh i actually had to use generative AI(for troubleshooting and it was barely anything anyways), but only for the first mic input stuff(less than 10 lines, so it works for hack club). For some reason, it wasn't picking up my audio the way I originally did it, even though i copied from reddit
for the same version of python but i dont know what happened there.  
Once the microphone stuff was done, I knew how to do everything myself, so I'm proud of actually coding the app to open sites and do operations. A lot of it relied on string splicing, which luckily my ap csp teacher drilled us hard at school.  
Other than those 10-20 lines that I rewrote with AI because MY FRICKING CODE WHICH WAS RIGHT DIDNT WORK, the only other ai I used was google search ai summaries, which tbh shouldnt count, and that again was barely for anything!
All HTML stuff was my own as well
