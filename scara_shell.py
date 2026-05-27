#!/usr/bin/env python3
import cmd
import getpass
from datetime import datetime

class ScaraShell(cmd.Cmd):
    intro = r"""
 ╔══════════════════════════════════════════════════════════════╗
 ║                                                              ║
 ║   ███████╗ ██████╗ █████╗ ██████╗  █████╗                    ║
 ║   ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗                   ║
 ║   ███████╗██║     ███████║██████╔╝███████║                   ║
 ║   ╚════██║██║     ██╔══██║██╔══██╗██╔══██║                   ║
 ║   ███████║╚██████╗██║  ██║██║  ██║██║  ██║                   ║
 ║   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝                   ║
 ║                                                              ║
 ║   ███████╗██╗  ██╗███████╗██╗     ██╗                        ║
 ║   ██╔════╝██║  ██║██╔════╝██║     ██║                        ║
 ║   ███████╗███████║█████╗  ██║     ██║                        ║
 ║   ╚════██║██╔══██║██╔══╝  ██║     ██║                        ║
 ║   ███████║██║  ██║███████╗███████╗███████╗                   ║
 ║   ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝                   ║
 ║                                                              ║
 ║                [ NEURAL INTERFACE V3.1 ]                     ║
 ║                                                              ║
 ╚══════════════════════════════════════════════════════════════╝

"""

    prompt = "admin@scara:~$ "

    def __init__(self):
        super().__init__()
        self.user = None
        self.authenticated = False

    def do_login(self, arg):
        """login <username>"""
        username = arg.strip()
        if not username:
            print("Usage: login <username>")
            return

        password = getpass.getpass("Password: ")

        if username == "admin" and password == "lotus":
            self.user = username
            self.authenticated = True
            self.prompt = f"{username}@scara-core:~$ "
            print("Access granted.")
        else:
            print("Access denied.")

    def do_whoami(self, arg):
        """Show current user"""
        print(self.user if self.authenticated else "guest")

    def do_status(self, arg):
        """Show system status"""
        print("MIND: ONLINE")
        print("LINK: STABLE")
        print("SECURITY: OBSERVING")
        print("TIME:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def do_scan(self, arg):
        """Scan virtual system"""
        print("Scanning...")
        print("[OK] /core")
        print("[LOCKED] /sealed")
        print("[UNKNOWN] /abyss")

    def do_unlock(self, arg):
        """Unlock restricted area"""
        if not self.authenticated:
            print("Permission denied.")
            return

        print("Seal accepted.")
        print("Access to /sealed granted.")

    def do_exit(self, arg):
        """Exit shell"""
        print("Connection closed.")
        return True

    def do_EOF(self, arg):
        print()
        return self.do_exit(arg)

    def default(self, line):
        print(f"Unknown command: {line}")


if __name__ == "__main__":
    ScaraShell().cmdloop()