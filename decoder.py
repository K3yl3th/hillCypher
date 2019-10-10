# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 18:53:23 2019

@author: marie
"""
import hillCypher as hc

#MAIN PROGRAM
	
code = hc.code()
C = hc.matrix(code)

K = hc.chooseKey()
invK = hc.np.linalg.inv(K)

messageNumber = C.dot(invK)

message = hc.messageText(messageNumber, hc.alphabet)
message = "".join(message)

print("\nThe message is:")
print(message)

input("\nPress enter to exit the decoder")