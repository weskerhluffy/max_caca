'''
Created on 27/11/2016

@author: ernesto
'''
import sys
import logging
nivel_log = logging.ERROR
# nivel_log = logging.DEBUG

def crea_monton(numeros):
    for idx_num, nume in enumerate(numeros):
        num_ultimo = nume
        idx_act = idx_num
        while idx_act:
            num_act = numeros[(idx_act - 1) >> 1]
            if num_ultimo > num_act:
                numeros[idx_act] = num_act
            else:
                break
            idx_act = (idx_act - 1) >> 1
        assert numeros[idx_act] <= num_ultimo
        numeros[idx_act] = num_ultimo


def monton_sort(numeros):
    tam_nume = len(numeros)
    crea_monton(numeros)


    for idx_num, nume in enumerate(numeros):
        limite_heap = tam_nume - idx_num - 1
        num_ultimo = numeros[limite_heap]
        idx_act = 0
        numeros[limite_heap] = numeros[0]
        assert not limite_heap or numeros[limite_heap] >= numeros[limite_heap - 1]
        while ((idx_act << 1) | 1) < limite_heap:
            idx_i = (idx_act << 1) | 1
            idx_d = idx_i + 1
            if(idx_i < limite_heap):
                idx_maior = idx_i
            if(idx_d < limite_heap) and numeros[idx_i] < numeros[idx_d]:
                    idx_maior = idx_d
            num_act = numeros[idx_maior]
                
            if num_ultimo < num_act:
                numeros[idx_act] = num_act
            else:
                break
            idx_act = idx_maior
        numeros[idx_act] = num_ultimo

    return numeros


def max_mieda_core(numeros, tam_ventana):
    tam_numeros = len(numeros)
    idx_limite = tam_numeros - tam_ventana
    salto_idx = tam_ventana - 1
    min_caca = 0
    
    numeros_ord = monton_sort(numeros)
#    numeros_ord = sorted(numeros)
    
    min_caca = numeros_ord[tam_ventana - 1] - numeros_ord[0]
    for idx_nume, numero in enumerate(numeros_ord[:idx_limite + 1]):
        min_actual = 0
        idx_final = idx_nume + salto_idx
        min_actual = numeros_ord[idx_final] - numero
        if(min_actual < min_caca):
            min_caca = min_actual
    
    return min_caca

def max_mierda_main():
    lineas = list(sys.stdin)
    numeros = []
    
    tam_ventana = int(lineas[1])
    
    for caca in lineas[2:]:
        numeros.append(int(caca))
    
    
    res = max_mieda_core(numeros, tam_ventana)
    print(res)
    
        

if __name__ == '__main__':
        FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
        logging.basicConfig(level=nivel_log, format=FORMAT)
        max_mierda_main()

