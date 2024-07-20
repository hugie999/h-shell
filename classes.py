#this file contains fake classes for typehintings
import typing
import pathlib
import importlib
import types
from pathlib import Path
import rich
import rich.style

class commandNotFoundError(Exception):
    pass

class metaDictV3(typing.TypedDict):
    id:str
    "the id of the plugin (eg 'ca.hugie999.hshell)"
    title:str
    "the title of the plugin (eg 'ls command')"
    description:str
    "what the plugin does"
    version:int
    "the version of the plugin"
    apiver:int
    "the api version"
    ver:int
    "the legacy api version (kept around for easier code) always 3 unless its an old plugin"
    type:str
    "the type of the plugin one of ('command', 'everyCommand')"

class metaDictV2(typing.TypedDict):
    name:str
    "the title of the plugin (eg 'ls command')"
    desc:str
    "what the plugin does"
    pluginver:int
    "the version of the plugin"
    type:int
    "the type of plugin (0 for command, 1 for every command)"
    oncommand:bool
    "if the plugin happens every command (im honestly not sure why this and type exsist)"
    doafter:bool
    "if the command happens before or after the user command (requires onc ommand to be true)"

class plugin:
    def __init__(self,plugin: types.ModuleType) -> None:
        self.module:types.ModuleType = plugin
        self.COMS:list[str] = self.module.COMS
        self.META:metaDictV3|metaDictV2 = self.module.META
        try:
            self.module.DONTLOAD
        except:
            pass
        else:
            if self.module.DONTLOAD:
                raise AssertionError("THIS PLUGIN HAS REQUESTED NOT TO BE LOADED")
        try:
            self.PLUGVER:int = self.module.PLUGVER
            "legacy plugin api version variale use meta['apiver'] instead"
        except AttributeError:
            raise AssertionError("THIS PLUGIN USES API VERSION 1 PLEASE USE V3")
        assert self.PLUGVER > 1, "THIS PLUGIN USES API VERSION 1 PLEASE USE V3"
        if "apiver" in self.META:
            self.apiVersion = self.META["apiver"]
        else:
            self.apiVersion = 2
        
        
        self.HELPCOMS:list[str] = self.module.HELPCOMS
        self.HELPDESCRIPTION:list[str] = self.module.HELPDESC
        if self.apiVersion == 2:
            self.docom:function = self.module.docom
        else:
            self.runCommand:function = self.module.runCommand
    def docom(comfull:str,themestr:list[str],cd:Path,GLOBALS:dict,LOCALS:dict):
        "does a command (legacy plugin)"
        pass
    def runCommand(command:list[str],cd:pathlib.Path,console:rich.console,style:rich.style.Style|str) -> int:
        "does a command in a plugin"
        pass
    def __str__(self) -> str:
        return f"(plugin with commands: {self.COMS})"