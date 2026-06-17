
1. Statische IP festlegen
Ziel:
Die IP-Adresse des Servers wird fest auf 192.168.24.104 gesetzt.

Verbindungsnamen ermitteln
- nmcli connection show
Typischer Name:
netplan-eth0


Statische IP konfigurieren:

- sudo nmcli connection modify netplan-eth0 \
- ipv4.addresses 192.168.24.104/24 \
- ipv4.gateway 192.168.24.254 \
- ipv4.dns "192.168.24.254" \
- ipv4.method manual

Änderung aktivieren
- sudo nmcli connection down netplan-eth0sudo 
- nmcli connection up netplan-eth0

Prüfung
- ip a
Erwartet:
IP-Adresse 192.168.24.104 ist gesetzt.

2. Benutzer anlegen
2.1 Benutzer „willi“ (kein Admin)

- sudo adduser willi

Passwort setzen:
1234

Dialog durchgehen und mit Y bestätigen.
Dieser Benutzer hat keine sudo-Rechte.

2.2 Benutzer „fernzugriff“
- sudo adduser fernzugriff

Passwort setzen:
12345

Dialog durchgehen und mit Y bestätigen.

2.3 Adminrechte für „fernzugriff“
- sudo usermod -aG sudo fernzugriff

Prüfung
- groups fernzugriff

Erwartet:
fernzugriff : fernzugriff sudo

Damit hat der Benutzer Administratorrechte.

3. SSH-Dienst installieren und aktivieren
Installation
- sudo apt updatesudo apt install openssh-server -y

Dienst starten und aktivieren
- sudo systemctl enable sshsudo systemctl start ssh

Status prüfen
- sudo systemctl status ssh

Erwartet:
active (running)
enabled


4. SSH-Zugriff einschränken
Nur der Benutzer fernzugriff darf sich verbinden.
Datei öffnen
- sudo nano /etc/ssh/sshd_config

Folgende Zeile hinzufügen
- AllowUsers fernzugriff

Dienst neu starten
- sudo systemctl restart ssh

5. SSH-Verbindung herstellen
Wichtig: Gerät muss im WLAN R324-Public sein.
Verbindung
- ssh fernzugriff@192.168.24.104
Beim ersten Mal:
Are you sure you want to continue connecting?

→ yes

Login
Passwort: 12345

Danach bist du auf dem Server eingeloggt.


6. Docker installieren
- sudo apt-get update && sudo apt-get upgrade -y
- sudo apt install docker.io -y
- sudo systemctl enable docker.service
- sudo systemctl start docker.service

Test
- sudo docker run hello-world

7. Todo-App deployen
7.1 Repository klonen
- git clone https://github.com/gats100/todolist-repo ~/todolist

Falls nötig:
- sudo apt install git -y

7.2 Image bauen
- cd ~/todolistsudo docker build -t todolist-webapp .

7.3 Container starten
- sudo docker run -d -p 5000:5000 --name todolist todolist-webapp

8. Zugriff auf die Anwendung
Browser:
http://192.168.24.104:5000/

Beispiel:
HTTPGET http://192.168.24.104:5000/todo-list/1318d3d1-d979-47e1-a225-dab1751dbe75