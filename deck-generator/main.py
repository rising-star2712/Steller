#!/usr/bin/env python
# coding: utf-8

# ### Import requirements

# In[ ]:


from functions.main_functions import *


# In[ ]:


#@markdown ###### Enter a topic:
topic="Organic Farming" #@param {type:"string"}
#@markdown ###### Select a style:
Style = "Style 2" #@param ["Style 1","Style 2","Style 3"] {type:"string"}
#@markdown ###### Select a number of slides
Number_of_Slides=5 #@param {type:"slider", min:2, max:7, step:1}
#@markdown ###### Select the image source
image_source="Pexel"#@param ["Pexel","Unsplash","Stable Diffusion"] {type:"string"}
#@markdown ###### Select a Stable diffusion model if image source is "Stable diffusion"
sd_model= "Lykon/DreamShaper" #@param {type:"string"}
#@markdown ###### Select an Openai Model:
engine="gpt-3.5-turbo" #@param ["gpt-4-32k-0613","gpt-4-32k","gpt-4-0613","gpt-4","gpt-3.5-turbo-16k-0613","gpt-3.5-turbo-0613","gpt-3.5-turbo-16k","gpt-3.5-turbo","text-ada-001","text-babbage-001","text-curie-001","text-davinci-002","text-davinci-003"]{type:"string"}
#@markdown ###### Enter your OpenAi api key here:
api_key = "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"

text_models=["text-ada-001","text-babbage-001","text-curie-001","text-davinci-002","text-davinci-003"]
chat_models=["gpt-3.5-turbo-16k-0613","gpt-3.5-turbo-0613","gpt-3.5-turbo-16k","gpt-3.5-turbo"]
styles={"Style 1":"style1.css","Style 2":"style2.css","Style 3":"style3.css"}
type_of_slides=["para-1", "para-2","img", "points"]

use_chat = False if engine in text_models else True

style=styles[Style]
slides = ["slide-1:title"]

nums=Number_of_Slides-(Number_of_Slides//2)
slides.extend([f"slide-{i+2}:{type_of_slides[0:2][int(random.randint(0,1))]}" for i in range(nums)])
slides.extend([f"slide-{i+nums+2}:{type_of_slides[2:4][int(random.randint(0,1))]}" for i in range(Number_of_Slides-(nums)-1)])


# In[ ]:


bg_image=image_to_base64(get_background(style))

content = None
while content == None :
    content = generate_content(slides,topic,engine,api_key,use_chat)
    if content != None: 
        break
    else:
        continue

  


# ### Make sure that the `content` is not `None`.
# #### At times openai api returns an error due to various reasons,`re-run` the above cell till `content` is not `None`.

# In[ ]:


#print(content)


# In[ ]:


html=generate_template(style, slides,content,bg_image,image_source).render()


# ##### This cell may return an error but it can be ignore, the pdf can be seen in the left panel

# In[ ]:

print(html)
#render_pdfkit(html,topic.replace(" ","-")+".pdf")


# In[ ]:




