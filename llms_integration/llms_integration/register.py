from abc import ABC, abstractmethod
import ollama
import requests

class API(ABC):
    def __init__(self):
        self.token = None

    @property
    @abstractmethod
    def api_model(self):
        pass

    @property
    @abstractmethod
    def token(self):
        pass
    
    @property
    @abstractmethod
    def send(self):
        pass
    
class OllmaAPI(API):
    def __init__(self) -> None:
        super().__init__()
        self.__host = '0.0.0.0'
        self.__port = '11434'
        self.__messages = []

    @property
    def url(self):
        return f"{self.__host}:{self.__port}"
    
    @property
    def api_model(self):
        return "ollama"
    
    @property
    def token(self):
        return self.__token
    
    @token.setter
    def token(self, value):
        self.__token = value

    def chat(self):
        r = requests.post(
            f"http://{self.url}/api/chat",
            json={"model": self.api_model, "messages": self.messages, "stream": True},
        stream=True
        )
        r.raise_for_status()
        output = ""

        for line in r.iter_lines():
            body = json.loads(line)
            if "error" in body:
                raise Exception(body["error"])
            if body.get("done") is False:
                message = body.get("message", "")
                content = message.get("content", "")
                output += content
                # the response streams one token at a time, print that as we receive it
                print(content, end="", flush=True)

            if body.get("done", False):
                message["content"] = output
                return message
    
    @property
    def messages(self):
        return self.__messages

    def send(self, text_message):
        self.messages.append({"role": "user", "content": text_message})
        message = self.chat()
        self.messages.append(message)

class ApiFactory(ABC):
    @abstractmethod
    def create_api(self):
        """Factory Method: Create a API instance."""
        pass

class OllmaAPIFactory(ApiFactory):
    def create_api(self):
        return OllmaAPI()

def create_api(api='ollama'):
    apis = {
        'ollama': OllmaAPIFactory
    }

    return apis[api]().create_api()

if __name__ == '__main__':
    
    print(create_api().token)
    print(create_api().send("Porque o céu é azul?"))