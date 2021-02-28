import discord, colorama, os
from colorama import init, Fore, Style, ansi, AnsiToWin32
colorama.init(convert=True)

TOKEN = "YourTokenHere"
p = True # Set to True if you want to send an automatic reply message everytime a non-friended user DM's you (Optional)
p_reply = "(automatically sent message) i might take a while to respond so yeah" # Custom automatic reply message (Optional)

# Insert a channel/server/groupchat/DM ID to blacklist them! (Optional)
server_blacklist = ()
channel_blacklist = ()
groupchat_blacklist = ()
dm_blacklist = ()

c_reset = Fore.RESET
c_resetall = Style.RESET_ALL
c_bright = Style.BRIGHT
c_normal = Style.NORMAL
c_green = Fore.GREEN
c_yellow = Fore.YELLOW
c_magenta = Fore.MAGENTA
c_blue = Fore.BLUE
c_red = Fore.RED
c_cyan = Fore.CYAN
c_white = Fore.WHITE
c_black = Fore.BLACK
c_lightmagenta = Fore.LIGHTMAGENTA_EX
c_lightred = Fore.LIGHTRED_EX
c_lightcyan = Fore.LIGHTCYAN_EX
c_lightgreen = Fore.LIGHTGREEN_EX
c_lightyellow = Fore.LIGHTYELLOW_EX
c_lightblue = Fore.LIGHTBLUE_EX
c_lightwhite = Fore.LIGHTWHITE_EX
c_lightblack = Fore.LIGHTBLACK_EX

def make_unicode(input):
    if type(input) != unicode:
        input =  input.decode('utf-8')
    return input

def main():
    ansi.clear_screen()

    sent = []
    appgreen = f"{c_reset}[{c_lightgreen}APP{c_reset}] "
    appred = f"[{c_reset}{c_lightred}APP{c_reset}] "
    class Client(discord.Client):
        async def on_ready(self):
            print(f"{appgreen}Selfbot {Fore.MAGENTA}{self.user}{Fore.RESET} ready!")
        async def on_message(self, message):
            a = message.author.id
            b = message.content
            def checkifpinged():
                if f"<@!{self.user.id}>" in message.content:
                    return f"{c_lightmagenta}PINGED{c_reset}, "
                else:
                    return ""
            #def returnuserid():
            #    if "<@!" in message.content:
            #        a = message.content.partition("<@!")
            #        userid = ""
            #        b = 0
            #        for i in a:
            #            if b == 18:
            #                return userid
            #            b += 1
            #            userid += i

            if message.channel.id not in channel_blacklist or message.author.id not in dm_blacklist:
                if isinstance(message.channel, discord.channel.DMChannel):
                    if p == True:
                        if message.author.id != self.user.id and message.channel.id not in sent and message.author not in self.user.friends:
                            sent.append(message.channel.id)
                            await message.channel.send(p_reply)
                    if a == self.user.id:
                        a = "You"
                    else:
                        a = message.author
                    if b == "":
                        b = f"{c_lightblack}User sent a file/started a call/pinned a message{c_reset}"
                    print(appgreen + f"({checkifpinged()}{c_yellow}DM{c_reset}) {c_lightred}{a}{c_reset}: {c_red}{b}{c_reset}")
                else:
                    try:
                        if message.guild.id not in server_blacklist:
                            if a == self.user.id:
                                a = "You"
                            else:
                                a = message.author
                            if b == "":
                                b = f"{c_lightblack}User sent a file/pinned a message{c_reset}"
                            #messag = message.content.replace("<@!" + returnuserid() + ">", "@" + await Client.fetch_user(returnuserid()).name)
                            print(appgreen + f'({checkifpinged()}{c_lightcyan}{message.guild.name}{c_reset}, {c_lightcyan}#{message.channel}{c_reset}) {c_green}{a}{c_reset}: {c_blue}{b}')
                    except:
                        if message.channel.id not in groupchat_blacklist:
                            if a == self.user.id:
                                a = "You"
                            else:
                                a = message.author
                            if b == "":
                                b = f"{c_lightblack}User sent a file/pinned a message{c_reset}"
                            print(appgreen + f"({checkifpinged()}{c_yellow}GROUP-CHAT{c_reset}) {c_lightred}{a}{c_reset}: {c_red}{b}{c_reset}")
  
    try:
        Client().run(TOKEN, bot=False)
    except Exception as e:
        ansi.clear_screen()
        exit(f"{c_reset}{appred}Error! {e}")

if __name__ == '__main__':
    main()
