from ciente import Client
import discord
from discord import app_commands
import configparser

cliente = Client()
tree = app_commands.CommandTree(cliente)

config = configparser.ConfigParser()
config.read('config.ini')
tonk = config['DISCORD']['TONK']

print(type(tonk))