import main as foosball

nome = 'replay_golo_jv_1_ja_2.txt'

def le_replay(nome_ficheiro):
    '''
    Função que recebe o nome de um ficheiro contendo um replay, e que deverá
    retornar um dicionário com as seguintes chaves:
    bola - lista contendo tuplos com as coordenadas xx e yy da bola
    jogador_vermelho - lista contendo tuplos com as coordenadas xx e yy da do jogador\_vermelho
    jogador_azul - lista contendo tuplos com as coordenadas xx e yy da do jogador\_azul
    '''
    game_replay = {}
    replays = []
    with open(nome_ficheiro, 'r') as ficheiro:
        linhas = ficheiro.readlines()
        for linhas in linhas:
            replay = linhas.split(';')
            replays.append(replay)
        replay_bola = replays[0]
        replay_vermelho = replays[1]
        replay_azul = replays[2]
    
        replay_bola_pos = [(float(pos.split(',')[0]),float(pos.split(',')[1])) for pos in replay_bola]
        replay_vermelho_pos = [(float(pos.split(',')[0]),float(pos.split(',')[1])) for pos in replay_vermelho]
        replay_azul_pos = [(float(pos.split(',')[0]),float(pos.split(',')[1])) for pos in replay_azul]
    
        game_replay['bola'] = replay_bola_pos
        game_replay['jogador_vermelho'] = replay_vermelho_pos
        game_replay['jogador_azul'] = replay_azul_pos
    return game_replay

def main():
    estado_jogo = foosball.init_state()
    foosball.setup(estado_jogo, False)
    replay = le_replay(nome)
    for i in range(len(replay['bola'])):
        estado_jogo['janela'].update()
        estado_jogo['jogador_vermelho'].setpos(replay['jogador_vermelho'][i])
        estado_jogo['jogador_azul'].setpos(replay['jogador_azul'][i])
        estado_jogo['bola']['objeto'].setpos(replay['bola'][i])
    estado_jogo['janela'].exitonclick()


if __name__ == '__main__':
    main()