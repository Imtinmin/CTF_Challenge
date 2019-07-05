#
# Python Ping Sweep  GUI Application
#

import wxversion
wxversion.select("2.8")

import wx                   # Import the GUI module wx
import sys                  # Import the standard library module sys
import ping                # Import the ICMP Ping Module
import socket            # Import the standard library module socket

from time import gmtime, strftime   # import time functions

#
# Event Handler for the pingScan Button Press
#

def pingScan(event):

        # First, I need to check that the startHost is <= endHost value
        
        if hostEnd.GetValue() < hostStart.GetValue():
                
                # This is an improper setting
                # Notify the user and return

                dlg = wx.MessageDialog(mainWin,"Invalid Local Host Selection", "Confirm", wx.OK | wx.ICON_EXCLAMATION)
                result = dlg.ShowModal()
                dlg.Destroy()
                return
                
        # Update the Status Bar
        mainWin.StatusBar.SetStatusText('Executing Ping Sweep .... Please Wait')
        
        # Record the Start Time
        utcStart = gmtime()
        utc = strftime("%a, %d %b %Y %X +0000", utcStart)
        results.AppendText("\n\nPing Sweep Started: "+ utc+ "\n\n")

        # Build the base IP Address String
        # Extract data from the ip Range and host name user selections
        # Build a Python List of IP Addresses to Sweep
        
        baseIP = str(ipaRange.GetValue())+'.'+str(ipbRange.GetValue())+'.'+str(ipcRange.GetValue())+'.'

        ipRange = []

        for i in range(hostStart.GetValue(), (hostEnd.GetValue()+1)):
                ipRange.append(baseIP+str(i))

        # For each of the IP Addresses, Attempt an PING
        
        for ipAddress in ipRange:

                try:
        
                        # Report the IP Address to the Window Status Bar
                        mainWin.StatusBar.SetStatusText('Pinging IP: '+ ipAddress)
                        
                        # Perform the Ping
                        delay = ping.do_one(ipAddress, timeout=2)
                        
                        # Display the IP Address in the Main Window
                        results.AppendText(ipAddress+'\t')

                        if delay != None:
                                # If Successful (i.e. no timeout) display the result and response time 
                                results.AppendText('   Response Success')
                                results.AppendText('   Response Time: ' + str(delay) + ' Seconds')
                                results.AppendText("\n")
                        else :
                                # If delay == None, then the request timed out
                                results.AppendText('   Response Timeout')
                                results.AppendText("\n")

                except socket.error, e:
                        # for socket Errors Report the offending IP
                        results.AppendText(ipAddress)
                        results.AppendText('   Response Failed: ') 
                        results.AppendText(e.message)
                        results.AppendText("\n")

        # Record and display the ending time of the sweep
        utcEnd = gmtime()
        utc = strftime("%a, %d %b %Y %X +0000", utcEnd)
        results.AppendText("\nPing Sweep Ended: "+ utc + "\n\n")    

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
mainWin = wx.Frame(None, title="Simple Ping (ICMP) Sweeper 1.0", size =(1000,600))

#define the action panel

panelAction = wx.Panel(mainWin)

#define action buttons
# I'm creating two buttons, one for Scan and one for Exit
# Notice that each button contains the name of the function that will 
# handle the button press event.  pingScan and ProgramExit respectively

scanButton = wx.Button(panelAction, label='Scan')
scanButton.Bind(wx.EVT_BUTTON, pingScan)

exitButton  = wx.Button(panelAction, label='Exit')
exitButton.Bind(wx.EVT_BUTTON, programExit)

# define a Text Area where I can display results

results          = wx.TextCtrl(panelAction, style = wx.TE_MULTILINE | wx.HSCROLL)

# Base Network for Class C IP Addresses has 3 components
# For class C addresses, the first 3 octets define the network i.e 127.0.0
# the last 8 bits define the host i.e. 0-255

# Thus I setup 3 spin controls one for each of the 3 network octets
# I also, set the default value to 127.0.0 for convienence

ipaRange     = wx.SpinCtrl(panelAction, -1, '')
ipaRange.SetRange(0, 255)
ipaRange.SetValue(127)

ipbRange    = wx.SpinCtrl(panelAction, -1, '')
ipbRange.SetRange(0, 255)
ipbRange.SetValue(0)

ipcRange    = wx.SpinCtrl(panelAction, -1, '')
ipcRange.SetRange(0, 255)
ipcRange.SetValue(0)

# Also, I'm adding a lable for the user 

ipLabel         = wx.StaticText(panelAction, label="IP Base: ")

# Next, I want to provide the user with the ability to set the host range
# they wish to scan.  Maximum is 0 - 255

hostStart     = wx.SpinCtrl(panelAction, -1, '')
hostStart.SetRange(0, 255)
hostStart.SetValue(1)

hostEnd      = wx.SpinCtrl(panelAction, -1, '')
hostEnd.SetRange(0, 255)
hostEnd.SetValue(10)

HostStartLabel         = wx.StaticText(panelAction, label="Host Start: ")
HostEndLabel           = wx.StaticText(panelAction, label="Host End: ")

# Now I create BoxSizer to automatically align the different components neatly
# First, I create a horizontal Box
# I'm adding the buttons, ip Range and Host Spin Controls

actionBox = wx.BoxSizer()
actionBox.Add(scanButton,  proportion=1,  flag=wx.LEFT,  border=5)
actionBox.Add(exitButton,   proportion=0,  flag=wx.LEFT,  border=5)

actionBox.Add(ipLabel, proportion=0, flag=wx.LEFT|wx.CENTER, border=5)

actionBox.Add(ipaRange,      proportion=0,  flag=wx.LEFT,  border=5)
actionBox.Add(ipbRange,      proportion=0,  flag=wx.LEFT,  border=5)
actionBox.Add(ipcRange,      proportion=0,  flag=wx.LEFT,  border=5)

actionBox.Add(HostStartLabel, proportion=0, flag=wx.LEFT|wx.CENTER, border=5)
actionBox.Add(hostStart,      proportion=0,  flag=wx.LEFT,  border=5)

actionBox.Add(HostEndLabel, proportion=0, flag=wx.LEFT|wx.CENTER, border=5)
actionBox.Add(hostEnd,      proportion=0,  flag=wx.LEFT,  border=5)

# Next I create a Vertical Box that I place the Horizontal Box Inside
# Along with the results text area

vertBox = wx.BoxSizer(wx.VERTICAL)
vertBox.Add(actionBox, proportion=0, flag=wx.EXPAND | wx.ALL, border = 5)
vertBox.Add(results, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)

# I'm adding a status bar to the main windows to display status messages

mainWin.CreateStatusBar()

# Finally, I use the SetSizer function to automatically size the windows based on the
# the definitions above

panelAction.SetSizer(vertBox)

# Display the main window 

mainWin.Show()

# Enter the Applications Main Loop
# Awaiting User Actions

app.MainLoop()
