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


from nicegui.events import ValueChangeEventArguments, ClickEventArguments

def show(event: ValueChangeEventArguments):
    ai_reply_response = chatgpt.get_response(event.value)
    name = type(event.sender).__name__
    #ui.notify(f'{name}: {event.value}')
    ui.label(f'{name}: {ai_reply_response}')
    
  
    
    
ui.input('Text input', on_change=show)    

ui.run()
