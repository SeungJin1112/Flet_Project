from context import * 

import openai

g_ai_instance = None;

g_ai_api_key = "";

class AiChatGPT():
    _ai = None;

    _ai_prompt = None;

    def __init__(self): 
        global g_ai_instance;

        if g_ai_instance == None:
            g_ai_instance = self;
        
        if self._ai == None:
            self._ai = openai;
            self._ai.api_key = g_ai_api_key;

    def fn_start(self): pass;
    def fn_end(self): pass;
    def fn_enable(self): pass;
    def fn_disable(self): pass;

    def fn_get_instance(self):
        if g_ai_instance != None:
            return g_ai_instance;
    
class AiPrompt():
    _instance = None;

    def __init__(self, ai): 
        self._instance = ai.fn_get_instance();
    
    def fn_start(self): 
        # 통신 테스트
        if g_ai_api_key != "":
            if self._instance != None and self._instance._ai != None: 
                response = self._instance._ai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "system", "content": "You are a doctor."},
                            {"role": "user", "content": "hi"}],
                    max_tokens=1024
                );

            print(response);

    def fn_end(self): pass;
    def fn_enable(self): pass;
    def fn_disable(self): pass;

    def fn_prompt(self, prompt): 
        if g_ai_api_key != "":
            if self._instance != None and self._instance._ai != None: 
                response = self._instance._ai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "system", "content": "You are a doctor."},
                            {"role": "user", "content": "hi"}],
                    max_tokens=1024
                );

            print(response);