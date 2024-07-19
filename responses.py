from random import choice, randint



def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Bom, você está terrivelmente silencioso (/_ \)'
    elif 'oi' in lowered:
        return 'Chama! o((>ω< ))o'
    elif 'tudo bem?' in lowered:
        return 'De boa e tu?'
    elif 'tchau' in lowered:
        return 'Até ;)'
    elif 'rolar dado' in lowered:
        return  f'Deu: {randint(1,20)}'
    else:
        return choice(['Não manjo o que tu falou ＞﹏＜',
                       'Que bagulho doido é esse? （︶^︶）',
                       'Cara, não ablo isso não (╬▔皿▔)╯'])
