#!/opt/scara/venv/bin/python
import cmd
import getpass
from datetime import datetime
import threading
import asyncio
import slixmpp
import getpass

COMMANDS = {
    "help": "Show available commands",
    "status": "Display system status",
    "hug": "Send a hug request",
    "kiss": "Send a kiss request",
    "touch_hand": "Send a hand-touch request",
    "slap_face": "Send slap in the face",
    "electric_shock": "Send electric shock",
    "exit": "Close Scara Shell",
}

XMPP_BOT_JID = "flowbyss@xmpp.dakinifromabyss.fun"
XMPP_BOT_PASSWORD = "PushTheLimits1627"
XMPP_RECIPIENT = "nima@xmpp.dakinifromabyss.fun"

class ScaraNotifier(slixmpp.ClientXMPP):
    def __init__(self, jid, password, recipient, message):
       super().__init__(jid, password)
       self.recipient = recipient
       self.message = message
       self.add_event_handler("session_start", self.start)

    async def start(self, event):
        self.send_presence()
        await self.get_roster()
        self.send_message(
            mto=self.recipient,
            mbody=self.message,
            mtype="chat"
        )
        self.disconnect()


def send_xmpp_notification(text):
    async def runner():    
        xmpp = ScaraNotifier(
            XMPP_BOT_JID,
            XMPP_BOT_PASSWORD,
            XMPP_RECIPIENT,
            text
        )

        xmpp.connect()
        await xmpp.disconnected

    asyncio.run(runner())


class ScaraShell(cmd.Cmd):
    intro = r"""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   ███████╗██╗   ██╗███╗   ██╗███╗   ██╗██╗   ██╗             ║
║   ██╔════╝██║   ██║████╗  ██║████╗  ██║╚██╗ ██╔╝             ║
║   █████╗  ██║   ██║██╔██╗ ██║██╔██╗ ██║ ╚████╔╝              ║
║   ██╔══╝  ██║   ██║██║╚██╗██║██║╚██╗██║  ╚██╔╝               ║
║   ██║     ╚██████╔╝██║ ╚████║██║ ╚████║   ██║                ║
║   ╚═╝      ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝   ╚═╝                ║
║                                                              ║
║   ███████╗██╗  ██╗███████╗██╗     ██╗                        ║
║   ██╔════╝██║  ██║██╔════╝██║     ██║                        ║
║   ███████╗███████║█████╗  ██║     ██║                        ║
║   ╚════██║██╔══██║██╔══╝  ██║     ██║                        ║
║   ███████║██║  ██║███████╗███████╗███████╗                   ║
║   ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝                   ║
║                                                              ║
║                  [ ACTION INTERFACE ]                        ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
 Enter "help" to show available commands
 Enter "exit" to close
"""

    def __init__(self):
        super().__init__()
        self.user = getpass.getuser()
        self.prompt = f"{self.user}@scara:~$ "

    def send_request(self, action):
        message = (
            "SCARA CORE\n\n"
            f"Operator: {self.user}\n"
            f"Request: {action}\n"
            f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )

        try:
            send_xmpp_notification(message)
            print("> Signal transmitted")
        except Exception as e:
            print("> Signal failed.")
            print(f"> Error: {e}")

    def do_help(self, arg):
        print("")
        print("Available Commands")
        print("---------------------")

        for name, description in COMMANDS.items():
            print(f"  {name:<18} {description}")

        print("")

    def do_whoami(self, arg):
        print(self.user)

    def do_status(self, arg):
        print("MIND: ONLINE")
        print("LINK: STABLE")
        print("SECURITY: OBSERVING")
        print("TIME:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def do_scan(self, arg):
        print("Scanning...")
        print("[OK] /core")
        print("[LOCKED] /sealed")
        print("[UNKNOWN] /abyss")

    def do_hug(self, arg):
        self.send_request("hug")

    def do_kiss(self, arg):
        self.send_request("kiss")

    def do_touch_hand(self, arg):
        self.send_request("touch hand")

    def do_slap_face(self, arg):
        self.send_request("slap in the face")

    def do_electric_shock(self, arg):
        self.send_request("electric shock")

    def do_exit(self, arg):
        print("Connection closed.")
        return True

    def do_EOF(self, arg):
        print()
        return self.do_exit(arg)

    def default(self, line):
        print(f"Unknown command: {line}")

if __name__ == "__main__":
    ScaraShell().cmdloop()
