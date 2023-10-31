# py_chatbot

**Relatório sobre o projeto:**

Detalhes da Implementação:

O chatbot implementado faz uso da API do OpenAI, especificamente o modelo "gpt-3.5-turbo". A implementação é baseada na biblioteca Streamlit e inclui a utilização de outras bibliotecas Python, como PyPDF2 para a extração de texto de um arquivo PDF. Os detalhes da implementação são os seguintes:

    Importação de bibliotecas:
        os: Para a configuração da chave da API do OpenAI
        streamlit: Para a criação da interface do chatbot
        PyPDF2: Para a extração de texto de um arquivo PDF
        Bibliotecas específicas do projeto langchain para lidar com processamento de texto e recuperação de informações

    Função get_text():
        Responsável por extrair o texto de um arquivo PDF chamado "Base.pdf"

    Função get_chunks(text):
        Divide o texto extraído em pedaços menores para processamento subsequente

    Função get_vectorstore(chunks):
        Cria um vectorstore para armazenar os pedaços de texto e utiliza as embeddings do OpenAI para representá-los

    Função get_conversation(vectorstore):
        Configura um sistema de conversação que utiliza o modelo de linguagem da OpenAI e um mecanismo de recuperação baseado no vectorstore criado

    Função get_answer(user_question):
        Envia uma pergunta do usuário para o chatbot e obtém a resposta. Armazena o histórico da conversa para lembrar as interações anteriores

Resultados da Avaliação:

O chatbot implementado é simples e eficaz na resposta a perguntas específicas. Ele é capaz de responder a perguntas com base nas informações contidas no texto do arquivo PDF. No entanto, o chatbot apresenta algumas limitações em relação à compreensão de contexto. Ele não é capaz de manter conversas longas ou entender o contexto mais amplo das interações. A eficácia do chatbot depende da qualidade e relevância das informações presentes no PDF e das perguntas feitas pelos usuários.

Para testar o chatbot:

    Obtenha uma chave de API do OpenAI e substitua <YOUR-API-KEY-HERE> no código pelo seu token de API

    Execute o comando "streamlit run chatbot.py" no terminal para iniciar o chatbot

    Na interface do chatbot, digite sua pergunta na caixa de entrada e pressione Enter

    O chatbot responderá com uma mensagem que contém a resposta à sua pergunta
