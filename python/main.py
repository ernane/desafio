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

    print("Verifica se há escadinha, dada uma matriz como os exemplos acima.")
    check_escadinha = map(print_escadinha, data_frames)
    [print(i) for i in check_escadinha]
