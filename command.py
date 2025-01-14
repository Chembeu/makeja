import cmd
class HelloWorld(cmd.Cmd):
    """simple command processor example"""
    prompt = "chembeu > "
    intro = "Welcome to chembeu shell"
    def do_greet(self, line):
        print ("hello")
    def do_funga(self,arg):
        """Exiting the terminal"""
        print("Goodbye")
        return True
    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()