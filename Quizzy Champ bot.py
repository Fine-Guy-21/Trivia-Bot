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



@bot.on_raw_update()
async def handle_poll_update(bot, poll,user, ls):
    print(bot)
    print(user)
    print(poll)
    print(ls)





""" @bot.on_raw_update()
async def handle_poll_update(bot, poll, user, _):
    # Get the poll results
    poll_results = poll.get("results", {}).get("results", [])
    poll_results = poll.results.results

    # Find the correct answer
    for result in poll_results:
        if result.chosen ==  False:
            # Check if the user's answer was correct
            if result.correct == False:
                print("User guessed correctly!")
            else:
                print("User guessed incorrectly.")
            break
    else:
        print("Could not determine if the user guessed correctly.")
 """

bot.run()



{
    758704198: pyrogram.raw.types.User(
            id=758704198, 
            is_self=False, 
            contact=False, 
            mutual_contact=False, 
            deleted=False, 
            bot=False, 
            bot_chat_history=False, 
            bot_nochats=False, 
            verified=False, 
            restricted=False, 
            min=False, 
            bot_inline_geo=False, 
            support=False, 
            scam=False, 
            apply_min_photo=True, 
            fake=False, 
            bot_attach_menu=False, 
            premium=False, 
            attach_menu_enabled=False,
            bot_can_edit=False, 
            access_hash=-8292500750927469972, 
            first_name='Prince Fine', 
            last_name='Guy 🌚✨ | 🫣', 
            username='Fine_guy_21', 
            photo=pyrogram.raw.types.UserProfilePhoto(photo_id=3258609718204147772, dc_id=4, has_video=False, personal=False), 
            status=pyrogram.raw.types.UserStatusRecently(), 
            restriction_reason=[], 
            lang_code='en', 
            usernames=[])}


{
    "_": "types.UpdateMessagePoll",
    "poll_id": 5969975541820817762,
    "results": {
        "_": "types.PollResults",
        "min": False,
        "results": [
            {
                "_": "types.PollAnswerVoters",
                "option": "b'\\x00'",
                "voters": 0,
                "chosen": False,
                "correct": False
            },
            {
                "_": "types.PollAnswerVoters",
                "option": "b'\\x01'",
                "voters": 0,
                "chosen": False,
                "correct": True
            },
            {
                "_": "types.PollAnswerVoters",
                "option": "b'\\x02'",
                "voters": 1,
                "chosen": False,
                "correct": False
            },
            {
                "_": "types.PollAnswerVoters",
                "option": "b'\\x03'",
                "voters": 0,
                "chosen": False,
                "correct": False
            }
        ],
        "total_voters": 1,
        "recent_voters": [],
        "solution_entities": []
    },


    

    "poll": {
        "_": "types.Poll",
        "id": 5969975541820817762,
        "question": " [1/10]. How long did it take the motorized window washers of the original World Trade Center to clean the entire exterior of the building?\n\n",
        "answers": [
            {
                "_": "types.PollAnswer",
                "text": "2 Months",
                "option": "b'\\x00'"
            },
            {
                "_": "types.PollAnswer",
                "text": "1 Month",
                "option": "b'\\x01'"
            },
            {
                "_": "types.PollAnswer",
                "text": "3 Weeks",
                "option": "b'\\x02'"
            },
            {
                "_": "types.PollAnswer",
                "text": "1 Week",
                "option": "b'\\x03'"
            }
        ],
        "closed": False,
        "public_voters": False,
        "multiple_choice": False,
        "quiz": True,
        "close_period": 45,
        "close_date": 1717224188
    }
}




""" 
{
    "_": "types.UpdateMessagePoll",
    "poll_id": 5969975541820817763,
    "results": {
        "_": "types.PollResults",
        "min": false,
        "results": [
            {
                "_": "types.PollAnswerVoters",
                "option": "b'\\x00'",
                "voters": 1,
                "chosen": false,
                "correct": false
            },
            {
                "_": "types.PollAnswerVoters",
                "option": "b'\\x01'",
                "voters": 0,
                "chosen": false,
                "correct": true
            },
            {
                "_": "types.PollAnswerVoters",
                "option": "b'\\x02'",
                "voters": 0,
                "chosen": false,
                "correct": false
            },
            {
                "_": "types.PollAnswerVoters",
                "option": "b'\\x03'",
                "voters": 0,
                "chosen": false,
                "correct": false
            }
        ],
        "total_voters": 1,
        "recent_voters": [],
        "solution_entities": []
    },
    "poll": {
        "_": "types.Poll",
        "id": 5969975541820817763,
        "question": " [1/10]. Directly between the Washington Monument and the Reflecting Pool is a memorial to which war?\n\n",
        "answers": [
            {
                "_": "types.PollAnswer",
                "text": "American Civil War",
                "option": "b'\\x00'"
            },
            {
                "_": "types.PollAnswer",
                "text": "World War II",
                "option": "b'\\x01'"
            },
            {
                "_": "types.PollAnswer",
                "text": "American Revolutionary War",
                "option": "b'\\x02'"
            },
            {
                "_": "types.PollAnswer",
                "text": "Vietnam War",
                "option": "b'\\x03'"
            }
        ],
        "closed": false,
        "public_voters": false,
        "multiple_choice": false,
        "quiz": true,
        "close_period": 45,
        "close_date": 1717224447
    }
}

 """


