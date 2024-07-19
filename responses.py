from random import choice, randint



def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if 'karudê' in lowered:
        if lowered == '':
            return 'Bom, você está terrivelmente silencioso (/_ \)'
        elif 'bom dia' in lowered:
            return choice(['Bom diaaa! S2',
                           'Ohayō :D',
                           'Salvee ヾ(•ω•`)o'])
        elif 'como você esta?' in lowered:
            return choice(['De boa na lagoa (￣o￣) . z Z',
                           'Estou escutando um Twice ❤',
                           'Só nos games ლ(╹◡╹ლ)'])
        elif 'como tu esta?' in lowered:
            return choice(['Só pelo churras －O－',
                           'Os gurizes estão bem ;P',
                           'Só no chimas ( •̀ ω •́ )✧'])
        elif 'ouvindo' in lowered:
            return choice(['Estou ouvindo twice - Like OOH-AHH',
                           'Estou ouvindo twice - CHEER UP',
                           'Estou ouvindo twice - TT',
                           'Estou ouvindo twice - Knock Knock',
                           'Estou ouvindo twice - Signal',
                           'Estou ouvindo twice - Likey',
                           'Estou ouvindo twice - Heart Shaker',
                           'Estou ouvindo twice - Brand New Girl',
                           'Estou ouvindo twice - Candy Pop',
                           'Estou ouvindo twice - What is Love?',
                           'Estou ouvindo twice - Dance The Night Away',
                           'Estou ouvindo twice - YES or YES',
                           'Estou ouvindo twice - The Best Thing I Ever Did',
                           'Estou ouvindo twice - Fancy (a melhor)',
                           'Estou ouvindo twice - Breakthrough',
                           'Estou ouvindo twice - Feel Special',
                           'Estou ouvindo twice - Fake & True',
                           'Estou ouvindo twice - More & More',
                           'Estou ouvindo System Of A Down - Toxicity',
                           'Estou ouvindo Slipknot - Psychosocial',
                           'Estou ouvindo Metallica - One',
                           'Estou ouvindo KoRn- Freak On a Leash',
                           'Estou ouvindo DJ Matt-D - Pandora',
                           'Estou ouvindo Foo Fighters - Everlong',
                           'Estou ouvindo Calypso - Entre Tapas e Beijos',
                           'Estou ouvindo Kyary Pamyu Pamyu - PONPONPON',
                           'Estou ouvindo BABYMETAL - Gimme chocolate!!',
                           'Estou ouvindo Gorillaz - 19-2000',
                           'Estou ouvindo Chico Buarque - Construção',
                           'Estou ouvindo Kyary Pamyu Pamyu - PONPONPON'])
        elif 'está bem' in lowered:
            return choice(['Estou tranquila :D',
                           'De buenas'])
        elif 'o que esta fazendo' in lowered:
            return choice(['Estou programando :actually:'])
        elif 'oi' in lowered:
            return choice(['Chama! o((>ω< ))o',
                           'yippieeee! ヾ(≧▽≦*)o'])
        elif 'tudo bem?' in lowered:
            return 'De boa e tu?'
        elif 'tchau' in lowered:
            return 'Até ;)'
        elif 'd20' in lowered:
            return  f'Deu: {randint(1,20)}'
        elif 'd100' in lowered:
            return  f'Deu: {randint(1,100)}'
        elif 'd6' in lowered:
            return  f'Deu: {randint(1,20)}'
        else:
            return choice(['Não manjo o que tu falou ＞﹏＜',
                           'Que bagulho doido é esse? （︶^︶）',
                           'Cara, não ablo isso não (╬▔皿▔)╯'])
