import pandas as pd
from matriz import (matrizCorreta, matrizEscadinha, matrizEscadinhaEstendida,
                    matrizEscadinhaReversa, matrizInutilizavel_1,
                    matrizInutilizavel_2)


def isescadinha(dt_frame):
    rows = [i for i in range(len(dt_frame)-1)]
    columns = [i for i in range(len(dt_frame.columns)-1)]

    result = []
    for row in rows:
        if dt_frame.loc[row, 0] != dt_frame.loc[row + 1, 1]:
            result.append(False)
        else:
            result.append(True)

    for colum in columns:
        for i in range(len(columns)-1):
            if dt_frame.loc[i, colum] != dt_frame.loc[i+1, colum + 1]:
                result.append(False)
            else:
                result.append(True)

    return False if False in result else True


def ordena_escadinha(dt_frame):
    if isescadinha(dt_frame["dt"]):
        result = f" Matrix {dt_frame['index']} Atual\n{dt_frame['dt']}\n"
        for i in range(len(dt_frame["dt"])):
            data_frame = dt_frame["dt"].loc[i]
            idx_max = data_frame.idxmax()
            max_ate_tamanho = data_frame[idx_max+1:len(data_frame)]
            primeiro_ate_max = data_frame[0:idx_max+1]
            data_frame_ordem = max_ate_tamanho.append(primeiro_ate_max,
                                                      ignore_index=True)
            dt_frame["dt"].loc[i] = data_frame_ordem
        result += f" Matrix {dt_frame['index']} Depois\n{dt_frame['dt']}\n"
        return result
    else:
        return f' Matriz: {dt_frame["index"]} não é Escadinha'


def print_escadinha(data):
    return f' Matriz: {data["index"]} é Escadinha? {isescadinha(data["dt"])}'


if __name__ == '__main__':
    data_frames = (
        {'index': 'Correta', 'dt': pd.DataFrame(matrizCorreta)},
        {'index': 'Escadinha', 'dt': pd.DataFrame(matrizEscadinha)},
        {'index': 'EscadinhaEstendida',
            'dt': pd.DataFrame(matrizEscadinhaEstendida)},
        {'index': 'EscadinhaReversa',
            'dt': pd.DataFrame(matrizEscadinhaReversa)},
        {'index': 'Inutilizavel_1',
            'dt': pd.DataFrame(matrizInutilizavel_1)},
        {'index': 'Inutilizavel_2',
            'dt': pd.DataFrame(matrizInutilizavel_2)},
    )

    '''
    Verifica se há escadinha, dada uma matriz como os exemplos acima.
    '''
    print("1) Questão")
    check_escadinha = map(print_escadinha, data_frames)
    [print(i) for i in check_escadinha]

    '''
    Se houver escadinha, mapear os dados corretamente, retornando a matriz
    correta.
    '''
    print("2) Questão")
    ordena_escadinha = map(ordena_escadinha, data_frames)
    [print(i) for i in ordena_escadinha]
