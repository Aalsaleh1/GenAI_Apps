pip install gpt4all
from gpt4all import GPT4All
model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf") # downloads / loads a 4.66GB LLM
with model.chat_session():
    print(model.generate("Write a joke about AI", max_tokens=1024))
  with model.chat_session():
    print(model.generate("write a joke?", max_tokens=64))

with model.chat_session():
    print(model.generate("Write a poem on AI", max_tokens=132))
