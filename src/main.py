from nicegui import ui
import os, openai

openai.api_key = os.getenv("OPENAI_API_KEY")
conversation = []

class ChatGPT:  
    

    def __init__(self):
        
        self.messages = conversation
        self.model = os.getenv("OPENAI_MODEL", default = "gpt-3.5-turbo")



    def get_response(self, user_input):
        conversation.append({"role": "user", "content": user_input})
        

        response = openai.ChatCompletion.create(
	            model=self.model,
                messages = self.messages

                )

        conversation.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
        
        print("AI回答內容：")        
        print(response['choices'][0]['message']['content'].strip())


        
        return response['choices'][0]['message']['content'].strip()

chatgpt = ChatGPT()


class Prompt:

    prompt_string: str
    answer_string: str


    def __init__(self):
	prompt_string = ""
	answer_string = ""

    def on_changed(self, symbol: str):
        if symbol is None or symbol == "":
            pass
        if symbol.lower() == "generate":
	    ai_reply_response = chatgpt.get_response(prompt_string)
            self.answer_string = ai_reply_response
		
		



prompt = Prompt()


from nicegui.events import ValueChangeEventArguments


#def getGPTrespond(event: ValueChangeEventArguments):
    #ai_reply_response = chatgpt.get_response(event.value)
    #name = type(event.sender).__name__
    #ui.label(f'ChatGPT AI: {ai_reply_response}')

ui.input("Type in string here.").bind_value(prompt, "prompt_string")


#ui.label('Please type in your question here first. And then cut and paste it below./ 先打好你的問題在這，然後貼到下面的空格。')    
#ui.input('Type in your Question!')    
#ui.label('Paste here, and get ChatGPT response./ 問題或提示貼在這裡，然後得到ChatGPT AI的回答。')    
#ui.input('Paste here', on_change=getGPTrespond)

ui.button("Generate", on_click=lambda: prompt.on_changed("generate"))

ui.label(f'ChatGPT AI: {prompt.answer_string}').bind_value(prompt, "answer_string")
ui.run()
