import PySimpleGUI as sg
import requests
import subprocess

appList = [
    {
        "appid": 1,
        "app_name": "visual studio code",
        "url": "https://az764295.vo.msecnd.net/stable/b7886d7461186a5eac768481578c1d7ca80e2d21/VSCodeUserSetup-x64-1.77.1.exe",
        "filename": "vscode.exe"
    },
    {
        "appid": 2,
        "app_name": "notepad++",
        "url": "https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.5.2/npp.8.5.2.Installer.x64.exe",
        "filename": "notepad++.exe"
    },
    {
        "appid": 3,
        "app_name": "node js",
        "url": "https://nodejs.org/dist/v18.15.0/node-v18.15.0-x64.msi",
        "filename": "nodejs.msi"
    },
    {
        "appid": 4,
        "app_name": "python 3.11",
        "url": "https://www.python.org/ftp/python/3.11.3/python-3.11.3-amd64.exe",
        "filename": "python.exe"
    },
    {
        "appid": 5,
        "app_name": "pycharm",
        "url": "https://download-cdn.jetbrains.com/python/pycharm-community-2023.1.exe",
        "filename": "pycharm.exe"
    },
    {
        "appid": 6,
        "app_name": "Eclipse IDE 2023‑03",
        "url": "https://www.eclipse.org/downloads/download.php?file=/oomph/epp/2023-03/R/eclipse-inst-jre-win64.exe",
        "filename": "eclipse.exe"
    },
    {
        "appid": 7,
        "app_name": "postman",
        "url": "https://dl.pstmn.io/download/latest/win64",
        "filename": "postman.exe"
    },
    {
        "appid": 8,
        "app_name": "Brave browser",
        "url": "https://referrals.brave.com/latest/BraveBrowserSetup-BRV010.exe",
        "filename": "brave.exe"
    },
    {
        "appid": 9,
        "app_name": "google chrome",
        "url": "https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7BB6D7CAE8-6795-8B95-62E0-CA053360DDDB%7D%26lang%3Den-GB%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe",
        "filename": "chrome.exe"
    },
    {
        "appid": 10,
        "app_name": "firefox",
        "url": "https://cdn.stubdownloader.services.mozilla.com/builds/firefox-stub/en-US/win/365f4b32496818d27303b1145d78fa4688bd631812f293c15b6abb2e094424f6/Firefox%20Installer.exe",
        "filename": "firefox.exe"
    },
    {
        "appid": 11,
        "app_name": "obs studio",
        "url": "https://cdn-fastly.obsproject.com/downloads/OBS-Studio-29.0.2-Full-Installer-x64.exe",
        "filename": "obs.exe"
    },
    {
        "appid": 12,
        "app_name": "xampp",
        "url": "https://sourceforge.net/projects/xampp/files/XAMPP%20Windows/8.0.28/xampp-windows-x64-8.0.28-0-VS16-installer.exe",
        "filename": "xampp.exe"
    }
]

sg.theme("Darkamber")
checkbox = [
    [
        sg.Checkbox("vscode", key="vscode.exe"),
        sg.Checkbox("notepad++", key="notepad++.exe"),
        sg.Checkbox("nodejs", key="nodejs.exe"),
        sg.Checkbox("chrome", key="chrome.exe"),
        sg.Checkbox("python3", key="python.exe"),
        sg.Checkbox("pycharm", key="pycharm.exe"),
        sg.Checkbox("eclipse", key="eclipse.exe"),
        sg.Checkbox("postman", key="postman.exe"),
        sg.Checkbox("brave", key="brave.exe"),
        sg.Checkbox("firefox", key="firefox.exe"),
        sg.Checkbox("obs", key="obs.exe"),
        sg.Checkbox("xampp", key="xampp.exe"),
    ],
]
buttons = [[sg.Submit("Install", auto_size_button=True), sg.Exit()]]

layout = [
    [
        sg.Text(
            "Express Installer",
            font=("Arial Bold", 20),
            size=20,
            expand_x=True,
            justification="center",
        )
    ],
    [
        sg.Text(
            "Choose Apps",
            font=("century gothic Bold", 15),
            expand_x=True,
            justification="center",
        )
    ],
    [sg.Column(checkbox, justification="center")],
    [sg.Column(buttons, justification="center")],
]

window = sg.Window("Express Installer", layout, resizable=True).Finalize()
# window.maximize()


def download(key):
    for x in appList:
        if x["filename"] == key:
            print(f"downloading {x['filename']}...")
            download_path = key
            response = requests.get(x['url'])
            with open(download_path, 'wb') as f:
                f.write(response.content)
            install_command = download_path
            subprocess.run(install_command, shell=True)
            break


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Install":
        for i in checkbox[0]:
            if values[i.key] == True:
                download(i.key)
window.close()
