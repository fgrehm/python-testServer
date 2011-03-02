Instalação
==========

Instale os pacotes OpenSSL e pyOpenSSL. No Ubuntu:

	apt-get install openssl python-openssl

Crie o arquivo server.pem, entrando na pasta do servidor, com o comando:

	openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes

Edite, como root, seu arquivo /etc/hosts, e acrescente a linha:

	127.0.0.1 pagseguro.uol.com.br

Enquanto esta linha estiver lá, sua máquina vai entender que o servidor pagseguro.uol.com.br é ela mesma. Naturalmente, você não conseguirá acessar o site do PagSeguro enquanto o ambiente de testes estiver ligado. Para desligá-lo, comente ou remova esta linha.

Edite o arquivo settings.py dentro da pasta pagseguroMockup e troque a url de retorno pela sua. Estamos no ambiente de testes, logo sua url pode começar com localhost.

Execute o arquivo PagSeguroServer.py, com o comando:

	python PagSeguroServer.py

Se você receber um mensagem “Permission denied”, significa que seu usuário não tem permissão para levantar um servidor na porta 443. Como alternativa, você pode executar o comando acima como root, com sudo:

	sudo  python PagSeguroServer.py

Já se você receber a mensagem “Address already in use”, significa que você já tem um servidor respondendo HTTPS. Talvez seja o Apache. Considere desabilitar o SSL do Apache, removendo o link simbólico /etc/apache2/mods-enabled/ssl.load.