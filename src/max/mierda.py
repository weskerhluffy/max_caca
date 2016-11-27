'''
Created on 27/11/2016

@author: ernesto
'''
import sys
import logging
nivel_log = logging.ERROR
# nivel_log = logging.DEBUG
logger_cagada = None

def crea_monton(numeros):
    for idx_num, nume in enumerate(numeros):
        num_ultimo = nume
        idx_act = idx_num
        logger_cagada.debug("anadiendo %s en id %u" % (num_ultimo, idx_act))
        while idx_act:
            num_act = numeros[(idx_act - 1) >> 1]
            logger_cagada.debug("num act %u contra num ult %u en %u" % (num_act, num_ultimo, (idx_act - 1) >> 1))
            if num_ultimo > num_act:
                numeros[idx_act] = num_act
            else:
                break
            idx_act = (idx_act - 1) >> 1
        assert numeros[idx_act] <= num_ultimo
        numeros[idx_act] = num_ultimo
        logger_cagada.debug("finalmente %u kedo en %u" % (num_ultimo, idx_act))
#         logger_cagada.debug("nums asta aora %s"%numeros)
        for idx_nume in range(idx_num + 1):
            num_act_tmp = numeros[idx_nume]
            idx_i = (idx_nume << 1) | 1
            idx_d = idx_i + 1
            if(idx_i < idx_num + 1):
                assert numeros[idx_i] < num_act_tmp
                if(idx_d < idx_num + 1):
                    assert numeros[idx_d] < num_act_tmp, "l ijo der %u act %u" % (numeros[idx_d], num_act_tmp)
    logger_cagada.debug("nada orig %s" % (numeros))


def monton_sort(numeros):
    tam_nume = len(numeros)
    crea_monton(numeros)
    for idx_nume in range(tam_nume):
        num_act = numeros[idx_nume]
        idx_i = (idx_nume << 1) | 1
        idx_d = idx_i + 1
        if(idx_i < tam_nume):
            assert numeros[idx_i] < num_act
            if(idx_d < tam_nume):
                assert numeros[idx_d] < num_act, "l ijo der %u act %u" % (numeros[idx_d], num_act)


    logger_cagada.debug("el tope %u" % numeros[0])
    for idx_num, nume in enumerate(numeros):
        limite_heap = tam_nume - idx_num - 1
        num_ultimo = numeros[limite_heap]
        idx_act = 0
        logger_cagada.debug("num u;t %s limite heap %u" % (num_ultimo, limite_heap))
        numeros[limite_heap] = numeros[0]
        logger_cagada.debug("ordenado %u en pos %u" % (numeros[0], limite_heap))
        assert not limite_heap or numeros[limite_heap] >= numeros[limite_heap - 1]
        while ((idx_act << 1) | 1) < limite_heap:
            idx_i = (idx_act << 1) | 1
            idx_d = idx_i + 1
            if(idx_i < limite_heap):
                idx_maior = idx_i
            if(idx_d < limite_heap) and numeros[idx_i] < numeros[idx_d]:
                    idx_maior = idx_d
            num_act = numeros[idx_maior]
                
            logger_cagada.debug("num act %u contra num ult %u" % (num_act, num_ultimo))
            if num_ultimo < num_act:
                numeros[idx_act] = num_act
            else:
                break
            idx_act = idx_maior
        logger_cagada.debug("asignando %u a pos %u" % (num_ultimo, idx_act))
        numeros[idx_act] = num_ultimo
        logger_cagada.debug("nums asta aora %s" % numeros)
    logger_cagada.debug("alelu %s" % (numeros))

    logger_cagada.debug("die monster die %s" % numeros)
    return numeros


def max_mieda_core(numeros, tam_ventana):
    tam_numeros = len(numeros)
    idx_limite = tam_numeros - tam_ventana
    salto_idx = tam_ventana - 1
    min_caca = 0
    
#    numeros_ord = monton_sort(numeros)
    numeros_ord = sorted(numeros)
    logger_cagada.debug("go %s" % numeros_ord)
    
    min_caca = numeros_ord[tam_ventana - 1] - numeros_ord[0]
    for idx_nume, numero in enumerate(numeros_ord[:idx_limite + 1]):
        min_actual = 0
        idx_final = idx_nume + salto_idx
        logger_cagada.debug("when there is %u %u" % (idx_nume, idx_final))
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
    
    logger_cagada.debug("teen titans %s" % numeros)
    
    res = max_mieda_core(numeros, tam_ventana)
    print(res)
    
        

if __name__ == '__main__':
        FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
        logging.basicConfig(level=nivel_log, format=FORMAT)
        logger_cagada = logging.getLogger("asa")
        logger_cagada.setLevel(nivel_log)
        max_mierda_main()
