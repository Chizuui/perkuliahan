import zlib
import gzip
import rncryptor
cryptor = rncryptor.RNCryptor()

binary = gzip.open("SEB-Slearn.seb", 'rb')
f = binary.read()
binary.close()

#im getting error here
dec_data = (rncryptor.decrypt(f[4:], 'iitu'))

print(zlib.decompress(dec_data,15 + 32))