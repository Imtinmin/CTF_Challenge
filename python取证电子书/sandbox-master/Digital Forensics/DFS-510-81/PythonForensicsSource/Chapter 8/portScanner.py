#
# Python Port Scanner
#

import wxversion
wxversion.select("2.8")

import wx                               # Import the GUI module wx
import sys                              # Import the standard library module sys
import ping                            # Import the ICMP Ping Module
from socket import *          # Import the standard library module socket

from time import gmtime, strftime   # import time functions

#
# Event Handler for the pingScan Button Press
#

def portScan(event):

        # First, I need to check that the starting port is <= ending port value
        
        if portEnd.GetValue() < portStart.GetValue():
                
                # This is an improper setting
                # Notify the user and return

                dlg = wx.MessageDialog(mainWin,"Invalid Host Port Selection", "Confirm", wx.OK | wx.ICON_EXCLAMATION)
                result = dlg.ShowModal()
                dlg.Destroy()
                return
                
        # Update the Status Bar
        mainWin.StatusBar.SetStatusText('Executing Port Scan .... Please Wait')
        
        # Record the Start Time
        utcStart = gmtime()
        utc = strftime("%a, %d %b %Y %X +0000", utcStart)
        results.AppendText("\n\nPort Scan Started: "+ utc+ "\n\n")

        # Build the base IP Address String
        # Extract data from the ip Range and host name user selections
        # Build a Python List of IP Addresses to Sweep
        
        baseIP = str(ipaRange.GetValue())+'.'+str(ipbRange.GetValue())+'.'+str(ipcRange.GetValue())+'.'+str(ipdRange.GetValue())

        # For  IP Addresses Specified Scan the Ports Specified

        for port in range(portStart.GetValue(), portEnd.GetValue()+1):

                try:
        
                        # Report the IP Address to the Window Status Bar
                        mainWin.StatusBar.SetStatusText('Scanning: '+ baseIP+' Port: '+str(port))
                                              
                        # open a socket
                        reqSocket = socket(AF_INET, SOCK_STREAM)
                        
                        # Try Connecting to the specified IP, Port
                      
                        response = reqSocket.connect_ex((baseIP, port))

                        if(response == 0) :
                                # Display the ipAddress and Port
                                results.AppendText(baseIP+'\t'+str(port)+'\t')                                
                                results.AppendText('Open')
                                results.AppendText("\n")
                        else:
                                if displayAll.GetValue() == True:
                                        results.AppendText(baseIP+'\t'+str(port)+'\t')           
                                        results.AppendText('Closed')            
                                        results.AppendText("\n")

                        reqSocket.close()                        
                        
                except socket.error, e:
                        # for socket Errors Report the offending IP
                        results.AppendText(baseIP+'\t'+str(port)+'\t')
                        results.AppendText('Failed: ') 
                        results.AppendText(e.message)
                        results.AppendText("\n")

        # Record and display the ending time of the sweep
        utcEnd = gmtime()
        utc = strftime("%a, %d %b %Y %X +0000", utcEnd)
        results.AppendText("\nPort Scan Ended: "+ utc + "\n\n")    

        # Clear the Status Bar
        mainWin.StatusBar.SetStatusText('')

# End Scan Event Handler ==========================


# 
# Program Exit Event Handler
#

def programExit(event):
        sys.exit()

# End Program Exit Event Handler =================

#
# Setup the Application Windows ==================
#

app = wx.App()

# define window
mainWin = wx.Frame(None, title="Simple Port Scanner", size =(1200,600))

#define the action panel

panelAction = wx.Panel(mainWin)

#define action buttons
# I'm creating two buttons, one for Scan and one for Exit
# Notice that each button contains the name of the function that will 
# handle the button press event.  Port Scan and ProgramExit respectively

displayAll    = wx.CheckBox(panelAction, -1, 'Display All', (10, 10))
displayAll.SetValue(True)

scanButton = wx.Button(panelAction, label='Scan')
scanButton.Bind(wx.EVT_BUTTON, portScan)

exitButton  = wx.Button(panelAction, label='Exit')
exitButton.Bind(wx.EVT_BUTTON, programExit)

# define a Text Area where I can display results

results = wx.TextCtrl(panelAction, style = wx.TE_MULTILINE | wx.HSCROLL)

# Base Network for Class C IP Addresses has 3 components
# For class C addresses, the first 3 octets define the network i.e 127.0.0
# the last 8 bits define the host i.e. 0-255

# Thus I setup 3 spin controls one for each of the 4 network octets
# I also, set the default value to 127.0.0.0 for convienence

ipaRange     = wx.SpinCtrl(panelAction, -1, '')
ipaRange.SetRange(0, 255)
ipaRange.SetValue(127)

ipbRange    = wx.SpinCtrl(panelAction, -1, '')
ipbRange.SetRange(0, 255)
ipbRange.SetValue(0)

ipcRange    = wx.SpinCtrl(panelAction, -1, '')
ipcRange.SetRange(0, 255)
ipcRange.SetValue(0)

ipdRange    = wx.SpinCtrl(panelAction, -1, '')
ipdRange.SetRange(0, 255)
ipdRange.SetValue(1)

# Also, I'm adding a lable for the user 

ipLabel         = wx.StaticText(panelAction, label="IP Address: ")

# Next, I want to provide the user with the ability to set the port range
# they wish to scan.  Maximum is 20 - 1025

portStart     = wx.SpinCtrl(panelAction, -1, '')
portStart.SetRange(1, 1025)
portStart.SetValue(1)

portEnd      = wx.SpinCtrl(panelAction, -1, '')
portEnd.SetRange(1, 1025)
portEnd.SetValue(5)

PortStartLabel         = wx.StaticText(panelAction, label="Port Start: ")
PortEndLabel           = wx.StaticText(panelAction, label="Port  End: ")

# Now I create BoxSizer to automatically align the different components neatly
# First, I create a horizontal Box
# I'm adding the buttons, ip Range and Host Spin Controls

actionBox = wx.BoxSizer()

actionBox.Add(displayAll,     proportion=0,  flag=wx.LEFT|wx.CENTER,  border=5)
actionBox.Add(scanButton,  proportion=0,  flag=wx.LEFT,  border=5)
actionBox.Add(exitButton,   proportion=0,  flag=wx.LEFT,  border=5)

actionBox.Add(ipLabel, proportion=0, flag=wx.LEFT|wx.CENTER, border=5)

actionBox.Add(ipaRange,      proportion=0,  flag=wx.LEFT,  border=5)
actionBox.Add(ipbRange,      proportion=0,  flag=wx.LEFT,  border=5)
actionBox.Add(ipcRange,      proportion=0,  flag=wx.LEFT,  border=5)
actionBox.Add(ipdRange,      proportion=0,  flag=wx.LEFT,  border=5)

actionBox.Add(PortStartLabel, proportion=0, flag=wx.LEFT|wx.CENTER, border=5)
actionBox.Add(portStart,      proportion=0,  flag=wx.LEFT,  border=5)

actionBox.Add(PortEndLabel, proportion=0, flag=wx.LEFT|wx.CENTER, border=5)
actionBox.Add(portEnd,      proportion=0,  flag=wx.LEFT,  border=5)

# Next I create a Vertical Box that I place the Horizontal Box Inside
# Along with the results text area

vertBox = wx.BoxSizer(wx.VERTICAL)
vertBox.Add(actionBox, proportion=0, flag=wx.EXPAND | wx.ALL, border = 5)
vertBox.Add(results, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)

# I'm adding a menu and status bar to the main window

mainWin.CreateStatusBar()

# Finally, I use the SetSizer function to automatically size the windows based on the
# the definitions above

panelAction.SetSizer(vertBox)

# Display the main window 

mainWin.Show()

# Enter the Applications Main Loop
# Awaiting User Actions

app.MainLoop()
