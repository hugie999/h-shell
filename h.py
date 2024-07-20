#!/usr/bin/python3

__version__ = '0.0.1R'

import logging
import rich
import rich.console
import os
import typing
import readline
import re
import rich.style
import classes
import glob
import importlib.machinery
from pathlib import Path
import subprocess

if os.name == 'nt':
    raise NotImplementedError('windows is NOT supported')

HOME = Path(__file__).parent

logConfig = logging.basicConfig(filename='logs.log',filemode='w',level=logging.INFO,format='[%(name)s] (%(levelname)s) - %(message)s',force=True)

logs = logging.getLogger(__name__)
a = logging.StreamHandler()
a.setLevel(logging.INFO)
a.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
shellVars = {'FILE':None,'STRICT':False}
logs.info(HOME)
console = rich.console.Console()
console.style = rich.style.Style()
plugins:list[classes.plugin] = []
echoCommands = True
helpCommands = ['! - group','start (file)','help (command)','debug','echo (content)','loadPlugins','exit (code <- num)']
# theme = classes.theme('blue')

def loadPlugins():
    plugins:list[classes.plugin] = []
    for file in glob.glob(str(HOME)+'/plugins/*'):
        if file.split('/')[-1] in ['__pycache__','help.txt']:
            continue
        try:
            plugins.append(classes.plugin(importlib.machinery.SourceFileLoader(file,file).load_module()))
        except AssertionError:
            logs.warning(f"skiped plugin {file}")
        except Exception as e:
            logs.error(f'got error in plugin {file}',exc_info=e)
        else:
            if plugins[-1].apiVersion > 2:
                logs.info(f"loaded plugins: {plugins[-1].META['id']}")
            else:
                logs.info(f"loaded plugins: {plugins[-1].META['name']}")
                

def preProcessCommand(cmd:str,console:rich.console.Console,cd:Path) -> str:
    # if cmd.startswith('`'):
    #     starsWithSub = False
    #     logs.info('starts with substitution')
    # else:
    #     starsWithSub = False
    cmdSplit = cmd.split('`')
    origCmdSplit = cmd.split('`')
    substitutions = []
    logs.info(cmdSplit)
    
    for ind,val in enumerate(origCmdSplit):
        if ind%2!=0:
            cmdSplit.pop(ind)

    substitutions = re.findall('`.*`',cmd)
    
    logs.info(f'command: {cmdSplit}')
    logs.info(f'substitutions: {substitutions}')
    
    for ind,command in enumerate(substitutions):
        try:
            with console.capture() as cap:
                processCommand(command,console,cd,True)
            outPut = cap.get().removesuffix('\n')
        except classes.commandNotFoundError:
            outPut = subprocess.getoutput(command)
        cmdSplit.insert(ind*2+1,outPut)
    logs.info(f'command: {cmdSplit}')
    
    return ''.join(cmdSplit)

def processCommand(cmd:str,c:rich.console.Console,cd:Path,ensureNoSystemCommands:bool=False) -> int:
    global echoCommands
    commandSplit:list[str] = preProcessCommand(cmd,c,cd).split(' ')
    commandLength:int = len(commandSplit)
    if commandLength < 1:
        return
    match commandSplit[0]:
        case '!SETSTRICT':
            shellVars['STRICT'] = True
        case '!SETPOLITE':
            shellVars['STRICT'] = False
        case '!NOECHO':
            echoCommands = False
        case '!YESECHO':
            echoCommands = True
        case '!SETTO':
            if commandLength < 3:
                c.print('[red]bad amount of arguements[/]')
                logs.warning('(command error) !SETTO expected 2 arguments but got less')
                return 1
            varName = commandSplit[1]
            if varName == 'FILE':
                logs.warning('file tried to set FILE var')
                print('!FILE var cannot be set!')
                return 1
            else:
                shellVars[varName] = int(processCommand(' '.join(commandSplit)))
        case '!SET':
            varName = commandSplit[1]
            if varName == 'FILE':
                logs.warning('file tried to set FILE var')
                print('!FILE var cannot be set!')
                return 1
            else:
                if ' '.join(commandSplit[2:]).isdigit():
                    shellVars[varName] = int(' '.join(commandSplit[2:]))
                else:
                    shellVars[varName] = ' '.join(commandSplit[2:])
        case '!RUNIF':
            if commandLength < 3:
                c.print('[red]bad amount of arguements[/]')
                logs.warning('(command error) !RUNIF expected 2 arguments but got less')
                return 1
            if shellVars.get(commandSplit[1]) == 0:
                processCommand(' '.join(commandSplit[2:]))
        case 'start':
            runFile(' '.join(commandSplit[1:]),cd)
        case 'help':
            # c.print('not done.')
            with open(f'{HOME}/helps/index.txt') as f:
                c.print(f.read().format({'commands':helpCommands}))
        case 'debug':
            logs.setLevel(logging.DEBUG)
        case 'echo':
            c.print(' '.join(commandSplit[1:]))
        case 'loadPlugins':
            c.print('[blue]loading plugins...[/]')
            loadPlugins()
            for plug in plugins:
                print(plug)
            # plugins[0].docom(' '.join(commandSplit),['\x1b[0m','\x1b[0m'],cd)
        case 'plugman':
            for plug in plugins:
                print(plug.COMS)
        case 'exit':
            if commandLength > 1:
                quit(int(commandSplit[1]))
            else:
                quit(0)
        case _:
            didPlugin = False
            for plug in plugins:
                if commandSplit[0] in plug.COMS:
                    # print(plug.apiVersion)
                    if plug.apiVersion == 2:
                        try:
                            plug.docom(' '.join(commandSplit),['\x1b[0m','\x1b[0m'],cd,{'notice':'globals are no longer supplied in h-shell (rw)'},{'notice':'locals are no longer supplied in h-shell (rw)'})
                        except Exception as e:
                            logs.error(f'plugin error on plugin ({plug.META["name"]})')
                    else:
                        didPlugin = True
                        try:
                            return plug.runCommand(commandSplit,cd,c,c.style)
                        except Exception as e:
                            logs.error(f'plugin error on plugin ({plug.META["id"]})')
                            return 1
                            
                    didPlugin = True
                    return 0
            
            if not didPlugin:
                if ensureNoSystemCommands:
                    raise classes.commandNotFoundError('command not found!')
                else:
                    try:
                        code = subprocess.run(commandSplit).returncode
                    except FileNotFoundError:
                        c.print('[red]command not found![/]')
                        return 1
                    else:
                        # cd = os.getcwd()
                        return code
    return 0

def runFile(file:str,cd:Path):
    with open(file) as f:
        prevFile = shellVars['FILE']
        shellVars['FILE'] = file
        for line in f.readlines():
            if line.startswith('#!'):
                continue
            if echoCommands and line.removesuffix('\n') != '!NOECHO':
                print(f'({file})> {line.removesuffix("\n")}')
            processCommand(line.removesuffix("\n"),console,cd)
        shellVars['FILE'] = prevFile
def main():
    global echoCommands
    cd = Path(HOME)
    runFile('autoExec.hsh',cd)
                
    
    
    while True:
        shellVars['FILE'] = None
        # console.print(f'[green]h-shell ({__version__})>[/] ',end='')
        processCommand(input(console.render_str(f'[green]h-shell ({__version__})>[/] ',markup=True,style='green')),console,cd)
    
if __name__ == '__main__':
    print()
    main()