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

    def fn_start(self): 
        self._ai_prompt=AiPrompt();
    
        self._ai_list = [self._ai_prompt];
    
        for iter in self._ai_list:
                iter.fn_start();
           
    def fn_end(self): pass;
    def fn_enable(self): pass;
    def fn_disable(self): pass;
    
class AiPrompt():
    def __init__(self): pass;
    def fn_start(self): 
        # 통신 테스트
        if g_ai_api_key != "":
            if g_ai_instance != None and g_ai_instance._ai != None: 
                response = g_ai_instance._ai.ChatCompletion.create(
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
            if g_ai_instance != None and g_ai_instance._ai != None: 
                response = g_ai_instance._ai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "system", "content": "You are a doctor."},
                            {"role": "user", "content": "hi"}],
                    max_tokens=1024
                );

            print(response);