# Hill Cypher

An hill cypher is used to encrypt and decode messages using matrices multiplications (one matrix being the message, and the other one the key). 

The implementation of this algorithm uses a 9-digit key.

# Dependencies

- [Python 3](https://www.python.org/)

## Installation

1. Clone the repository to your local machine, or copy the content of the [decoder.py](https://github.com/MarianneDery/hillCypher/blob/master/decoder.py), [encoder.py](https://github.com/MarianneDery/hillCypher/blob/master/encoder.py) and [hillCypher.py](https://github.com/MarianneDery/hillCypher/blob/master/hillCypher.py) files to local files in the same directory.
2. Open the terminal at the location of the files.
3. To encode a message, run it with the command `python encoder.py`
4. To decode a message, run it with the command `python decoder.py`
5. Enjoy!

## Encoding

To encode a message, you can either use your own key or generate a new one. Make sure to save it to decode the message. Once you have the key, give the message and the application will give you the encoded version.

## Decode

To decode a message, simply give the application the encoded message and the corresponding key, and let the magic happen!