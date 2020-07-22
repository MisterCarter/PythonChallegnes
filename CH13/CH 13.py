import xmlrpc.client

server = 'http://www.pythonchallenge.com/pc/phonebook.php'

client = xmlrpc.client.ServerProxy(server)

print( client.system.listMethods())

x = client.system.listMethods()


print( client.system.methodHelp('phone'))
print( client.system.methodHelp('system.listMethods'))
print( client.system.methodHelp('system.methodHelp'))
print( client.system.methodHelp('system.methodSignature'))
print( client.system.methodHelp('system.multicall'))
print( client.system.methodHelp('system.getCapabilities'))

print (client.phone('Bert'))
print (client.phone('94112'))

