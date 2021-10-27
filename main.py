from math import floor
'''float/int'''

def read_list():
    given = input("Dati numere separate prin virgula:")
    int_list = given.split(',')
    list = [ ]
    for int_lst in int_list:
        list.append(int(int_lst))
    return list

def read_list_float():
    given = input("Dati numere separate prin virgula:")
    float_list = given.split(',')
    list = [ ]
    for float_lst in float_list:
        list.append(float(float_lst))
    return list


'2.Toate numerele sunt prime'


def get_prim(n):
    '''
    Determina daca un numar este prim sau nu.
    :param n:
    :return:True-numarul este prim, False-numarul nu este prim
    '''
    if n<2:
        return False
    d=2
    while d*d<=n:
        if n%d==0:
            return False
        d=d+1
    return True

def test_get_prim():
    assert get_prim(3) == True
    assert get_prim(28) == False

test_get_prim()

def get_longest_all_primes(lst):
    '''
    Toate numerele sunt formate din cifre prime
    :param lst:
    :return:
    '''
    result=[]
    max=0
    poz=0

    for i in lst:
        if get_prim(i) == True:
            result.append(i)
            poz=poz+1
        else:
            if poz>max:
                finallist=[]
                j=0
                max=poz
                for j in result:
                    finallist.append(j)
            poz=0
            result=[]

    return finallist


'problema 13'

def cifre_prime(n):
    '''
    Verivica daca un numar este format din cifre prime.
    :param n:
    :return: True-toate cifrele din nr sunt prime, False-nu sunt toate cifrele din nr prime
    '''
    while n!=0:
        if get_prim(n%10)==False:
            return False
        else:
            n=n//10
    return True

def test_cifre_prime():
    assert cifre_prime(357)==True
    assert cifre_prime(224)==False

test_cifre_prime()

def get_longest_prime_digits(lst):
    '''
    Toate numerele sunt formate din cifre prime.
    :param lst:
    :return:
    '''
    result = [ ]
    max = 0
    poz = 0

    for i in lst:
        if cifre_prime(i) == True:
            result.append(i)
            poz = poz + 1
        else:
            if poz >max:
                finallist=[]
                max = poz
                for j in result:
                    finallist.append(j)
            result=[]
    return finallist

'problema 14'

def part(n):
    '''
    Determinam daca partea fractionara este egala cu cea intreaga
    :param n:
    :return:True-partiile sunt egale,False-nu sunt egale
    '''
    intreg=int(n)
    aux=n
    while aux%1!=0:
        aux=aux*10
        intreg=intreg*10
    aux=aux-intreg
    aux=int(aux)
    if aux==int(n):
        return True
    else:
        return False




def get_longest_equal_int_real(lst):
    '''
    Toate numerele au partea întreagă egală cu partea fracționară
    :param lst:
    :return:
    '''
    result = [ ]
    max = 0
    poz = 0
    finallist=[]
    for i in lst:
        if part(i) == True:
            result.append(i)
            poz = poz + 1
        else:

            if poz > max:

                finallist=[]
                max = poz
                for j in result:
                    finallist.append(j)
            result=[]

    return finallist



def print_main():
    print('1.Subsecventa numere prime. ')
    print('2.Subsecventa ')
    print('3.Partea intreaga egala cu partea fractionara. ')
    print('x.Iesire ')

def main():
    while True:
        print_main()
        op=input("Alegeti optiune:")
        if op=='1':
            lst= read_list()
            result=get_longest_all_primes(lst)
            print(result)
        if op=='2':
            lst=read_list()
            result=get_longest_prime_digits(lst)
            print(result)
        if op=='3':
            lst=read_list_float()
            result = get_longest_equal_int_real(lst)
            print(result)
        if op == 'x':
            break
        else:
            print("Optiune gresita! Reincearca:")


main()






