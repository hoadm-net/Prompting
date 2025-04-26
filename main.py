from langchain_core.messages import HumanMessage, SystemMessage
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()

    model = init_chat_model('gpt-4o-mini', model_provider='openai')

    messages = [
        SystemMessage('Trong vai trò chuyên gia tư vấn, hãy trả lời giúp tôi một số câu hỏi sau:'),
        HumanMessage("Xin chào!"),
    ]

    response = model.invoke(messages)
    print(response.content)
