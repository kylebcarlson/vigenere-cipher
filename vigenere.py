
import getpass
import itertools


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
    #print key_indices
	
    alphas = [new_alpha(x) for x in key_indices]
    #print alphas
    
    msg = list((raw_input('Please enter a message to encrypt:\n')).lower())
    #print msg

    msg_indices= [alphabet.index(m) if m != ' ' else ' ' for m in msg]
    #print msg_indices

    c = itertools.cycle(alphas)
    
    translation = [next(c)[v] if v != ' ' else v for v in msg_indices]
   
    new_msg = ''.join(x for x in translation).upper()
    
    print '\n%s\n' % new_msg



def decrypt():

    key = getpass.getpass('Please enter a key: ').lower()

    key = list(key.replace(' ',''))

    matches = [alphabet.index(l) for l in key] 

    alphas = [new_alpha(x) for x in matches]
    
    msg = list((raw_input('Please enter a message to decrypt:\n')).lower())

    c = itertools.cycle(alphas)
    
    msg_indices = [next(c).index(i) if i != ' ' else i for i in msg]
    #print msg_indices

    translation = [alphabet[t] if t != ' ' else t for t in msg_indices]

    orig_msg = ''.join(x for x in translation).upper()

    print '\n%s\n' % orig_msg


if __name__ == '__main__':
	main()


	




