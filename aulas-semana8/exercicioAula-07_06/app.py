from Cliente import Cliente
from ClienteDAO import ClienteDAO

clienteDAO = ClienteDAO("arquivo.pkl")
cliente = Cliente(1, "Caio")

clienteDAO.add(cliente)
print(clienteDAO.get(1))

arquivo2 = ClienteDAO("arquivo.pkl")
arquivo2.add(Cliente(2, "Nicolas"))

print(arquivo2.get(2))
print(arquivo2.get(1))