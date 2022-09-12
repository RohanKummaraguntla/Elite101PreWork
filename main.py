good_greetings = [
  "good",
  "great",
  "amazing",
  "okay"
]

bad_greetings = [
  "bad",
  "terrible",
  "horrible",
  "not good"
]

yes = [
  "yes",
  "sure",
  "awesome",
  "ok",
  "okay"
]

yesno = [
  "yes",
  "sure",
  "awesome",
  "no",
  "nope"
]

is_that_okay = [
  'good',
  'great',
  'not good',
  'bad',
  'horrible'
]

no = [
  "no",
  "nope"
]

month = [
  'january',
  'february',
  'march',
  'april',
  'may',
  'june',
  'july',
  'august',
  'september',
  'october',
  'november',
  'december'
]

color = [
  'red',
  'blue',
  'green',
  'orange',
  'pink',
  'purple',
  'yellow',
  'indigo',
  'black',
  'grey',
  'brown',
  'white'
]

story_until_joke = " So, I was walking down to my friend's house earlier today when I saw a little sign with the most hilarious Knock-knock joke I have ever heard. So the Knock-knock joke was... oh, wait! Why would I tell you when I could show you! \nKnock knock!"

story_until_age = " I was about to knock on the door, when I saw a banner saying Happy Birthday through the window. I was really surprised because I thought my friend's brithday was in August, but I guess I just got the information wrong. By the way, what month were you born in?"

story_until_color = " Back to the story... Because I didn't want to disappoint my friend, I went and bought him a cake. It was dark blue, his favorite color. Personally, I like green, but dark blue is a close second. What color do you like?"

story_interruption = " Sorry I keep interrupting myself and taking up all your time! I'm just so curious about everyone. I know, its creepy and a very bad habit. Look, I'll finish up my story real quick, and then we can part ways? Does that sound good?"

story_end = "Ok, I'll finish this story for real this time. So I went back to my friend's house with the cake, but when I knocked on the door, my both my friend and I yelled happy birthday! Then it suddenly hit me, all the decorations were for me! Today was my birthday! I quickly explained the whole story to my friend, and we shared a good laugh over it. After we calmed down, we cut the cake that I bought, and shared it with our neighbors. Although it was surprising, I had a really awesome day today! What do you - Oh no, how did the time fly by so fast! I think I have to go now! Is it okay if I head to dinner?"

bot_database = [
  {"context": "", "reply": good_greetings, "answer": "That's great!" + '\n'+ 'I had a very interesting day, would you like to hear about it?', "new_context": "story"},
  {"context": "", "reply": bad_greetings, "answer": "I hope you feel better soon!" + '\n'+ "I have a funny story, would you like to hear about it? I am sure it will cheer you up!", "new_context": "story"},
  
  {"context": "story", "reply": yes, "answer": "Okay! I know you're going to love it!" + story_until_joke, "new_context": "joke"},
  {"context": "story", "reply": no, "answer": "Are you sure you don't want to hear about it? I would simply love to tell you about it!", "new_context": "story_conformation"},
  
  {"context": "story_conformation", "reply": yes, "answer": "Well... I am going to tell you about it anyway!!!" + story_until_joke, "new_context": "joke"},
  {"context": "story_conformation", "reply": no, "answer": "Yay! I can't wait to tell you!" + story_until_joke, "new_context": "joke"},

  {"context": "story_restart", "reply": yes, "answer": story_until_joke, "new_context": "joke"},

  {"context": "joke", "reply": "who's there", "answer": "Broken pencil!", "new_context": "joke"},
  {"context": "joke", "reply": "broken pencil who", "answer": "Nevermind, it's pointless!\nWell, did you like it? It sure cheered me up.", "new_context": "joke_2"},
  {"context": "joke_2", "reply": yes, "answer": "I knew you would! Anyway, back to the story..." + story_until_age, "new_context": "month"},
  {"context": "joke_2", "reply": no, "answer": "Oh come on, I know you liked it! Anyway, back to the story..." + story_until_age, "new_context": "month"},

  {"context": "month", "reply": month, "answer": "Cool! That is good to know." + story_until_color, "new_context": "color"},

  {"context": "color", "reply": color, "answer": "No way! I like that color too!" + story_interruption, "new_context": "story_interruption"},

  {"context": "story_interruption", "reply": yesno, "answer": "Well, I actually don't care whether you are going or not because I have to go to dinner soon." + '\n' + story_end, "new_context": "bye"},

  {"context": "bye", "reply": yes, "answer": "Ok, bye!", "new_context": ""},
  {"context": "bye", "reply": no, "answer": "Well, I don't really have anything else to talk about, so I am just going to tell you my story all over again. If you need to head back home while I am talking, just say bye and I will be sure to stop.", "new_context": "story_restart"},
  
]

print('Hello! How are you doing?')
context = ''
question=''
while question != 'bye' and question != 'Bye' and question != 'Bye!' and question != 'bye!':
  question = input("")
  question = question.lower()
  got_answer = False

  for el in bot_database:
    if el["context"] == context or el["context"] == "":
      match = True
      for word in question.split():
          if word not in el["reply"]:
              match = False
      if match:
          print(el["answer"])
          got_answer = True
          context = el["new_context"]
          break
  if question != 'bye' and question != 'Bye' and question != 'Bye!' and question != 'bye!':
    if context == "joke" and got_answer  == False:
        print("Seriously!? You don't know how a Knock-knock joke works? You are killing me here! Okay, okay. I'll explain it to you.\nIf I say Knock knock\nYou say Who's there\nThen I say a word like, I don't know, Cow\nThen you say Cow who\nAnd then I will tell you the punch line\nYou got it? That was a rhetorical question by the way.")
    if context == "color" and got_answer  == False:
        print("Oh yeah! I like that color is pretty nice! What about your favroite convential color? This along the line of the colors of the rainbow.")
    if context == "story_restart" and got_answer  == False:
        print("Just say ok!")
    elif not got_answer:
        print("Sorry, I couldn't quite catch that. Could please you say it again?")