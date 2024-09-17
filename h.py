#!/usr/bin/python3

__version__ = '0.0.2R'

import logging
import rich
import rich.color
import rich.console
import os
import typing
import readline
import io
import re
import rich.live
import rich.markdown
import rich.panel
import rich.screen
import rich.style
import rich.table
import rich.text
import classes
import glob
import hashlib
import importlib.machinery
from pathlib import Path
import subprocess
import json
import getch
import threading

if os.name == 'nt':
    raise NotImplementedError('windows is NOT supported')

HOME = Path(__file__).parent

logConfig = logging.basicConfig(filename='logs.log',filemode='w',level=logging.DEBUG,format='[%(name)s] (%(levelname)s) - %(message)s',force=True)

logs = logging.getLogger(__name__)
a = logging.StreamHandler()
a.setLevel(logging.INFO)
a.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
reservedShellVars = ['FILE','LINES','INPUT']
shellVars = {'FILE':None,'STRICT':False,'SPECIALCHARS':True,'DOCHECK':False,'SUM':None,'MULTILINE':False,'LINES':[],'LINENO':1,'TAGS':{},'PROMPT':'>','INPUT':None,'JUMPING':False,'JUMPLINES':-1,'newMode':False}
loadedFuntions = {'autoExec':'!NOECHO\necho empty...\necho `!GET FILE`'}
currentDirectory:Path = Path(HOME)
logs.info(HOME)
console = rich.console.Console()
console.style = rich.style.Style(color='green')
plugins:list[classes.plugin] = []
echoCommands = True
helpCommands = ['! - group','start (file)','help (command)','debug','echo (content)','loadPlugins','exit (code <- num)']
# theme = classes.theme('blue')

def loadPlugins():
    global plugins
    plugins = []
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

def runFuntion(funcName:str,funcArgs:tuple):
    if funcName in loadedFuntions:
        runFile(io.StringIO(loadedFuntions[funcName]),currentDirectory,fileName=f'__FUNC_{funcName}__')
    else:
        raise FileNotFoundError('no function')

def preProcessCommand(cmd:str,console:rich.console.Console,cd:Path) -> str:
    cmdSplit = cmd.split('`')
    origCmdSplit = cmd.split('`')
    substitutions = []
    logs.info(f'cmd: {cmdSplit}')
    
    for ind,val in enumerate(origCmdSplit):
        if ind%2!=0:
            cmdSplit.pop(ind)

    substitutions = re.findall('`.*`',cmd)
    for indx,value in enumerate(substitutions):
        value:str
        substitutions[indx] = value.removeprefix('`').removesuffix('`')
    
    
    
    logs.info(f'command: {cmdSplit}')
    logs.info(f'substitutions: {substitutions}')
    
    for ind,command in enumerate(substitutions):
        try:
            with console.capture() as cap:
                logs.info(f'run substituion: {command}')
                processCommand(command,console,ensureNoSystemCommands=True,dontAdvanceLines=True,dontAddLines=True)
            outPut = str(rich.text.Text.from_ansi(cap.get().removesuffix('\n')))
            logs.info(f'substitution output: {outPut}')
        except classes.commandNotFoundError:
            outPut = subprocess.getoutput(command)
        cmdSplit.insert(ind*2+1,outPut)
    logs.info(f'command: {cmdSplit}')
    
    return ''.join(cmdSplit)

def processCommand(cmd:str,c:rich.console.Console,*,ensureNoSystemCommands:bool=False,dontAdvanceLines:bool=False,dontAddLines:bool=False) -> int:
    global currentDirectory
    global echoCommands
    global shellVars
    global plugins
    commandSplit:list[str] = preProcessCommand(cmd,c,currentDirectory).split(' ')
    commandLength:int = len(commandSplit)
    if not dontAddLines:
        shellVars['LINES'].append(cmd)
    if not dontAdvanceLines:
        shellVars['LINENO'] += 1
    if len(cmd) < 1:
        return 0
    if cmd.startswith('#'):
        return 0
    if shellVars['JUMPING'] and commandSplit[0] != '!TAG' and shellVars['JUMPLINES'] > 0:
        shellVars['JUMPLINES'] -= 1
    elif shellVars['JUMPING'] and commandSplit[0] != '!TAG':
        shellVars['JUMPING'] = False
        shellVars['JUMPLINES'] = -1
    match commandSplit[0]:
        case '!FUNC':
            runFuntion(commandSplit[1],())
        case '!FUNCS':
            c.print(list(loadedFuntions.keys()))
        case '!TAG':
            if commandLength < 1:
                c.print('[red]bad amount of arguements[/]')
                return 1
            shellVars['TAGS'].update({commandSplit[1]:shellVars['LINENO']})
            if shellVars['JUMPING']:
                shellVars['JUMPING'] = False
                shellVars['JUMPLINES'] = -1
        case '!UNTAG':
            if commandLength < 1:
                c.print('[red]bad amount of arguements[/]')
                return 1
            shellVars['TAGS'].update({commandSplit[1]:shellVars['LINENO']})
        case '!GOTO':
            if commandLength < 1:
                c.print('[red]bad amount of arguements[/]')
                return 1
            if not commandSplit[1] in shellVars['TAGS']:
                c.print('[red]bad tag![/]')
                return 2
            lines = shellVars['LINENO']
            shellVars['LINENO'] = shellVars['TAGS'].get(commandSplit[1])-1
            logs.debug(f'pre lineno: {lines}')
            logs.debug(f'lineno: {shellVars['LINENO']}')
            logs.debug(f'lines: {shellVars['LINES']}')
            while shellVars['LINENO'] < lines-1:
                processCommand(shellVars['LINES'][shellVars['LINENO']],c,dontAddLines=True)
        case '!JUMP':
            if commandLength < 3:
                c.print('[red]bad amount of arguements[/]')
                return 1
            if commandSplit[1] in shellVars['TAGS']:
                c.print('[red]tag already exsists![/]')
                return 2
            shellVars['JUMPING'] = True
            shellVars['JUMPLINES'] = int(commandSplit[2])
        case '!MATH':
            if commandLength < 2:
                c.print('[red]bad amount of arguements[/]')
                return 1
            out = eval(' '.join(commandSplit[1:]),shellVars)
            if type(out) == bool:
                c.print(out)
                if out:
                    return 0
                else:
                    return 1
            if not str(out).isdigit():
                c.print('[red]bad math operation[/]')
                return 1
            else:
                c.print(int(out))
                return 0
        case '!CHECK':
            if commandLength == 1:
                shellVars['DOCHECK'] = True
            else:
                shellVars['SUM'] = commandSplit[1]
                shellVars['DOCHECK'] = True
        case '!SETSTRICT':
            shellVars['STRICT'] = True
        case '!SETPOLITE':
            shellVars['STRICT'] = False
        case '!NOECHO':
            echoCommands = False

        case '!YESECHO':
            echoCommands = True
        case '!VARS':
            c.print(shellVars)
        case '!GET':
            if commandLength < 2:
                c.print('[red]bad amount of arguements[/]')
                return 1
            c.print(shellVars[' '.join(commandSplit[1:])])
        # case '!SETTO':
        #     if commandLength < 3:
        #         c.print('[red]bad amount of arguements[/]')
        #         logs.warning('(command error) !SETTO expected 2 arguments but got less')
        #         return 1
        #     varName = commandSplit[1]
        #     if varName == 'FILE':
        #         logs.warning('file tried to set FILE var')
        #         print('!FILE var cannot be set!')
        #         return 1
        #     else:
        #         shellVars[varName] = int(processCommand(' '.join(commandSplit),c))
        case '!SET':
            varName = commandSplit[1]
            if varName in reservedShellVars:
                logs.warning(f'file tried to set {varName} var')
                print(f'!{varName} var cannot be set!')
                return 1
            else:
                if commandSplit[2] == 'True':
                    shellVars[varName] = True
                    logs.debug('var is bool')
                elif commandSplit[2] == 'False':
                    shellVars[varName] = False
                    logs.debug('var is bool')
                    
                elif ' '.join(commandSplit[2:]).isdigit():
                    shellVars[varName] = int(' '.join(commandSplit[2:]))
                    logs.debug('var is int')
                else:
                    shellVars[varName] = ' '.join(commandSplit[2:])
                logs.info(f'set shellvar: {varName} to {shellVars[varName]}')
        case '!RUNIF':
            if commandLength < 3:
                c.print('[red]bad amount of arguements[/]')
                logs.warning('(command error) !RUNIF expected 2 arguments but got less')
                return 1
            if (shellVars.get(commandSplit[1]) == 0 or shellVars.get(commandSplit[1]) == True) and shellVars.get(commandSplit[1]) != False:
                logs.debug('runif suceeded')
                return processCommand(' '.join(commandSplit[2:]),c,dontAddLines=True,dontAdvanceLines=True)
            else:
                logs.debug('runif failed')
        case '!FiLE':
            c.print()
        case 'inp':
            with getch.keyboardHolder() as k:
                print(k.read())
        case 'cd':
            if commandLength < 2:
                c.print('[red]this command needs at least one value![/]')
                return 1
            else:
                os.chdir(' '.join(commandSplit[1:]))
                currentDirectory = Path(os.getcwd())
                logs.info(f'new cd: {currentDirectory}')
        case 'start':
            runFile(' '.join(commandSplit[1:]),currentDirectory)
        case 'style':
            if commandLength == 1:
                c.print(console.style)
                # c.print('[red]not enough arguements[/]')
                return 1
                
            
            elif commandLength == 2:
                console.style += rich.style.Style(color =commandSplit[1])
            elif commandLength == 3:
                newStyle = rich.style.Style(**{commandSplit[1]:commandSplit[2]})
                console.style += newStyle
            else:
                return 2
            
        case 'help':
            # c.print('not done.')
            with open(f'{HOME}/helps/index.md') as f:
                # with c.pager():
                c.print(rich.markdown.Markdown(f.read().format({'commands':helpCommands})))
        case 'debug':
            logs.setLevel(logging.DEBUG)
        case 'echo':
            c.print(' '.join(commandSplit[1:]))
        case 'loadPlugins':
            # c.print('[blue]loading plugins...[/]')
            loadPlugins()
            # plugins[0].docom(' '.join(commandSplit),['\x1b[0m','\x1b[0m'],cd)
        case 'plugins':
            c.rule('avalible plugins:')
            for plug in plugins:
                if plug.apiVersion > 2:
                    c.print(plug.META['title'])
                else:
                    c.print(plug.META['name'])
            c.rule()
        case 'exit':
            if commandLength > 1:
                quit(int(commandSplit[1]))
            else:
                quit(0)
        case 'hist':
            t = rich.table.Table(expand=True)
            t.add_column('order',ratio=1)
            t.add_column('command',ratio=9)
            for indx,hist in enumerate(shellVars['LINES']):
                t.add_row(str(indx),hist)
            c.print(t)
        case _:
            didPlugin = False
            for plug in plugins:
                if commandSplit[0] in plug.COMS:
                    # print(plug.apiVersion)
                    if plug.apiVersion == 2:
                        try:
                            plug.docom(' '.join(commandSplit),['\x1b[0m','\x1b[0m'],currentDirectory,{'notice':'globals are no longer supplied in h-shell (rw)'},{'notice':'locals are no longer supplied in h-shell (rw)'})
                        except Exception as e:
                            logs.error(f'plugin error on plugin ({plug.META["name"]})',exc_info=e)
                            c.print('[red reverse]PLUGIN ERROR! (check logs.log)[/]')
                            return 1
                    else:
                        didPlugin = True
                        try:
                            return plug.runCommand(commandSplit,currentDirectory,c,c.style)
                        except Exception as e:
                            logs.error(f'plugin error on plugin ({plug.META["id"]})',exc_info=e)
                            c.print('[red reverse]PLUGIN ERROR! (check logs.log)[/]')
                            return 1
                    didPlugin = True
                    return 0
            if not didPlugin:
                if ensureNoSystemCommands:
                    logs.info(f'ensureNoSystemCommands passed for command: {cmd}')
                    raise classes.commandNotFoundError('command not found!')
                else:
                    try:
                        if shellVars['newMode']:
                            code = runShellCommandContained(commandSplit).returncode
                        else:
                            code = subprocess.run(commandSplit).returncode
                    except FileNotFoundError:
                        c.print('[red]command not found![/]')
                        return 1
                    except PermissionError:
                        c.print('[red]cannot run command! (permssion error)[/]\n[blue]--> please make sure the file is executable[/]')
                        
                    else:
                        currentDirectory = Path(os.getcwd())
                        return code
    return 0

def runShellCommandContained(com:list[str]) -> subprocess.Popen:
    try:
        newEnv = os.environ.copy()
        newEnv['COLUMNS'] = '5'
        process = subprocess.Popen(com,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,stdin=subprocess.PIPE,encoding='utf-8',env=newEnv)
        # process.stdin.write(input(':'))
        keys = ''
        def keyboardThreadFuntion():
            with getch.keyboardHolder() as key:
                k = key.read()
                keys += k
                process.stdin.write(k)
        pan = rich.panel.Panel('',title=com[0])
        # termSize = os.get_terminal_size()
        # getch.set_winsize(process.stdout.fileno(),termSize.lines,termSize.columns-2)
        keyboardThread = threading.Thread(None,keyboardThreadFuntion)
        keyboardThread.start()
        with rich.live.Live(pan) as live:
            pan.renderable += process.stdout.read()
    except KeyboardInterrupt:
        pass
    finally:
        process.wait(10)
        keyboardThread.join(3)
        console.print(pan)
    return process

def runFile(file:io.StringIO|str,cd:Path,*,fileName:str|None=None):
    global shellVars
    if type(file) == str:
        f = open(file)
    else:
        f = file
    prevLineNo = shellVars['LINENO']
    prevLines  = shellVars['LINES']
    prevTags   = shellVars['TAGS']
    prevCheck  = shellVars['DOCHECK']
    prevSum    = shellVars['SUM']
    shellVars['LINENO'] = 1
    shellVars['LINES']  = []
    shellVars['TAGS']   = {}

    
    prevFile = shellVars['FILE']
    if type(file) == str:
        shellVars['FILE'] = file
    else:
        shellVars['FILE'] = fileName
    for lNum,line in enumerate(f.readlines()):
        if shellVars['DOCHECK'] and not shellVars['SUM']:
            shellVars['DOCHECK'] = False
            lines = f.readlines()
            chkSum = hashlib.md5(''.join(lines[lNum:]).encode()).hexdigest()
            logs.info(f'sum is: {chkSum}')
            console.print(f'[green]checksum is: {chkSum}[/]')
        if shellVars['DOCHECK'] and shellVars['SUM']:
            shellVars['DOCHECK'] = False
            lines = f.readlines()
            chkSum = hashlib.md5(''.join(lines[lNum:]).encode()).hexdigest()
            logs.info(f'sum is: {chkSum}')
            if chkSum != shellVars['SUM']:
                logs.info(f'quit file due to bad sum: (expected: {shellVars["SUM"]}, got:{chkSum})')
                console.print(f'[red]invalid checksum (got: {chkSum}, expected: {shellVars["SUM"]})')
                break
            # console.print(f'[green]checksum is: {chkSum}[/]')
        
        if line.startswith('#!'):
            continue
        if echoCommands and line.removesuffix('\n') != '!NOECHO':
            print(f'({file})> {line.removesuffix("\n")}')
        processCommand(line.removesuffix("\n"),console)
    shellVars['FILE'] = prevFile
    shellVars['LINENO'] = prevLineNo
    shellVars['LINES']  = prevLines
    shellVars['TAGS']   = prevTags
    shellVars['DOCHECK'] = prevCheck
    shellVars['SUM'] = prevSum
    f.close()
def main():
    global echoCommands
    global currentDirectory
    runFile('autoExec.hsh',currentDirectory)
                
    
    
    while True:
        # shellVars['FILE'] = None
        # console.print(f'[green]h-shell ({__version__})>[/] ',end='')
        try:
            comList = ['!NOECHO']
            com = input(console.style.render(f'h-shell ({__version__})> '))
            if com == '!':
                itterations = 1
                com = input(console.style.render(f'0001> '))
                comList.append(com)
                while com != '!':
                    comList.append(com)
                    itterations += 1
                    com = input(console.style.render(f'{str(itterations).zfill(4)}> '))
                runFile(io.StringIO('\n'.join(comList)), currentDirectory,fileName='__CONSOLE__')
            else:
                try:
                    processCommand(com,console)
                except SystemExit:
                    quit(1)
                except:
                    console.print_exception()
                    if com == 'exit':
                        quit(1)
        except KeyboardInterrupt:
            console.print('[red bold]break![/]')
            console.print('[blue]-> tip: use "exit" to quit[/]')
            # quit(0)
        except Exception as e:
            console.print_exception()
            logs.error('error in processCommand loop',exc_info=e)
if __name__ == '__main__':
    print()
    main()