
from discord.ext import commands
import discord
# Define o comando
@commands.command(name='socorro')
async def socorro_command(ctx, *args):
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
        return ('!socorro comandos, para ver os comandos que eu sei <:actually:1263690743864758395>\n'
                '!socorro falas, para ver a falas, que eu respondo quando chamada <:1b:1259507885948534896>')

    if 'falas' in lowered:
        return ('Opa, eu consigo responder: \nbom dia\nvocê esta?\ntu esta?\nouvindo\nestá bem?\nesta fazendo?'
                '\noi\ntudo bem?\ntchau\nacademia\ntrilha favorita\n'
                'Qualquer ideia de implementação ou melhoria, fale com os meus desenvolvedores OwO')
    elif 'comandos' in lowered:
        return ('Opa, os comandos que eu aprendi, são: \nfalas\nd6\nd20\nd100\ncomandos\n'
                'Qualquer ideia de implementação ou melhoria, fale com os meus desenvolvedores OwO')


def setup(bot: commands.Bot):
    bot.add_command(socorro_command)