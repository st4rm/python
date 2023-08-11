# Read the contents of a file to replace a specific string.

filename = 'PBKDF(HMAC-SHA256)KAT.txt' 

with open(filename, 'r') as f:
    lines = f.readlines()

    with open(filename.split('.')[0] + '_Tests.' + filename.split('.')[1], 'w') as f:
        for line in lines:
            if 'MK = ' in line: 
                line = line.split()[0] + ' ' + line.split()[1] + '\n'  ## line = 'MK = \n'
                f.write(line)
            else:
                f.write(line)