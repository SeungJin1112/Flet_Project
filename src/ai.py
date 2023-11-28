import openai
import re

from context import * 

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
                            {"role": "user", "content": f"""{prompt}.
                            이 증상들이 어떤 병의 특징일 수 있으며, 
                            증상을 완화할 수 있는 상용 약물 성분들을 다음과 같은 JSON 형식으로 제공해 주세요: 
                            '{{"예상 병명": ["병명1", "병명2"], "성분": ["성분1", "성분2"]}}'
                             해당 형식을 꼭 지켜주세요."""}],
                    max_tokens=1024
                );
            
            response_text = response.choices[0].message.content;
            response_str = str(response_text);
            # print(response_str);

            pattern = r'\{[^\}]*\}';
            matches = re.findall(pattern, response_str);
            # print(matches);

            extracted_string = matches[0] if matches else None;
            print(extracted_string);
        
            if extracted_string:
                return extracted_string;
    
        return None;
