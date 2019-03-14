while True:
    input_chunk = infile.read(1024)

    if len(input_chunk) == 0:
        # if we've reached the end of the file and it _is_ a 
        # multiple of 16 in length, pad 16 bytes with the value '16'
        end_of_line = True
        input_chunk += struct.pack('{}B'.format(16), *(16 * [16]))
    elif len(input_chunk) % 16 > 0:
        # if we don't have an input_chunk which is divisible by 16,
        # pad it by the remainder with bytes with the value of the
        # remainder
        end_of_line = True
        input_chunk_remainder =  16 - (len(input_chunk) % 16)
        input_chunk += struct.pack('{}B'.format(input_chunk_remainder),
                *(input_chunk_remainder * [input_chunk_remainder]))

    outfile.write(encryption_cipher.encrypt(input_chunk))

    if end_of_line:
        break
