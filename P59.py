def combination(string, n):
    result = []
    m = len(string)
    if m - n < n:
        n = m - n

    if n < 0:
        return None
    elif n == 0:
        return string
    elif n == 1:
        return [char for char in string]
    else:
        for i in range(len(string)):
            remain = string[:i] + string[i + 1:]
            letter = string[i]
            result += list(map(lambda x: letter + x,
                               combination(remain, n - 1)))
        return set(result)


def XOR_decryption(message, key):
    return [message[i] ^ ord(key[i % 3]) for i in range(len(message))]


def get_text(message):
    text = ''
    for char in map(chr, message):
        text += char
    return text


def test_valid(message, word_list):
    text = get_text(message)
    # words=text.lower().strip('!,.?').split(' ')

    count = 0
    for word in word_list:
        if word in text:
            count += 1
    return count

with open('p059_cipher.txt') as f:
    message = [int(char) for char in f.read().strip().split(',')]

with open('word_list.txt') as f:
    word_list = [i[:-1] for i in f.readlines()]


string = ''
for i in range(97, 123):
    string += chr(i)

key_set = combination(string, 3)


flag = 0
for key in key_set:
    decrypted = XOR_decryption(message, key)
    valid_num = test_valid(decrypted, word_list)
    if valid_num > flag:
        best = decrypted
        flag = valid_num

print(get_text(best))
print('\nThe answer is {0}'.format(sum(best)))
