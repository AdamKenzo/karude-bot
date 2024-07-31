from random import choice, randint
from discord.ext import commands
import discord
# Define o comando
@commands.command(name='d')
async def dado_command(ctx, *args):
    user_message = ' '.join(args)
    response = get_response(user_message)

    # Verifica se a resposta é válida
    if response and response.strip():
        try:
            await ctx.send(response)
        except discord.errors.HTTPException as e:
            # Log específico para erro HTTP
            print(f'Erro HTTP ao enviar mensagem: {e}')
        except Exception as e:
            # Log para outros tipos de erros
            print(f'Erro ao enviar mensagem: {e}')
    else:
        print('(Resposta vazia não enviada)')

def get_response(user_input: str) -> str:
    lowered = user_input.lower()

    if lowered == '':
        return ('Você pode rolar diferentes tipos de dados:man_mage:, basta digitar ! mais:\n d 4;\n d 6;\n '
                'd 8;\n d 10;\n d 12;\n d 20;\n d 100 ')

    if '100' in lowered:
        return f'd100🎲 deu {randint(1, 100)}'
    elif '20' in lowered:
        return f'd20🎲 deu {randint(1, 20)}'
    elif '12' in lowered:
        return f'd12🎲 deu {randint(1, 12)}'
    elif '10' in lowered:
        return f'd10🎲 deu {randint(1, 10)}'
    elif '8' in lowered:
        return f'd8🎲 deu {randint(1, 8)}'
    elif '6' in lowered:
        return f'd6🎲 deu {randint(1, 6)}'
    elif '4' in lowered:
        return f'd4🎲 deu {randint(1, 4)}'

def setup(bot: commands.Bot):
    bot.add_command(dado_command)