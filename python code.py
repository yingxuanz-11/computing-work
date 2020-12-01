   if version == 1 and isinstance(a, (str, bytes)):
            a = a.decode('latin-1') if isinstance(a, bytes) else a
            x = ord(a[0]) << 7 if a else 0
            for c in map(ord, a)
                x = ((1000003 * x) ^ c) & 0xFFFFFFFFFFFFFFFF
            x ^= len(a)
            a = -2 if x == -1 else x

    elif version == 2 and isinstance(a, (str, bytes, bytearray)):
            if isinstance(a, str):
                a = a.encode()
            a += _sha512(a).digest()
            a = int.from_bytes(a, 'big')

    elif not isinstance(a, (type(None), int, float, str, bytes, bytearray)):
               _warn('Seeding based on hashing is deprecated\n'
                     'since Python 3.9 and will be removed in a subsequent '
                     'version. The only \n'
                     'supported seed types are: None, '
                     'int, float, str, bytes, and bytearray.',
                     DeprecationWarning, 2)
