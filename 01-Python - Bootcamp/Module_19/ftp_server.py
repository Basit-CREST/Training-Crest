from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer
import os

# Path to shared folder (e.g., Download folder)
shared_path = "/storage/emulated/0/My_FTP_server"

authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", shared_path, perm="elradfmwMT")
authorizer.add_anonymous(shared_path)  # Optional anonymous access

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("0.0.0.0", 2121), handler)
print(f"✅ FTP server started on port 2121, serving {shared_path}")
server.serve_forever()
