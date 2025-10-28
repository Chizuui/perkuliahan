def salam(**person):
    print('Halo', person['NamaDepan'], person['NamaBelakang'])

salam(NamaDepan='Aldo', NamaBelakang='Siregar')
salam(NamaBelakang='Budi', NamaDepan='Santoso')
salam(NamaDepan='Budi', NamaBelakang='Santoso', usia=20)
salam(NamaDepan='Budi')
