from modules import *
import argparse

p = argparse.ArgumentParser()
p.add_argument("-n", "--name", required=True, help="put your anime name")
p.add_argument("-f", "--filter", required=False, help="put your filters here", nargs='+')

input_arg = p.parse_args()

x = application.API().initialize(input_arg=input_arg.name)
print(x)