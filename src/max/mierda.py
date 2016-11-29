'''
Created on 27/11/2016

@author: ernesto
'''
import sys
import logging
nivel_log = logging.ERROR
#nivel_log = logging.DEBUG
logger_cagada = None

def ordena_rapido_particionar(numeros,izq,der,pivote):
	idx_ordenados=izq-1
	for idx_actual in range(izq,der):
		if(numeros[idx_actual]<=pivote):
			idx_ordenados+=1
			temp=numeros[idx_ordenados]
			numeros[idx_ordenados]=numeros[idx_actual]
			numeros[idx_actual]=temp

	numeros[der]=numeros[idx_ordenados+1]
	idx_ordenados+=1
	numeros[idx_ordenados]=pivote
	return idx_ordenados
	

def ordena_rapido(numeros,izq,der):
	logger_cagada.debug("la izq %u der %u"%(izq,der))
	
	if(der-izq<=0):
		return
	else:
		pivote=numeros[der]
		pivote_nuevo=ordena_rapido_particionar(numeros,izq,der,pivote)
		logger_cagada.debug("el pivote nuevo %u"%pivote_nuevo)
		ordena_rapido(numeros,izq,pivote_nuevo-1)
		ordena_rapido(numeros,pivote_nuevo+1,der)
	return numeros


def max_mieda_core(numeros, tam_ventana):
    tam_numeros = len(numeros)
    idx_limite = tam_numeros - tam_ventana
    salto_idx = tam_ventana - 1
    min_caca = 0
    
#    numeros_ord = monton_sort(numeros)
#    numeros_ord = sorted(numeros)
    numeros_ord = ordena_rapido(numeros,0,len(numeros)-1)
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
