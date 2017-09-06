
import getpass
import itertools
import string


#builds standard alphabet
alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]


#user selects action
def main():

    while True:
        action = raw_input('\nFor ENCRYPTION enter \'E\'\nFor DECRYPTION enter \'D\'\nTo QUIT enter \'Q\'\n  ').lower()
        if action == 'e':
	        encrypt()
        elif action == 'd':
	        decrypt()
        elif action == 'q':
	        quit()
        else:
            print('\nPLEASE ENTER \'E\' or \'D\' or \'Q\'!')
    

#builds new alphabet starting from character following (x)
def new_alpha(x):

    a = [chr(ord('a') + ((i-ord('a'))+x+1) % 26) for i in range(ord('a'), ord('z')+1)]
    return a


def encrypt():

    key = getpass.getpass('Please enter a key: ').lower()

    key = list(key.replace(' ',''))

    key_indices = [alphabet.index(l) for l in key]
	
    alphas = [new_alpha(x) for x in key_indices]
    
    msg = list((raw_input('Please enter a message to encrypt:\n')).lower())

    msg_indices = [alphabet.index(m) if m in alphabet else m for m in msg]

    c = itertools.cycle(alphas)

    translation = []

    for v in msg_indices:
    	try:
    		v = int(v)
    		translation.append(next(c)[v])
    	except ValueError:
    		translation.append(v)
    	
    new_msg = ''.join(x if x in alphabet else x for x in translation).upper()
    
    print '\n%s\n' % new_msg



def decrypt():

    key = getpass.getpass('Please enter a key: ').lower()

    key = list(key.replace(' ',''))

    matches = [alphabet.index(l) for l in key] 

    alphas = [new_alpha(x) for x in matches]
    
    msg = list((raw_input('Please enter a message to decrypt:\n')).lower())

    c = itertools.cycle(alphas)
    
    msg_indices = [next(c).index(i) if i in alphabet else i for i in msg]
    
    translation = []

    for t in msg_indices:
    	try:
    		t = int(t)
    		translation.append(alphabet[t])
    	except ValueError:
    		translation.append(t)
    
    orig_msg = ''.join(x for x in translation).upper()

    print '\n%s\n' % orig_msg


if __name__ == '__main__':
	main()


	




