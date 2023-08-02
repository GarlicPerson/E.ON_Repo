#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Needed Python packages:
#PyKCS11 
#pycryptodome


# In[ ]:


# Import packages

from PyKCS11 import *
from PyKCS11.LowLevel import *


# In[ ]:


# Set Filepath variables

bin_file_path = "D:\E.ON\E.ON_Repo\Encrypt_Data_Packet.bin"
signature_file_path = "D:\E.ON\E.ON_Repo\Enrypt_Data_Packet.sig"
pkcs11_library_path = "C:\Program Files\OpenSC Project\OpenSC\pkcs11\opensc-pkcs11.dll" 


# In[ ]:


# Save smartcard password into variable

password = "12345678"


# In[ ]:


# Load libraries

pkcs11 = PyKCS11Lib()
pkcs11.load(pkcs11_library_path)


# In[ ]:


# Get the available slots (smart card readers)
slots = pkcs11.getSlotList()


# In[ ]:


# Check if smartcard reader is available? If yes, how many slots
if not slots:
    print("No smart card reader found.")
    exit(1)


# In[ ]:


# Select the first slot
slot = slots[0]


# In[ ]:


# Smartcard session starts:
session = pkcs11.openSession(slot, CKF_SERIAL_SESSION | CKF_RW_SESSION)

try:
    #Enter pin:
    session.login(password)

    # Read the .bin file
    with open(bin_file_path, "rb") as file:
        binary_data = file.read()

    # Calculate the SHA256 hash of the .bin file
    sha256 = hashlib.sha256()
    sha256.update(binary_data)
    file_hash = bytearray(sha256.digest())

    # Find the private key on the smart card
    private_key = session.findObjects([
        (CKA_CLASS, CKO_PRIVATE_KEY),
        (CKA_KEY_TYPE, CKK_RSA),
        (CKA_SIGN, True),
    ])[0]

    # Sign the SHA256 hash of the .bin file
    signature = session.sign(private_key, file_hash, Mechanism(CKM_SHA256_RSA_PKCS))

    # Save the signature to a separate file
    with open(signature_file_path, "wb") as file:
        file.write(signature)

    print("File signed successfully. Signature saved to:", signature_file_path)

except PyKCS11Error as e:
    print("Error signing the message:", e)

finally:
    # Close the session
    session.closeSession()


# In[ ]:




