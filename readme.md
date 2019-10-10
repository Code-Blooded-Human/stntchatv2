This version contains a simple chat interface.

Run listen.py with argument as port (python listen.py <port-no>)

Then you may send message to another ip using (ensure that listen.py is running on remote machine)
echo "message" | python send.py <ip address> <port>

You may read recivied messages using python showchats.py