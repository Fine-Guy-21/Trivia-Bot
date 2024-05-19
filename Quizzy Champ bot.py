from pyrogram import Client, filters , enums
from pyrogram.types import ReplyKeyboardMarkup , Message
from pyrogram.enums import PollType
from pyrogram.handlers import poll_handler
import credentials as cr
import time , requests , random , html


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

                bot.send_poll(
                                chat_id= message.chat.id,
                                question =f" [{i}/{len(questions)}]. " + poll_question + "\n\n",
                                options = choices,
                                type = PollType.QUIZ,
                                open_period = 45,
                                is_anonymous = False,
                                correct_option_id= choices.index(question["correct_answer"])
                )
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


bot.run()