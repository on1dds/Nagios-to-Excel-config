# Nagios-to-Excel-config

Nagios core configurations quickly become huge. It is impossible to keep an overview of every configuration. Using nag2xls.py you can convert your configuration to a single excel file.

nag2xls.py
converts all valid .cfg object definition text files from the current directory to a single .xls file. The only object type you can't convert to excel is the timeperiod object since the directives are not consistent enought to convert to excel

Per .cfg file, a sheet will be generated. Every row in the sheet defines a new object (as described in the nagios definition pages)

Object types (command, contact, contactgroup, host, service, ...) are defined in column A. Other columns may be swapped as you prefer.

Check the Excel-to-Nagios-config project to generate .cfg files back from the .xls file
