
def sum_binary(word1, word2):
    res = ''
    recargo = 0
    for i in range(len(word1)):
        pos = len(word1) - i - 1
        
        suma = int(word1[pos]) + int(word2[pos]) + recargo
        if(suma > 1):
            recargo = 1
        else:
            recargo = 0

        res = str(suma % 2) + res
        
        if recargo == 1 and pos == 0:
            res = sum_one (res)
    
    return res

def sum_one(word):
    res = ''
    recargo = 1
    
    for i in range(len(word)):
        pos = len(word) - i - 1
        suma = int(word[pos]) + recargo

        if suma > 1:
            recargo = 1
        else:
            recargo = 0

        res = str(suma % 2) + res
    return res

def create_checksum(binaries_list):
    resultado = binaries_list[0]
    for i in range(1, len(binaries_list)):
        resultado = sum_binary(resultado, binaries_list[i])

    return flip_binary(resultado)

def flip_binary(binary):
    inverse = ''

    for bit in binary:
        if bit == '1':
            inverse += '0'
        else:
            inverse += '1'

    return inverse

def check_checksum(binaries_list):
    resultado = binaries_list[0]
    for i in range(1, len(binaries_list)):
        resultado = sum_binary(resultado, binaries_list[i])

    if resultado.count('1') == 8:
        return True
    else:
        return False

palabra = '10110011101010110101101011010101'
groups = [palabra[i:i+8] for i in range(0, len(palabra), 8)]
# print(groups)

checksum = create_checksum(groups)
print(checksum)
groups.append(checksum)

print(check_checksum(groups))

