# Основное задание

## Подготовка
$ ansible --version
ansible 2.10.5

# Самоконтроль выполненения задания

1. Где расположен файл с `some_fact` из второго пункта задания?  
**playbook/group_vars/all/examp.yml**

2. Какая команда нужна для запуска вашего `playbook` на окружении `test.yml`?  
**ansible-playbook site.yml -i ./inventory/test.yml**

3. Какой командой можно зашифровать файл?  
**ansible-vault encrypt <путь к файлу>**

4. Какой командой можно расшифровать файл?  
**ansible-vault decrypt <путь к файлу>**

5. Можно ли посмотреть содержимое зашифрованного файла без команды расшифровки файла? Если можно, то как?  
**ansible-vault view <путь к файлу>, ansible-vault edit <путь к файлу>**

6. Как выглядит команда запуска `playbook`, если переменные зашифрованы?  
**ansible-playbook site.yml -i ./inventory/prod.yml --ask-vault-pass** с последующим интерактивным вводом пароля, либо **ansible-playbook site.yml -i ./inventory/prod.yml --vault-password-file <путь к файлу с паролем>**

7. Как называется модуль подключения к host на windows?  
**Существует 2 модуля: psrp и winrm**  
ansible-doc -l -t connection | grep Microsoft  
psrp                           Run tasks over Microsoft PowerShell Remoting...  
winrm                          Run tasks over Microsoft's WinRM  

8. Приведите полный текст команды для поиска информации в документации ansible для модуля подключений ssh  
**ansible-doc -t connection ssh**

9. Какой параметр из модуля подключения `ssh` необходим для того, чтобы определить пользователя, под которым необходимо совершать подключение?  
**- remote_user**  
        User name with which to login to the remote server, normally set by the remote_user keyword.  
        If no user is supplied, Ansible will let the ssh client binary choose the user as it normally  
        [Default: (null)]  
        set_via:  
          env:  
          - name: ANSIBLE_REMOTE_USER  
          ini:  
          - key: remote_user  
            section: defaults  
          vars:  
          - name: ansible_user  
          - name: ansible_ssh_user  
        
