from pyrogram import Client, filters , enums
from pyrogram.types import ReplyKeyboardMarkup , Message ,CallbackQuery
from pyrogram.enums import PollType
from pyrogram.handlers import poll_handler
import credentials as cr
import time , requests , random , html , pyrogram


bot = Client( cr.session,
              api_id=cr.api_id, 
              api_hash=cr.api_hash,
              bot_token=cr.bot_token)

Fine = 758704198
Entertainment = -1001881740609


def trivia():
    url = "https://opentdb.com/api.php?amount=10&category=9"#&difficulty=hard&type=multiple"
    response = requests.get(url)     
    trivia_data = response.json()
    return trivia_data ["results"]

def formatted(text):
    text = html.unescape(text)
    text = text.replace("&quot;", '"')
    text = text.replace("&amp;", "&")
    text = text.replace("&quot;", '"')
    text = text.replace("&lt;", "<")
    text = text.replace("&gt;", ">")
    text = text.replace("&#039;", "'")

    return text

class Status:
   def __init__(self) -> None:
      pass
   def State(self,st):
      self.states = (st =='True')

st = Status()
st.State("True")



@bot.on_message( filters.command("quizstart"))
def createpoll(bot,message:Message):
    if st.states == True:
        st.State("False")
        questions = trivia()
        i = 1
        for question in questions:
            try:
                poll_question = formatted(question["question"])
                correct = formatted(question["correct_answer"])
                choices = [formatted(choice) for choice in question["incorrect_answers"]]
                choices.append(correct) 

                random.shuffle(choices)

                bot.send_message(Fine,f" question : {poll_question} \n\n correct : {question['correct_answer']}")
                correct = question["correct_answer"]
                poll_message = bot.send_poll(
                                    chat_id= message.chat.id,
                                    question =f" [{i}/{len(questions)}]. " + poll_question + "\n\n",
                                    options = choices,
                                    type = PollType.QUIZ,
                                    open_period = 45,
                                    is_anonymous = False,
                                    correct_option_id= choices.index(correct) )
                
                i+=1
                time.sleep(50)
            except Exception as e:
                print(e)
                bot.send_message(Fine,e)                 
                message.reply(f"I'm sorry , i'm unable to present question {i} due to error ")
                i+=1
                time.sleep(5) 
            if i == 10:
                st.State("True")
    else:
        message.reply(f"There is an ongoing quiz @{message.chat.username}")



""" @bot.on_raw_update()
async def handle_poll(client, update, users, chats):
    print(update) """

# @bot.on_poll()
# async def handle_poll(client, update, users, chats):
#     print(update)


@bot.on_poll()
async def handle_poll_update(client, update):
    
    print(update)








print("Working 1. 2. 3.")
bot.run()

"""
Poll update received: {
    "_": "Poll",
    "id": "5994670207908446779",
    "question": " [1/10]. In aerodynamics, which force pushes an object upwards?\n\n",
    "options": [
        {
            "_": "PollOption",
            "text": "Lift",
            "voter_count": 1,
            "data": "b'\\x00'"
        },
        {
            "_": "PollOption",
            "text": "Drag",
            "voter_count": 0,
            "data": "b'\\x01'"
        },
        {
            "_": "PollOption",
            "text": "Weight",
            "voter_count": 0,
            "data": "b'\\x02'"
        },
        {
            "_": "PollOption",
            "text": "Thrust",
            "voter_count": 0,
            "data": "b'\\x03'"
        }
    ],
    "total_voter_count": 1,
    "is_closed": false,
    "is_anonymous": true,
    "type": "PollType.QUIZ",
    "allows_multiple_answers": false,
    "correct_option_id": 0,
    "open_period": 45,
    "close_date": "2024-06-09 16:32:29"
}
Poll update received: {
    "_": "Poll",
    "id": "5994670207908446779",
    "question": " [1/10]. In aerodynamics, which force pushes an object upwards?\n\n",
    "options": [
        {
            "_": "PollOption",
            "text": "Lift",
            "voter_count": 1,
            "data": "b'\\x00'"
        },
        {
            "_": "PollOption",
            "text": "Drag",
            "voter_count": 0,
            "data": "b'\\x01'"
        },
        {
            "_": "PollOption",
            "text": "Weight",
            "voter_count": 0,
            "data": "b'\\x02'"
        },
        {
            "_": "PollOption",
            "text": "Thrust",
            "voter_count": 0,
            "data": "b'\\x03'"
        }
    ],
    "total_voter_count": 1,
    "is_closed": false,
    "is_anonymous": true,
    "type": "PollType.QUIZ",
    "allows_multiple_answers": false,
    "open_period": 45,
    "close_date": "2024-06-09 16:32:29"
}
Poll update received: {
    "_": "Poll",
    "id": "5994670207908446779",
    "question": " [1/10]. In aerodynamics, which force pushes an object upwards?\n\n",
    "options": [
        {
            "_": "PollOption",
            "text": "Lift",
            "voter_count": 1,
            "data": "b'\\x00'"
        },
        {
            "_": "PollOption",
            "text": "Drag",
            "voter_count": 1,
            "data": "b'\\x01'"
        },
        {
            "_": "PollOption",
            "text": "Weight",
            "voter_count": 0,
            "data": "b'\\x02'"
        },
        {
            "_": "PollOption",
            "text": "Thrust",
            "voter_count": 0,
            "data": "b'\\x03'"
        }
    ],
    "total_voter_count": 2,
    "is_closed": false,
    "is_anonymous": true,
    "type": "PollType.QUIZ",
    "allows_multiple_answers": false,
    "correct_option_id": 0,
    "open_period": 45,
    "close_date": "2024-06-09 16:32:29"
}
Poll update received: {
    "_": "Poll",
    "id": "5994670207908446779",
    "question": " [1/10]. In aerodynamics, which force pushes an object upwards?\n\n",
    "options": [
        {
            "_": "PollOption",
            "text": "Lift",
            "voter_count": 1,
            "data": "b'\\x00'"
        },
        {
            "_": "PollOption",
            "text": "Drag",
            "voter_count": 1,
            "data": "b'\\x01'"
        },
        {
            "_": "PollOption",
            "text": "Weight",
            "voter_count": 0,
            "data": "b'\\x02'"
        },
        {
            "_": "PollOption",
            "text": "Thrust",
            "voter_count": 0,
            "data": "b'\\x03'"
        }
    ],
    "total_voter_count": 2,
    "is_closed": false,
    "is_anonymous": true,
    "type": "PollType.QUIZ",
    "allows_multiple_answers": false,
    "open_period": 45,
    "close_date": "2024-06-09 16:32:29"
}


"""



""" 

Poll update received: {
    "_": "Poll",
    "id": "5994670207908446781",
    "question": " [1/10]. Which of the following blood component forms a plug at the site of injuries?\n\n",
    "options": [
        {
            "_": "PollOption",
            "text": "White blood cells",
            "voter_count": 0,
            "data": "b'\\x00'"
        },
        {
            "_": "PollOption",
            "text": "Blood plasma",
            "voter_count": 1,
            "data": "b'\\x01'"
        },
        {
            "_": "PollOption",
            "text": "Platelets",
            "voter_count": 0,
            "data": "b'\\x02'"
        },
        {
            "_": "PollOption",
            "text": "Red blood cells",
            "voter_count": 0,
            "data": "b'\\x03'"
        }
    ],
    "total_voter_count": 1,
    "is_closed": false,
    "is_anonymous": false,
    "type": "PollType.QUIZ",
    "allows_multiple_answers": false,
    "open_period": 45,
    "close_date": "2024-06-09 16:36:03"
}
Poll update received: {
    "_": "Poll",
    "id": "5994670207908446781",
    "question": " [1/10]. Which of the following blood component forms a plug at the site of injuries?\n\n",
    "options": [
        {
            "_": "PollOption",
            "text": "White blood cells",
            "voter_count": 0,
            "data": "b'\\x00'"
        },
        {
            "_": "PollOption",
            "text": "Blood plasma",
            "voter_count": 2,
            "data": "b'\\x01'"
        },
        {
            "_": "PollOption",
            "text": "Platelets",
            "voter_count": 0,
            "data": "b'\\x02'"
        },
        {
            "_": "PollOption",
            "text": "Red blood cells",
            "voter_count": 0,
            "data": "b'\\x03'"
        }
    ],
    "total_voter_count": 2,
    "is_closed": false,
    "is_anonymous": false,
    "type": "PollType.QUIZ",
    "allows_multiple_answers": false,
    "open_period": 45,
    "close_date": "2024-06-09 16:36:03"
}

"""

