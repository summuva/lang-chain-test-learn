from langchain.llms import LlamaCpp, OpenAI 
import config 
api = config.OPENAI_API_KEY

# Creamos el modelo al cual le hacemos las consultas
llm_openai = OpenAI(model_name= "text-davinci-003",openai_api_key=api)

# Dicho modelo nos retorna la respuesta 
# respuesta = llm_openai("HOlis como estas?")
# print(respuesta)



# Interactuar con modelos de chat

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

chatgpt = ChatOpenAI(openai_api_key=api)

# respuesta = chatgpt([HumanMessage(content="Weeeeeeenas")])
# print(respuesta)






# Uso de templates


from langchain import PromptTemplate 
# Creacion del template basico
template_basico = '''Eres un asistente virtual culinario que responde a preguntas de manera muy breve.
Pregunta: Cuales son los ingredientes para preparar {platillo}?
Respuesta: '''


# formateamos nuestro prompt con la clase promptTemplate 
prompt_temp = PromptTemplate(input_variables=["platillo"],template=template_basico)

prompt_value = prompt_temp.format(platillo="pizza de albahaca")

# respuesta = llm_openai(prompt_value)

# print(respuesta)



# Template completo 

from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate,ChatPromptTemplate