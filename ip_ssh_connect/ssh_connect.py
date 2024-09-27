#Импорт библиотеки для возможности подключения по SSH
#Import the SSH connection library
from fabric import Connection

#Список подсетей
#List of subnets
first_ip = '192.168.1.'
second_ip = '192.168.2.'

#Входные данные для авторизации по SSH
#Login data for authorization in SSH connection
user = 'type username here'
password = 'type password here'

#Базовое значение сети
#Default value of host
n = 0

#Функция подключения к компьютеру по SSH
#Funtion for SSH connect to IP-address
def ssh_connect(host, n):
    #Открываем текстовые файлы для записи полученных данных
    #Open txt-files for writing a received data
    ft1 = open('received_info.txt', 'w')
    ft2 = open('failed_ip.txt', 'w')
    #Цикл назначения IP-адреса в выбранной подсети от 0 до 255 и подключения к ней
    #Loop to assign an IP-address in the selected subnet from 0 to 255 and connecting to it
    while n <= 255:    
        ip_address = str(host)+str(n)
        n += 1
        #Попытка подключения к IP-адресу по SSH
        #Trying to connect to IP via SSH
        try:
            print('Connecting to ', ip_address)
            with Connection(ip_address, user=user, connect_timeout=1, connect_kwargs={'password': password}) as conn:
                #Пишет команду после подключения по SSH и заносит полученные данные в текстовой файл received_info.txt
                #Writing a command after succesful connecting via SSH and enters received data into a 'received_info.txt' file
                result = conn.run('type your command here')
                ft1.write(str(ip_address)+' '+str(result)+'\n\n\n')
                #Пишет команду после подключения по SSH и заносит полученные данные в текстовой файл received_info.txt
                #Writing a command after succesful connecting via SSH and enters received data into a 'received_info.txt' file
                result = conn.run("type your command here")
                ft1.write(str(result)+'\n\n\n')  
        #В случае неудачи код напишет в текстовой файл failed_ip.txt к какому IP-адресу не удалось подключится
        #In case of failure, the code will write to the text file 'failed_ip.txt' which IP address could not be connected to
        except Exception:
            ft2.write('Failed to connect to '+str(ip_address))
    #Закрываем текстовые файлы после внесения в них данных
    #Closing txt-files after entering data into them
    ft1.close()
    ft2.close()



#Функция выбора нужной подсети для получения IP-адреса
#Function of selecting the required subnet to obtain an IP address
def ip_connect():   
    #Спрашиваем пользователя об выборе нужной ему подсети
    #Asking the user to select the required subnet
    option_input = input('Enter the subnet number you want to connect:\n1. 192.168.1 2. 192.168.2 - ')

    #Если выбрана первая подсеть, то меняем host на выбранную нами подсеть и запускаем функцию ssh_connect()
    #If the first subnet is selected, then we change the host to the subnet we have selected and run the ssh_connect() function
    if option_input == '1':
        host_1 = first_ip
        ssh_connect(host_1, n)

    #Если выбрана вторая подсеть, то меняем host на выбранную нами подсеть и запускаем функцию ssh_connect()
    #If the second subnet is selected, then we change the host to the subnet we have selected and run the ssh_connect() function
    elif option_input == '2':
        host_2 = second_ip
        ssh_connect(host_2, n)
    
    #Если выбранной сети не в списке, то пишем пользователю об этом
    #If the selected network is not in the list, we write to the user about it
    else:
        print('Incorrect subnet selected.')

ip_connect()