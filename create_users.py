import os

def createAdminUsers():
    os.system('useradd 2rp-guilherme')
    os.system('echo "ZCteAb0TMvQkg" | passwd 2rp-guilherme --stdin')
    os.system('usermod -aG wheel 2rp-guilherme')

    os.system('useradd 2rp-rene')
    os.system('echo "HJndjeSdjeinS" | passwd 2rp-rene --stdin')
    os.system('usermod -aG wheel 2rp-rene')

    os.system('useradd 2rp-cristiano')
    os.system('echo "fenwmiHDSsnDs" | passwd 2rp-cristiano --stdin')
    os.system('usermod -aG wheel 2rp-cristiano')

def createDefaultUsers():
    os.system('useradd 2rp-kevin')
    os.system('echo "mDkfekxlDgeFj" | passwd 2rp-kevin --stdin')

    os.system('useradd 2rp-marcio')
    os.system('echo "ikDmklFklmFkI" | passwd 2rp-marcio --stdin')

    os.system('useradd 2rp-lucas')
    os.system('echo "kNBIVuOygyHUg" | passwd 2rp-lucas --stdin')

    os.system('useradd 2rp-ioram')
    os.system('echo "UgdbhDYGssgru" | passwd 2rp-ioram --stdin')
    os.system('useradd 2rp-matheus')
    os.system('echo "fheuNDsjdheIS" | passwd 2rp-matheus --stdin')

createAdminUsers()
createDefaultUsers()



