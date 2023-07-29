import random
from functions.main_functions import generate_content, image_to_base64, generate_template
from functions.images_functions import get_background
OPEN_API_KEY = ""
def generate_presentation(topic,style,num_slides,image_source):

    sd_model= "Lykon/DreamShaper" #@param {type:"string"}
    #@markdown ###### Select an Openai Model:
    engine="gpt-3.5-turbo" #@param ["gpt-4-32k-0613","gpt-4-32k","gpt-4-0613","gpt-4","gpt-3.5-turbo-16k-0613","gpt-3.5-turbo-0613","gpt-3.5-turbo-16k","gpt-3.5-turbo","text-ada-001","text-babbage-001","text-curie-001","text-davinci-002","text-davinci-003"]{type:"string"}
    #@markdown ###### Enter your OpenAi api key here:
    api_key = OPEN_API_KEY
    text_models = ["text-ada-001", "text-babbage-001", "text-curie-001", "text-davinci-002", "text-davinci-003"]
    # chat_models = ["gpt-3.5-turbo-16k-0613", "gpt-3.5-turbo-0613", "gpt-3.5-turbo-16k", "gpt-3.5-turbo"]
    styles = {"style1": "style1.css", "style2": "style2.css", "style3": "style3.css"}
    type_of_slides = ["para-1", "para-2", "img", "points"]

    use_chat = False if engine in text_models else True

    style_file = styles.get(style, "")

    slides = ["slide-1:title"]
    num_slides = int(num_slides)
    nums = num_slides - (num_slides // 2)
    slides.extend([f"slide-{i+2}:{type_of_slides[0:2][int(random.randint(0, 1))]}" for i in range(nums)])
    slides.extend([f"slide-{i+nums+2}:{type_of_slides[2:4][int(random.randint(0, 1))]}" for i in range(num_slides - nums - 1)])
    bg_image = image_to_base64(get_background(style_file))

    content = None
    while content is None:
        content = generate_content(slides, topic, engine, api_key, use_chat)
        if content is not None:
            break

    html = generate_template(style_file, slides, content, bg_image, image_source).render()
    return html